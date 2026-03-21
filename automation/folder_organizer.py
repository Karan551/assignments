import os, shutil

PATH = "."
folders = {
    "Images": [".jpg", ".jpeg", ".gif", ".png", ".svg", ".webp", ".apng", ".avif"],
    "Documents": [".pdf", ".txt", ".docx", ".doc", ".odt", ".xlsx", ".xml", ".sketch"],
    "Music": [".mp3", ".wav", ".ogg", ".aac", ".wma"],
    "Video": [".mp4", ".mkv", ".avi", ".webm", ".wmv"],
    "Archives": [".zip", ".gz", ".xz"],
    "Packages": [".deb", ".vsix", ".oxt"]
}


# 1. get folder name 😃
# 2. list files in folder 😃
# 3. check that is file or not 😃
# 4. create folder 😃
# 5. and after move file in specific folder

def create_folder(folder_name):
    os.makedirs(folder_name, exist_ok=True)


def move_file_in_folder(file_path, folder_path):
    if os.path.isfile(file_path) and os.path.isdir(folder_path):
        shutil.move(file_path, folder_path)
        # print(f"Moved: {file_name} → {folder_name}")
        print(f"Moved--: {os.path.basename(file_path)} → {folder_path}")


# print("-----",os.path.join("Test", "Images"))


def folder_org(path):
    # 1. create a folder
    for folder in folders:
        folder_path = os.path.join(path, folder)
        create_folder(folder_path)

    # 2.  list all files
    all_files = os.listdir(path)

    for file in all_files:
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            for folder, extensions in folders.items():
                folder_path = os.path.join(path, folder)
                if file.lower().endswith(tuple(extensions)):
                    move_file_in_folder(file_path, folder_path)
                    break


if __name__ == "__main__":
    user_choice = input("Are you sure to organise the folder and files? (Y|N)").lower()

    if user_choice == "y":
        folder_path = input("Enter a folder name or folder_path:: ")
        folder_org(folder_path)
    else:
        print("thanks")
