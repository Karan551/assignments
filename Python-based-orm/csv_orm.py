# csv_orm.py
import csv
import uuid
from datetime import datetime
from pathlib import Path
from typing import Dict, List

# Default database directory - can be customized using set_database_dir()
_DATABASE_DIR = "db"


def set_database_dir(path: str):
    """Set the database directory for CSV files."""
    global _DATABASE_DIR
    _DATABASE_DIR = path


def get_database_dir() -> str:
    """Get the current database directory."""
    return _DATABASE_DIR


class Field:
    def __init__(self, max_length=None, default=None, null=True):
        self.max_length = max_length
        self.default = default
        self.null = null
        self.name = None  # Will be set by metaclass

    def validate(self, value):
        if value is None and not self.null:
            raise ValueError(f"{self.name} cannot be null")
        return value

    def to_python(self, value):
        return value

    def to_csv(self, value):
        return str(value) if value is not None else ""


class CharField(Field):
    def validate(self, value):
        value = super().validate(value)
        if value and self.max_length and len(str(value)) > self.max_length:
            raise ValueError(f"{self.name} exceeds max_length of {self.max_length}")
        return value


class IntegerField(Field):
    def to_python(self, value):
        if value == "" or value is None:
            return None
        return int(value)


class DateTimeField(Field):
    def __init__(self, auto_now=False, auto_now_add=False, **kwargs):
        super().__init__(**kwargs)
        self.auto_now = auto_now
        self.auto_now_add = auto_now_add

    def to_python(self, value):
        if isinstance(value, str) and value:
            return datetime.fromisoformat(value)
        return value

    def to_csv(self, value):
        if isinstance(value, datetime):
            return value.isoformat()
        return str(value) if value else ""


class QuerySet:
    def __init__(self, model_class, data: List[Dict]):
        self.model_class = model_class
        self.data = data

    def filter(self, **kwargs):
        filtered_data = []
        for row in self.data:
            match = True
            for key, value in kwargs.items():
                if row.get(key) != str(value):
                    match = False
                    break
            if match:
                filtered_data.append(row)
        return QuerySet(self.model_class, filtered_data)

    def get(self, **kwargs):
        results = self.filter(**kwargs)
        if len(results.data) == 0:
            raise ValueError(
                f"{self.model_class.__name__} matching query does not exist"
            )
        if len(results.data) > 1:
            raise ValueError(f"Multiple {self.model_class.__name__} objects returned")
        return self.model_class._from_dict(results.data[0])

    def first(self):
        if self.data:
            return self.model_class._from_dict(self.data[0])
        return None

    def all(self):
        return QuerySet(self.model_class, self.data)

    def list(self):
        """Return a list of model instances"""
        return [self.model_class._from_dict(row) for row in self.data]

    def count(self):
        return len(self.data)

    def delete(self):
        """Delete all objects in this queryset"""
        if not self.data:
            return 0

        # Get IDs of all objects to delete
        ids_to_delete = {row.get("id") for row in self.data}

        # Load all data from CSV
        all_data = self.model_class._load_all_data()

        # Filter out the rows that should be deleted
        remaining_data = [row for row in all_data if row.get("id") not in ids_to_delete]

        # Calculate how many were actually deleted
        deleted_count = len(all_data) - len(remaining_data)

        # Save the remaining data back to CSV
        self.model_class._save_all_data(remaining_data)

        return deleted_count

    def __iter__(self):
        return iter([self.model_class._from_dict(row) for row in self.data])


class ModelMeta(type):
    def __new__(cls, name, bases, namespace):
        # Collect fields
        fields = {}
        for key, value in namespace.items():
            if isinstance(value, Field):
                value.name = key
                fields[key] = value

        # Add fields to namespace
        namespace["_fields"] = fields

        # Add id field if not present
        if "id" not in fields:
            id_field = CharField(max_length=36, default=lambda: str(uuid.uuid4()))
            id_field.name = "id"
            fields["id"] = id_field
            namespace["id"] = id_field

        return super().__new__(cls, name, bases, namespace)


class Model(metaclass=ModelMeta):
    def __init__(self, **kwargs):
        for field_name, field in self._fields.items():
            if field_name in kwargs:
                setattr(self, field_name, kwargs[field_name])
            elif field.default is not None:
                if callable(field.default):
                    setattr(self, field_name, field.default())
                else:
                    setattr(self, field_name, field.default)
            else:
                setattr(self, field_name, None)

        # Handle auto fields
        for field_name, field in self._fields.items():
            if isinstance(field, DateTimeField):
                if field.auto_now_add and getattr(self, field_name) is None:
                    setattr(self, field_name, datetime.now())

    @classmethod
    def _get_csv_filename(cls):
        db_dir = Path(_DATABASE_DIR)
        db_dir.mkdir(exist_ok=True)  # Create directory if it doesn't exist
        return db_dir / f"{cls.__name__.lower()}.csv"

    @classmethod
    def _get_fieldnames(cls):
        return list(cls._fields.keys())

    @classmethod
    def _load_all_data(cls):
        filename = cls._get_csv_filename()
        if not filename.exists():
            return []

        with open(filename, "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            return list(reader)

    @classmethod
    def _save_all_data(cls, data):
        filename = cls._get_csv_filename()
        fieldnames = cls._get_fieldnames()

        with open(filename, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

    @classmethod
    def _from_dict(cls, data_dict):
        instance = cls.__new__(cls)
        for field_name, field in cls._fields.items():
            value = data_dict.get(field_name, "")
            setattr(instance, field_name, field.to_python(value))
        return instance

    def _to_dict(self):
        result = {}
        for field_name, field in self._fields.items():
            value = getattr(self, field_name)
            result[field_name] = field.to_csv(value)
        return result

    def save(self):
        # Validate fields
        for field_name, field in self._fields.items():
            value = getattr(self, field_name)
            field.validate(value)

        # Handle auto_now fields
        for field_name, field in self._fields.items():
            if isinstance(field, DateTimeField) and field.auto_now:
                setattr(self, field_name, datetime.now())

        # Load existing data
        all_data = self._load_all_data()

        # Check if this is an update or create
        current_id = getattr(self, "id")
        updated = False

        for i, row in enumerate(all_data):
            if row.get("id") == current_id:
                all_data[i] = self._to_dict()
                updated = True
                break

        if not updated:
            all_data.append(self._to_dict())

        # Save back to CSV
        self._save_all_data(all_data)
        return self

    def delete(self):
        all_data = self._load_all_data()
        current_id = getattr(self, "id")

        all_data = [row for row in all_data if row.get("id") != current_id]
        self._save_all_data(all_data)

    @classmethod
    def objects(cls):
        return QuerySet(cls, cls._load_all_data())

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        instance.save()
        return instance

    def __str__(self):
        return f"{self.__class__.__name__}(id={getattr(self, 'id', 'None')})"

    def __repr__(self):
        fields_str = ", ".join([f"{k}={v!r}" for k, v in self._to_dict().items()])
        return f"{self.__class__.__name__}({fields_str})"
