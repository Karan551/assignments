import os
from odf.table import Table, TableRow, TableCell
from odf.opendocument import OpenDocumentSpreadsheet

ENV_PATH = "../../.env"


def read_dotenv_values(env_path):
    with open(env_path) as f:
        for line in f:
            if line.startswith("#") or line.strip() == "":
                continue

            key, value = line.strip().split("=", 1)
            os.environ[key] = value


if __name__ == "__main__":
    pass
