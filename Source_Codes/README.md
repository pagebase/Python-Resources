# Table of contents

1. [Sort files](#sort-files)
2. [List out existing drives](#list-out-existing-drives)

---
# Sort files

You have bunch of `JPG` files, `PDF` files, `MP4` files in your particular folder. You always select them manually, put them into their specified directories like:

- Audio
- Videos
- Photos
- Documents

You can do it by following `python` script. Just mention `source` and `destination` folder and **run** the program. In just seconds it sort your files and reduce your tedeous task. Don't say thanks to me, just tell me better ways to make it more robust and also contribute your creativity in it.

> Script 1

```python
import os
import shutil

try:
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
                    shutil.move(full_src_path, full_dst_path)

    src=input("Enter source path: ").strip() # `strip()` method remove white spaces from left, right sides.
    dst=input("Enter destination path: ").strip()
    folder_names = ["Photos", "Videos", "Audio", "Documents"]
    img_ext_list = [".png", ".jpeg", ".jpg", ".webp"]
    vid_ext_list = [".mp4", ".mkv", ".mov", ".wmv"]
    aud_ext_list = [".mp3", ".wav", ".aac"]
    doc_ext_list = [".pdf", ".csv", ".docx", "pptx"]

    # Create directory function call
    create_directory(folder_names, dst) # Create dircetories at destination as "Photos", "Videos", "Audio", "Documents"

    # Move images function call
    move_files(src, dst, img_ext_list, "Photos")
    move_files(src, dst, vid_ext_list, "Videos")
    move_files(src, dst, aud_ext_list, "Audio")
    move_files(src, dst, doc_ext_list, "Documents")

except Exception as e:
    print(e)

```

---
# List out existing drives

Did you ever checked how many of your drives present on your system? You onow the only way by heading to **This PC** and checking there how many drives are. You can check drives by `python` language too. Are you shocked? Don't worry, it's just tip of the iceberg.

> Script 2

```python
import os

# Check if drives are available
drives = []
for letter in range(65, 91):  # ASCII range for A-Z
    drive = f"{chr(letter)}:/"
    if os.path.exists(drive):
        drives.append(drive)

for i in drives:
    print(i)
```

---
