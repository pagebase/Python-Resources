import os

fp=open("Log.md","w")

# Basic directory walk
for alphabet in range(65,91):
    if os.path.exists(f"{chr(alphabet)}:/"):
        for root, dirs, files in os.walk(f"{chr(alphabet)}:/"):
            for file in files:
                print(os.path.join(root, file))  # Prints full path to each file
                fp.write(f"# {os.path.join(root,file)}\n")
