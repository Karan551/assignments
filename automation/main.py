import os

PATH = "."


def check_user_input():
    user_input = input("Do you want to continue? (y/n):").lower()
    if user_input == "y":
        return True
    return False


def create_new_folder(folder_name="test"):
    os.makedirs(folder_name, exist_ok=True)


def create_file(file_name, folder_name=""):
    if folder_name:
        file = PATH + "/" + folder_name + "/" + file_name
    else:
        file = PATH + "/" + file_name

    print("this is file name::", file, file_name)
    with open(file, "x"):
        pass

    pass


def show_dirs():
    items = sorted(os.listdir(PATH))
    for dirs in items:
        if os.path.isdir(dirs):
            print(dirs)


def show_files():
    items = sorted(os.listdir(PATH))
    for file in items:
        if not os.path.isdir(file):
            print(file)


def create_five_folders():
    user_input = input("Are your want to create folder Y | N:: ").lower()
    if user_input == "n":
        return
    for i in range(1, 6):
        create_new_folder(f"Folder_{i}")
    print("Folder is created successfully.")


def remove_dirs(dir_name):
    remove_dir_name = PATH + "/" + dir_name
    if check_user_input():
        if os.path.isdir(remove_dir_name) and os.path.exists(remove_dir_name):
            os.removedirs(remove_dir_name)
        else:
            print("Dir is not exist.")
    else:
        print("process aborted.")


def remove_files():
    pass


# ------------------Function calling---------------------

create_new_folder('Test')
show_files()
# create_five_folders()
print("All dirs are:")
show_dirs()
# print("after delete dirs::")

# remove_dirs("Folder_5")
# show_dirs()
create_file("file_org.py", "Test")

"""
File organiser project banana hai. 12-03-2026(Today)

"""
