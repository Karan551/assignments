import os
import time


def get_file_size(file_name: str, folder_name=""):
    if os.path.isfile(file_name):
        file_path = os.path.join(folder_name, file_name) if folder_name else file_name

        size_in_bytes = os.path.getsize(file_path)

        # size_in_kb = size_in_bytes / 2 ** 10 ( this is IEC standard)
        # size_in_mb = size_in_kb / 2 ** 10

        size_in_kb = size_in_bytes / 10 ** 3  # ( Here 1kb = 1000 bytes)
        size_in_mb = size_in_kb / 10 ** 3

        return size_in_kb, size_in_mb
    else:
        return None


def log_file_cleaner():
    files = os.listdir()

    for file in files:
        if os.path.isfile(file):
            if file.endswith((".log", ".cache", ".temp", ".bak", ".old", ".tmp", ".nomedia")):
                os.remove(file)
                print("Files deleted successfully.")


path = os.path.join("Test")
print(os.listdir(path))


def advance_log_file_cleaner(file_name, folder_name=""):
    """
    This function delete temporary file and large files greater than 5 mb
    :param file_name:
    :type file_name: str
    :param folder_name:
    :type folder_name:str
    :return:None
    :rtype:None
    """
    days_old = 30
    size_limit = 5 * 1024 * 1024
    file_path = os.path.join(folder_name, file_name) if folder_name else file_name

    for file in os.listdir(file_path):
        if os.path.isfile(file):

            file_size = get_file_size(file)[1]
            file_modified = os.path.getmtime(file_path)
            now = time.time()

            if file.endswith((".log", ".cache", ".temp", ".bak", ".old", ".tmp", ".nomedia")):
                os.remove(file)
                print("Deleted log file", file)
            elif file_size > size_limit:
                os.remove(file)
                print("Deleted large file", file)
            elif (now - file_modified) > (days_old * 86400):
                os.remove(file)
                print("Delete old file.")


if __name__ == "__main__":
    user_choice = input("Are you want to clear log files? Y|N : ").lower().strip()
    if user_choice == "y":
        log_file_cleaner()
    else:
        print("Thanks")

    print(os.path.getsize("./main.py"), type(os.path.getsize("./main.py")))
