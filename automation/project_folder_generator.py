import os,shutil

PATH = "."


def create_file(file_name, mode, project_name="", folder_name=""):
    if not folder_name:
        full_path = os.path.join(PATH, project_name, file_name)
    else:

        full_path = os.path.join(PATH, project_name, folder_name, file_name)

    with open(full_path, mode) as f:
        f.write("#" + project_name)


def create_project(create_project_name):
    # create a folder
    os.makedirs(project_name, exist_ok=True)

    # src , data , docs, texts, assets

    folders = ["src", "data", "docs", "texts", "assets"]

    for folder in folders:
        os.mkdir(project_name + "/" + folder)

    print(f"{project_name} created successfully")


def delete_project(del_project_name):
    path = PATH + "/" + del_project_name
    if os.path.exists(path) and os.path.isdir(del_project_name):
        shutil.rmtree(del_project_name)
    else:
        print("project doesn't exists.")


def smart_project_generator(proj_name: str):
    proj_name = proj_name.strip()
    os.makedirs(proj_name, exist_ok=True)

    folders = ["src", "data", "docs", "tests"]

    for folder in folders:
        path = os.path.join(proj_name, folder)
        os.makedirs(path)

    # to create a file
    files_lst = ["README.md", "requirements.txt", "main.py"]
    for file in files_lst:
        if not file == "main.py":
            create_file(file, "w", proj_name)
        else:
            create_file(file, "w", project_name=proj_name, folder_name="src")


if __name__ == "__main__":
    user_confirmation = input("Do you want to create a project? (Y|N): ").lower()
    if user_confirmation == "y":
        project_name = input("Enter project name:: ").strip()
        # this is normal project
        # create_project(project_name)

        # smart_project_generator(project_name)

    elif user_confirmation == "n":
        print("Thanks.")
    else:
        print("Invalid Input!")
