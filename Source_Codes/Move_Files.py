import shutil
import os

src = r""
dst = r""

counter = 1
with open("Log.txt", "w") as f:
    for root, folders, files in os.walk(src):
        for file in files:
            file_name, file_extension = os.path.splitext(file)
            src_path = os.path.join(root, file)
            dst_path = os.path.join(dst, file)

            # If file with same name exists in destination
            if os.path.exists(dst_path):
                print("Duplicate found!", file=file)
                new_file_name = f"{file_name}_{counter}{file_extension}"
                dst_path = os.path.join(dst, new_file_name)
                counter += 1

            shutil.copy2(src_path, dst_path)
            f.write(f"Copied: {src_path} -> {dst_path}\n")
