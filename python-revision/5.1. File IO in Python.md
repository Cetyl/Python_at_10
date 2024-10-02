
# File I/O in Python

File Input/Output (I/O) is an essential part of programming that allows you to read from and write to files. Python provides built-in functions and methods to handle file operations efficiently. This guide will cover the basics of file I/O, including opening, reading, writing, and closing files.

## Table of Contents

1. [What is File I/O?](#what-is-file-io)
2. [Opening a File](#opening-a-file)
   - [Syntax](#syntax)
   - [Modes of Opening a File](#modes-of-opening-a-file)
3. [Reading from a File](#reading-from-a-file)
   - [Reading Entire File](#reading-entire-file)
   - [Reading Line by Line](#reading-line-by-line)
   - [Reading Specific Number of Characters](#reading-specific-number-of-characters)
4. [Writing to a File](#writing-to-a-file)
   - [Writing Strings](#writing-strings)
   - [Appending to a File](#appending-to-a-file)
5. [Closing a File](#closing-a-file)
6. [Using `with` Statement](#using-with-statement)
7. [Exception Handling](#exception-handling)
8. [Conclusion](#conclusion)

## What is File I/O?

File I/O refers to the process of reading data from and writing data to files stored on disk. This allows you to store data permanently, share data between programs, and work with large datasets efficiently.

## Opening a File

Before you can read from or write to a file, you must open it using the `open()` function.

### Syntax

```python
file_object = open("filename", mode)
```

### Modes of Opening a File

- **`'r'`**: Read (default mode). Opens a file for reading.
- **`'w'`**: Write. Opens a file for writing, truncating the file first.
- **`'a'`**: Append. Opens a file for writing, appending new data to the end of the file.
- **`'b'`**: Binary mode. Used to read or write binary files.
- **`'t'`**: Text mode (default). Used for text files.
- **`'x'`**: Exclusive creation. Fails if the file already exists.

## Reading from a File

Once a file is opened in read mode, you can read its contents using various methods.

### Reading Entire File

```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

### Reading Line by Line

```python
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())
```

### Reading Specific Number of Characters

```python
with open("example.txt", "r") as file:
    content = file.read(10)  # Reads the first 10 characters
    print(content)
```

## Writing to a File

You can write data to a file by opening it in write or append mode.

### Writing Strings

```python
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
```

### Appending to a File

```python
with open("output.txt", "a") as file:
    file.write("Appending a new line.\n")
```

## Closing a File

It’s important to close a file when you are done with it to free up system resources.

```python
file = open("example.txt", "r")
# ... perform file operations ...
file.close()
```

However, using the `with` statement (as shown earlier) automatically closes the file for you.

## Using `with` Statement

The `with` statement simplifies file handling by automatically closing the file once the block is exited. This is the recommended way to work with files in Python.

```python
with open("example.txt", "r") as file:
    content = file.read()
```

## Exception Handling

It’s good practice to handle exceptions while working with files to avoid runtime errors. You can use `try` and `except` blocks to catch exceptions.

```python
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")
```

## Conclusion

File I/O in Python is a straightforward yet powerful way to handle data storage and retrieval. By understanding how to open, read, write, and close files, you can manage data effectively in your applications. Always remember to handle exceptions and use the `with` statement for cleaner code.
