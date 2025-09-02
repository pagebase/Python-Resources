import os
import shutil

try:
    # This function handle duplicate files
    def handle_duplicate_file(dst, directory_name, file_name):
        name, ext = os.path.splitext(file_name)
        counter = 1
        new_file_name = f"{name}_{counter}{ext}"
        new_file_path = os.path.join(dst, directory_name, new_file_name)

        while os.path.exists(new_file_path):
            counter += 1
            new_file_name = f"{name}_{counter}{ext}"
            new_file_path = os.path.join(dst, directory_name, new_file_name)

        return new_file_path


    # Create directories function
    def create_directory(directory_names, dst):
        for i in directory_names:
            path = os.path.join(dst,i) # If source path is `C:\Sorted_Data` then `path` variable contains `C:\Sorted_Data\Photos`, `C:\Sorted_Data\Videos` etc
            os.makedirs(path, exist_ok=True) # 2nd parameter would not raise FileExistEror. If folder already exist then it will not create it and won't raise any error.

    def move_files(src, dst, file_ext_list, directory_name):
        for root, folders, files in os.walk(src):
            for file in files:
                if file.lower().endswith(tuple(file_ext_list)): # `endswith()` method takes `str` or `tuple of str` as argument.
                    full_src_path=os.path.join(root,file)
                    full_dst_path=os.path.join(dst,directory_name,file)
                    if os.path.exists(full_dst_path):
                        duplicate_full_path=handle_duplicate_file(dst, directory_name, file)
                        shutil.move(full_src_path, duplicate_full_path)
                    else:
                        shutil.move(full_src_path, full_dst_path)

    src=input("Enter source path: ").strip() # `strip()` method remove white spaces from left, right sides.
    user_choice=input("Source and destination path is same?(yes | no): ").strip().lower()
    if user_choice=="Yes".lower():
        dst=src
    else:
        dst=input("Enter destination path: ").strip()
    folder_names = ["Photos", "Videos", "Audio", "Documents", "Softwares", "Archives"]
    img_ext_list = [".png", ".jpeg", ".jpg", ".webp"]
    vid_ext_list = [".mp4", ".mkv", ".mov", ".wmv"]
    aud_ext_list = [".mp3", ".wav", ".aac"]
    doc_ext_list = [".pdf", ".csv", ".docx", ".pptx", ".txt", ".md", ".torrent"]
    soft_ext_list=[".exe"]
    arc_ext_list=[".zip"]
    counter=1

    # Create directory function call
    create_directory(folder_names, dst) # Create dircetories at destination as "Photos", "Videos", "Audio", "Documents"

    # Move images function call
    move_files(src, dst, img_ext_list, "Photos")
    move_files(src, dst, vid_ext_list, "Videos")
    move_files(src, dst, aud_ext_list, "Audio")
    move_files(src, dst, doc_ext_list, "Documents")
    move_files(src, dst, soft_ext_list, "Softwares")
    move_files(src, dst, arc_ext_list, "Archives")

except Exception as e:
    print(e)