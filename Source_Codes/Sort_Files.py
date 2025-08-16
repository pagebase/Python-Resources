import os
import shutil

try:
    src = r"D:\Rakesh_Environment\Photos"
    dst = r"D:\Rakesh_Environment\Temp"
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
