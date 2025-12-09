# File Handling & OS Operations

## Topics Covered

- Opening files (`r`, `w`, `a`, `x`)
- Reading files (`read`, `readline`)
- Looping through file lines
- Try/Except/Finally for safe file access
- Appending data
- Overwriting files
- Creating & deleting files using `os`
- Using `with open()` context manager

## Files in This Folder

- **files.py** — main script containing all file-handling operations
- **names.txt** — sample names file
- **more_names.txt** — extra text file
- **context.txt** — overwritten during execution

## Summary

Day 06 covers essential file handling operations in Python, including reading, writing, creating, deleting, and safely managing files.

### ✔ Opening Files

Used different file modes:

- `r` — read
- `w` — write (overwrite)
- `a` — append
- `x` — create new
- `t` — text mode
- `b` — binary mode

### ✔ Reading Data

Practiced:

- `f.read()` — full content
- `f.read(4)` — first 4 characters
- `f.readline()` — reading one line at a time

Looping through remaining lines with:

```python
for line in f:
    print(line)
```

### ✔ Error Handling

Wrapped file access inside `try` / `except` / `finally` to:

- Catch failures
- Show custom error messages
- Ensure file is always closed

### ✔ Appending & Overwriting

Added new text to `names.txt` using append mode, then overwrote `context.txt` using write mode.

### ✔ Creating & Deleting Files with os

Used:

- `os.path.exists()`
- `os.mknod()` — create file
- `os.remove()` — delete file

For conditional file creation & deletion logic.

### ✔ With-Statement (Context Manager)

Used:

```python
with open("names.txt") as f:
    content = f.read()
```

Automatically closes the file — safest and recommended method.

## Run

To execute all file-handling operations:

```bash
python3 files.py
```