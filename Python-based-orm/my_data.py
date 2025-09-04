from models import Model, CharField, IntegerField, DateTimeField


# An ORM is a way that developers can write Python code that get converted into database calls.

# create an object
class Person(Model):
    name = CharField(max_length=255)
    age = IntegerField()
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)


class Blog(Model):
    title = CharField(max_length=255)
    content = CharField(max_length=1000)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)


# create an object
# ganesh = Person(name="Ganesh", age=25)
# ganesh.age = 18
#
# ganesh.save()


# print(ganesh._get_csv_filename())
# print(ganesh.__class__.__name__)
# To load all data
# for data in Person.objects.all():
#     print(data)

# Person.create(name="Manesh", age=21)
# print(Person.objects)

# print(list(Person.objects()))
# print(list(Person.objects().filter(name="Ganesh")))
# print(Person.objects().count())

# people = Person.objects.create(name="mahesh", age=21)
# people.save()
# print(Person.my_objects.create(name="Mahesh", age=25))
# print(people.count())
# Person.objects().create(name="Mahesh", age=21)
# mahesh = Person(name="Mahesh", age=25).save()
# print(mahesh._get_fieldnames())
# print(Person.objects().create(name="alok", age=23))

# for data in Person.objects():
#     print(data.name, data.age, data.id)


# ---------------------
js = Blog(title="JavaScript",
          content="JavaScript is a very funny language."
          )
js.save()
