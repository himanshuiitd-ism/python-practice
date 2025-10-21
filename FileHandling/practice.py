# f = open('myFile.txt','r')
# i=0
# while f:
#   i=i+1
#   line = f.readline()
#   if not line:
#     break
#   m1 = line.split(",")[0]
#   m2 = line.split(",")[1]
#   m3 = line.split(",")[2]
#   print(f"Marks of student {i} in Math is: ",m1)
#   print(f"Marks of student {i} in English is: ",m2)
#   print(f"Marks of student {i} in SST is: ",m3)
#   print(line)

f= open('myfile2.txt','a')
lines = ['line','line2','line3']
for line in lines:
  f.write(line + '\n')
f.close()

# Here’s a comprehensive list of Python’s built-in **file handling functions and methods**, along with their **names** and **uses**. These are essential for reading, writing, and managing files efficiently.

# ---

# ## 📂 Core File Handling Functions

# ### 🔹 `open()`
# - **Use**: Opens a file and returns a file object.
# - **Syntax**: `open('filename', 'mode')`
# - **Modes**:
#   - `'r'`: Read (default)
#   - `'w'`: Write (overwrites)
#   - `'a'`: Append
#   - `'b'`: Binary
#   - `'x'`: Create
#   - `'r+'`: Read and write

# ### 🔹 `close()`
# - **Use**: Closes the file and frees system resources.

# ---

# ## 📄 Reading Methods

# | Method         | Use                                                                 |
# |----------------|----------------------------------------------------------------------|
# | `read()`       | Reads entire file content as a string.                              |
# | `readline()`   | Reads a single line from the file.                                  |
# | `readlines()`  | Reads all lines and returns them as a list.                         |
# | `seek()`       | Moves the file pointer to a specific position.                      |
# | `tell()`       | Returns the current position of the file pointer.                   |

# ---

# ## ✍️ Writing Methods

# | Method         | Use                                                                 |
# |----------------|----------------------------------------------------------------------|
# | `write()`      | Writes a string to the file.                                        |
# | `writelines()` | Writes a list of strings to the file.                               |
# | `truncate()`   | Resizes the file to a specified size.                               |

# ---

# ## 🔍 File Property & Utility Methods

# | Method         | Use                                                                 |
# |----------------|----------------------------------------------------------------------|
# | `flush()`      | Flushes the internal buffer.                                        |
# | `fileno()`     | Returns the file descriptor (OS-level).                             |
# | `isatty()`     | Checks if the file is connected to a terminal device.              |
# | `name`         | Returns the name of the file.                                       |
# | `mode`         | Returns the mode in which the file was opened.                      |
# | `closed`       | Returns `True` if the file is closed.                               |

# ---

# ## ✅ File Capability Check Methods

# | Method         | Use                                                                 |
# |----------------|----------------------------------------------------------------------|
# | `readable()`   | Checks if the file can be read.                                     |
# | `writable()`   | Checks if the file can be written to.                               |
# | `seekable()`   | Checks if the file supports random access.                          |

# ---

# ## 🧠 Best Practice Tip

# Use the `with` statement for automatic file closing:

# ```python
# with open('data.txt', 'r') as file:
#     content = file.read()
# # File is automatically closed here
# ```

# ---

# Want a visual cheat sheet or a quick-use reference for these? I can whip one up for you. Or if you're working on a specific file task—like parsing logs or writing structured data—I can help you optimize it.