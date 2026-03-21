import hashlib, os, shutil

folders = {
    "Images": [".jpg", ".jpeg", ".gif", ".png", ".svg", ".webp", ".apng", ".avif"],
    "Documents": [".pdf", ".txt", ".docx", ".doc", ".odt", ".xlsx", ".xml", ".sketch"],
    "Music": [".mp3", ".wav", ".ogg", ".aac", ".wma"],
    "Video": [".mp4", ".mkv", ".avi", ".webm", ".wmv"],
    "Archives": [".zip", ".gz", ".xz"],
    "Packages": [".deb", ".vsix", ".oxt"]
}


def get_hash(file_path):
    with open(file_path, "rb") as f:
        file_data = f.read()
        return hashlib.sha256(file_data).hexdigest()


def get_hash_for_videos(file_path):
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def create_folder(parent_folder_path, folder_name):
    full_path = os.path.join(parent_folder_path, folder_name)
    os.makedirs(full_path, exist_ok=True)
    return full_path


def move_file_in_folder(file_path, dest_folder_path):
    file_name = os.path.basename(file_path)
    shutil.move(file_path, dest_folder_path)
    print(f"{file_name} moved successfully.")


def check_file_type(file_path):
    file_name = os.path.basename(file_path)
    if os.path.isfile(file_path):
        for folder, extensions in folders.items():
            if file_name.lower().endswith(tuple(extensions)):
                return folder

    return "Other"


def read_file(file_path, file_opening_mode="rb"):
    with open(file_path, file_opening_mode) as f:
        data = f.read()
        print("this is data\n", data)


def duplicate_file_finder_tool(folder_path):
    hashes = {}
    files = sorted(os.listdir(folder_path))
    for file in files:
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):

            file_hash = get_hash_for_videos(file_path) if check_file_type(file_path).lower() == "video" else get_hash(
                file_path)

            # if check_file_type(file_path).lower() == "video":
            #     file_hash = get_hash_for_videos(file_path)
            #
            # else:
            #     file_hash = get_hash(file_path)

            if file_hash in hashes:
                file_type = check_file_type(file_path)
                folder_name = f"duplicate_{file_type}_files"
                duplicate_folder_path = create_folder(folder_path, folder_name)

                move_file_in_folder(file_path, duplicate_folder_path)
            else:
                hashes[file_hash] = file
        else:
            print(f"{file} is not file.")


if __name__ == "__main__":
    # print(os.listdir("Images/"))
    print()

    # duplicate_file_finder_tool("Images")
    # duplicate_file_finder_tool("Images")
    folder_path = input("Enter folder path where you want to know the duplicate files:: ")
    duplicate_file_finder_tool(folder_path)

