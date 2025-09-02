# Python File Handling Exercises

Here are some exercises to practice file handling in Python:

## Basic File Operations

1. **File Creation**: Write a program that creates a new text file named "welcome.txt" and writes "Hello, Welcome to Python!" into it.

2. **File Reading**: Write a program that reads the contents of "welcome.txt" and prints them to the console.

3. **Appending to File**: Write a program that appends "This is a new line" to the existing "welcome.txt" file.

4. **Line Count**: Write a program that counts how many lines are in a given file.

## Intermediate Exercises

5. **Word Count**: Write a program that counts how many words are in a given file.

6. **Character Count**: Write a program that counts how many characters (including spaces) are in a given file.

7. **File Copy**: Write a program that copies the contents of one file to another file.

8. **Specific Word Search**: Write a program that searches for a specific word in a file and prints all lines containing that word.

## Advanced Exercises

9. **CSV Processing**: Given a CSV file with student data (name, age, grade), write a program that:
   - Reads the file
   - Calculates the average grade
   - Finds the youngest and oldest student

10. **Log File Analysis**: Write a program that analyzes a server log file (you can create a sample one) and:
    - Counts how many errors (lines containing "ERROR") occurred
    - Finds the most common error message
    - Creates a new file with just the error lines

11. **File Encryption**: Write a program that:
    - Encrypts a file by shifting each character by 3 in the ASCII table
    - Decrypts the file back to its original form

12. **Merge Files**: Write a program that merges the contents of two files into a third file, alternating lines from each file.

## Challenge Problems

13. **Word Frequency Counter**: Write a program that counts how many times each word appears in a file and displays the top 10 most frequent words.

14. **Binary File Operations**: Write a program that:
    - Creates a binary file and writes some data to it
    - Reads the binary file and displays the data

15. **Directory Walker**: Write a program that goes through all files in a directory and its subdirectories, and prints the names of all .txt files.

---
# How to Walk Through Directories in Python

To walk through directories (including subdirectories) in Python, you can use the `os.walk()` function from the `os` module. Here's how it works:

## Basic Directory Walking

```python
import os

# Basic directory walk
for root, dirs, files in os.walk('.'):  # '.' means current directory
    print(f"Current directory: {root}")
    print(f"Subdirectories: {dirs}")
    print(f"Files: {files}")
    print("-" * 40)
```

## Finding Specific Files

Here's how to find all `.txt` files in a directory and its subdirectories:

```python
import os

txt_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.txt'):
            txt_files.append(os.path.join(root, file))

print("Found text files:")
for file in txt_files:
    print(file)
```

## Using `pathlib` (Python 3.4+)

The more modern `pathlib` module provides an object-oriented approach:

```python
from pathlib import Path

# Find all Python files in directory and subdirectories
py_files = list(Path('.').rglob('*.py'))

print("Python files found:")
for file in py_files:
    print(file)
```

## Practical Example: Directory Size Calculator

```python
import os

def get_directory_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # Skip if it's a symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size

size = get_directory_size('.')
print(f"Total directory size: {size} bytes")
```

## Filtering Directories

You can modify the `dirs` list in-place to skip certain directories:

```python
import os

for root, dirs, files in os.walk('.'):
    # Skip hidden directories (Unix-like systems)
    dirs[:] = [d for d in dirs if not d.startswith('.')]
    
    # Process remaining files
    for file in files:
        if file.endswith('.py'):
            print(os.path.join(root, file))
```

## Key Points:

1. `os.walk()` generates tuples of (root, directories, files) for each directory
2. It traverses directories top-down by default (use `topdown=False` for bottom-up)
3. You can modify the `dirs` list to control which subdirectories are visited
4. `pathlib.Path.rglob()` provides a simpler interface for common cases
5. Always use `os.path.join()` or `Path` objects to handle paths properly across operating systems

Would you like me to explain any specific aspect of directory walking in more detail?

---
Let me explain directory walking with a clear sample directory structure and step-by-step explanation.

## Sample Directory Structure

Imagine we have this folder structure:

```
my_project/
├── main.py
├── config/
│   ├── settings.ini
│   └── old_settings.bak
├── data/
│   ├── input.csv
│   └── processed/
│       └── output.csv
└── docs/
    ├── README.txt
    └── images/
        ├── logo.png
        └── screenshot.jpg
```

## Walking Through This Structure with `os.walk()`

Here's what happens when we run `os.walk('my_project')`:

```python
import os

for root, dirs, files in os.walk('my_project'):
    print(f"Directory: {root}")
    print(f"Subdirectories: {dirs}")
    print(f"Files: {files}")
    print("---")
```

### The Output Would Be:

1. **First Iteration (root level)**:
   ```
   Directory: my_project
   Subdirectories: ['config', 'data', 'docs']
   Files: ['main.py']
   ---
   ```

2. **Second Iteration (config/)**:
   ```
   Directory: my_project/config
   Subdirectories: []
   Files: ['settings.ini', 'old_settings.bak']
   ---
   ```

3. **Third Iteration (data/)**:
   ```
   Directory: my_project/data
   Subdirectories: ['processed']
   Files: ['input.csv']
   ---
   ```

4. **Fourth Iteration (data/processed/)**:
   ```
   Directory: my_project/data/processed
   Subdirectories: []
   Files: ['output.csv']
   ---
   ```

5. **Fifth Iteration (docs/)**:
   ```
   Directory: my_project/docs
   Subdirectories: ['images']
   Files: ['README.txt']
   ---
   ```

6. **Sixth Iteration (docs/images/)**:
   ```
   Directory: my_project/docs/images
   Subdirectories: []
   Files: ['logo.png', 'screenshot.jpg']
   ---
   ```

## Key Observations:

1. **Order of Traversal**: It goes depth-first, exploring each subdirectory completely before moving to siblings.

2. **The Three Values** in each iteration:
   - `root`: Current directory path
   - `dirs`: List of subdirectory names in current directory
   - `files`: List of filenames in current directory

3. **Modifying `dirs`**: You can alter the `dirs` list to control traversal:
   ```python
   for root, dirs, files in os.walk('my_project'):
       # Skip 'processed' directories
       if 'processed' in dirs:
           dirs.remove('processed')
   ```

4. **Getting Full Paths**: Use `os.path.join(root, file)` to get complete paths:
   ```python
   for root, dirs, files in os.walk('my_project'):
       for file in files:
           if file.endswith('.csv'):
               full_path = os.path.join(root, file)
               print(f"Found CSV: {full_path}")
   ```

## Practical Example: Find All Image Files

```python
import os

image_extensions = {'.png', '.jpg', '.jpeg'}
image_files = []

for root, dirs, files in os.walk('my_project'):
    for file in files:
        if os.path.splitext(file)[1].lower() in image_extensions:
            image_files.append(os.path.join(root, file))

print("Found images:")
for img in image_files:
    print(img)
```

This would output:
```
Found images:
my_project/docs/images/logo.png
my_project/docs/images/screenshot.jpg
```

Would you like me to demonstrate any other specific directory walking scenarios?