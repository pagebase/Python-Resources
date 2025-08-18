import os

# Check if drives are available
drives = []
for letter in range(65, 91):  # ASCII range for A-Z
    drive = f"{chr(letter)}:/"
    if os.path.exists(drive):
        drives.append(drive)

for i in drives:
    print(i)