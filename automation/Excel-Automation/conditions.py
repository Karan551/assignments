import pandas as pd
from write_data_ods import read_dotenv_values
import os
from index import create_new_sheet

ENV_PATH = "../../.env"
# set env values
read_dotenv_values(ENV_PATH)

ODS_PATH = os.environ.get("PATH", None)
EXCEL_FILE_PATH = os.environ.get("EXCEL_PATH", None)

df = pd.read_excel(ODS_PATH)
# print(df)

# And condition
filtered_data = df[(df["Marks"] >= 80) & (df["City"] == "Delhi")]
# print(filtered_data)
# print()

# Or condition
filtered_data_2 = df[(df["City"] == "Kanpur") | (df["City"] == "Delhi")]
# print(filtered_data_2)
# print()

# find top students
top_students = df[df["Marks"] > 80]
# print(top_students)
print()

# sort data
sorted_data = df.sort_values(by="Marks", ascending=False)
# print(sorted_data)
print()

# step selection columns
# print(df[["City", "Name", "Marks", "City"]])

# top students sheets

excel_file = pd.read_excel(EXCEL_FILE_PATH)

print(excel_file.isnull())
# top_students_data = excel_file[excel_file["Marks"] > 80]
# print(top_students_data)
# create_new_sheet(EXCEL_FILE_PATH, top_students_data, "top-students", False)
# print(excel_file)
