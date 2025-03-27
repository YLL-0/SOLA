# Shell Commands and Basics for Linux/Unix

## What is a Shell Command?
- A **shell command** is a text-based instruction given to the shell to perform a specific task.
- Commands are entered at the shell prompt (e.g., `$` or `username@hostname>`).
- Shell commands can:
  - Run programs.
  - Manipulate files and directories.
  - Control processes.
  - Configure the system.

## Basic Shell Commands
Here are some commonly used shell commands:

### File and Directory Management
- `ls`: List files and directories.
  ```bash
  ls -l   # Detailed listing of files
  ls -a   # Show hidden files
  ```
- `cd`: Change directory.
  ```bash
  cd /home/yllo   # Navigate to /home/yllo
  cd ..           # Move up one directory
  ```
- `pwd`: Print the current working directory.
  ```bash
  pwd
  ```
- `mkdir`: Create a new directory.
  ```bash
  mkdir my_folder
  ```
- `rm`: Remove files or directories.
  ```bash
  rm file.txt       # Remove a file
  rm -r my_folder   # Remove a directory and its contents
  ```

### File Viewing and Editing
- `cat`: Display the contents of a file.
  ```bash
  cat file.txt
  ```
- `more`/`less`: View file contents one screen at a time.
  ```bash
  less file.txt
  ```
- `nano`/`vim`: Edit files in the terminal.
  ```bash
  nano file.txt
  ```

### Searching and Filtering
- `grep`: Search for text in files.
  ```bash
  grep "search_term" file.txt
  ```
- `find`: Search for files and directories.
  ```bash
  find /home -name "*.txt"
  ```

### Process Management
- `ps`: Display running processes.
  ```bash
  ps aux
  ```
- `kill`: Terminate a process.
  ```bash
  kill <PID>   # Replace <PID> with the process ID
  ```

### System Information
- `whoami`: Display the current user.
  ```bash
  whoami
  ```
- `uname`: Display system information.
  ```bash
  uname -a
  ```

## Exercises
Try these exercises to practice shell commands:

1. **File and Directory Management**:
   - Create a directory named `practice`.
   - Inside `practice`, create three files: `file1.txt`, `file2.txt`, and `file3.txt`.
   - List all files in the `practice` directory, including hidden files.
   - Delete `file3.txt` and rename `file1.txt` to `renamed_file.txt`.

2. **File Viewing and Searching**:
   - Create a file named `example.txt` with the following content:
     ```
     Hello World
     Shell commands are powerful.
     Practice makes perfect.
     ```
   - Use `cat` to display the file's content.
   - Search for the word "powerful" in `example.txt` using `grep`.

3. **Process Management**:
   - Run the `top` command to monitor system processes.
   - Find the process ID (PID) of a running program using `ps`.
   - Terminate a process using its PID.

4. **System Information**:
   - Find out your current username using `whoami`.
   - Display detailed system information using `uname`.

5. **Advanced**:
   - Use `find` to locate all `.txt` files in your home directory.
   - Create an alias for `ls -la` named `ll` in your shell.

## Additional Resources
- Use `man <command>` to access the manual for any command.
- Explore online tutorials for Linux/Unix shell basics.
