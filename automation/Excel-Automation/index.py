import pandas as pd
import os
from write_data_ods import read_dotenv_values

ENV_PATH = "../../.env"
# set env values
read_dotenv_values(ENV_PATH)

PATH = os.environ.get("PATH", None)
EXCEL_PATH = os.environ.get("EXCEL_PATH", None)

sheet_data = {
    "Name": ["Ganesh", "Mahesh", "Alok", "Master", "Vibhuti", "KW"],
    "Age": [22, 21, 23, 20, 24, 22],
    "Marks": [80, 84, 90, 75, 82, 90],
    "City": ["Lucknow", "Hyderabad", "Kanpur", "Jhansi", "Delhi", "UK"]
}

new_data = {
    "Club": ["Drama", "Music", "Sports"],
    "Members": [20, 15, 40]
}

if os.path.exists(PATH):
    df = pd.read_excel(PATH, engine="odf")
    # print(df["index"])
    # print("this is excel data:: \n")
    # print(df["S.No."], "\n-here new value::\n", df["Age"])
    # print("this is first row::-")
    # print(df.iloc[0])
    # print("this is third row::-")
    # print(df.iloc[2])

    # loop through data
    # for index, row in df.iterrows():
    #     print(row["Name"], row["Marks"])
    #     print()
    # print(df.columns)
    # print(df.columns.str.strip())
    # df.columns = df.columns.str.strip()
    # print(df.columns)
    # print(df.get("Age", default="Unknown arguments"))


def read_excel_data(path: str):
    if os.path.exists(path):
        excel_file_data = pd.read_excel(path, engine="odf")

        for index, row in excel_file_data.iterrows():
            print(f"{row['Name']} scored {row['Marks']}")


def sort_sheet_data(sheet_path, label_name, sort_asc=True):
    if os.path.exists(sheet_path):
        excel_file_data = pd.read_excel(sheet_path, engine="odf")

        excel_file_data.columns = excel_file_data.columns.str.strip()
        value = excel_file_data.get(label_name)

        if value is not None:
            sorted_excel_file = excel_file_data.sort_values(by=label_name, ascending=sort_asc)
            return sorted_excel_file
        else:
            print("Column doesn't exist.")

    return "Sheet doest not exist."


def check_all_sheet_name(workbook_path):
    base, ext = os.path.splitext(workbook_path)
    if ext.lower().endswith((".xlsx", ".xls", ".xlsm")):
        xls = pd.ExcelFile(workbook_path)
        return xls.sheet_names

    elif ext.lower().endswith((".ods", ".odt", ".odt")):
        ods = pd.ExcelFile(workbook_path)
        return ods.sheet_names
    return None


def create_new_sheet(path, data, sheet_name: str, index_value: bool):
    if os.path.exists(path):
        df = pd.DataFrame(data=data)
        # df.to_excel(path, sheet_name=sheet_name, index=False)
        if sheet_name in check_all_sheet_name(path):
            raise Exception("Sheet name already exists! Please write a unique name in workbook.")

        with pd.ExcelWriter(path=path, mode="a") as writer:
            df.to_excel(writer, sheet_name=sheet_name, index=index_value)
            print("sheet created.")


if __name__ == "__main__":
    # read_excel_data(PATH)
    # sort_marks_wise(PATH)
    # column_name = input("enter column name that you want to sort:: ")
    # result = sort_sheet_data(PATH, column_name)
    # print(result)
    # print(check_all_sheet_name(EXCEL_PATH))
    # print(check_all_sheet_name(PATH))
    # create_new_sheet(EXCEL_PATH, sheet_data, "new-student-data-2")
    # create_new_sheet(PATH, sheet_data, "new-student-data")
    # create_new_sheet(EXCEL_PATH, new_data, "clubs")

    pass
