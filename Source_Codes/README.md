# Table of contents

1. [Sort files](#sort-files)

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
    src = r""
    dst = r""
    counter = 1
    image_ext = [
        ".jpg",
        ".jpeg",
        ".jpe",
        ".jfif",
        ".jif",
        ".png",
        ".gif",
        ".bmp",
        ".dib",
        ".tif",
        ".tiff",
        ".heif",
        ".heic",
        ".webp",
        ".avif",
        ".apng",
        ".jp2",
        ".j2k",
        ".jpf",
        ".jpx",
        ".jpm",
        ".ico",
        ".cur",
        ".dds",
        ".icns",
        ".pcx",
        ".tga",
        ".icb",
        ".vda",
        ".vst",
        ".ras",
        ".sgi",
        ".sid",
        ".raw",
        ".cr2",
        ".cr3", 
        ".nef", 
        ".arw",
        ".sr2",
        ".srf",
        ".orf",
        ".rw2",
        ".dng",
        ".raf",
        ".pef",  
        ".x3f", 
        ".erf", 
        ".kdc", 
        ".mrw",
        ".svg",
        ".eps",
        ".pdf",
        ".ai",
        ".cdr",
        ".fits",
        ".fit",
        ".fts",
        ".dicom",
        ".dcm",
        ".hdr",
        ".exr",
        ".jxr",
        ".hdp",
        ".wdp",
        ".emf",
        ".wmf",
    ]

    for root, folders, files in os.walk(src):
        for file in files:
            file_name, ext = os.path.splitext(file)
            if ext.lower() in [e.lower() for e in img_ext]:
                src_path = os.path.join(root, file)
                dst_path = os.path.join(dst, file)

                if os.path.exists(dst_path):
                    new_file_name = f"{file_name}_{counter}{ext}"
                    dst_path = os.path.join(dst, new_file_name)
                    counter += 1

                shutil.move(src_path, dst_path)

except Exception as e:
    print("Error:", e)
```
