import os


# ['vijay-thalapathy.jpg', 'thalapathy-thumbnail.jpg']
# file_name = "Guardians Of The Galaxy 2 Hindi Talking Scene.mp4"
# file_name_2 = "Guardians Of The Galaxy 2 Hindi Talking Scene.gif.mp3.mp4"

# folder_path = "."


def bulk_file_rename_tool(folder_path):
    if os.path.isdir(folder_path):
        images_extension = (".jpg", ".jpeg", ".gif", ".png", ".svg", ".webp", ".apng", ".avif")

        all_image_files = [file for file in os.listdir(folder_path)
                           if os.path.isfile(os.path.join(folder_path, file))
                           and file.lower().endswith(images_extension)
                           ]

        for index, file in enumerate(all_image_files, start=1):

            old_full_path = os.path.join(folder_path, file)

            # get file original extension
            base_name, extension = os.path.splitext(file)

            # create file new name with same extension
            file_new_name = f"images_{index}{extension}"

            # full path of new file name.
            file_new_full_path = os.path.join(folder_path, file_new_name)

            print(f"file old name {base_name}--> new name {file_new_name}")

            # safety check avoid overwriting
            counter = 1
            while os.path.exists(file_new_full_path):
                new_name = f"images_{index}_{counter}{extension}"
                file_new_full_path = os.path.join(folder_path, new_name)

                counter += 1
            os.rename(old_full_path, file_new_full_path)

        print("All files renamed successfully.")


# bulk_file_rename_tool("Images")

# print(file_name_2.endswith())


if __name__ == "__main__":
    user_confirmation = input("Do you want to rename image name? (Y|N):: ").lower()
    if user_confirmation == "y":
        folder_path = input("Give folder full path where you want to rename image name:: ")
        bulk_file_rename_tool(folder_path)

    else:
        print("Thanks!")
