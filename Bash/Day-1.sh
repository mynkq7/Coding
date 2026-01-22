# Bash Commands
ls # List directory contents
# Options for ls command
ls -l # Long listing format
ls -a # Show all files including hidden files
ls -h # Human-readable file sizes
ls -R  # Recursive listing of subdirectories
ls -t # Short by modification time 

cd # Change directory
# Options for cd command
cd .. # Move up one directory
cd ~ # Move to home directory
cd - # Move to previous directory
cd / # Move to root directory

Pwd #  Display current directory

echo # Print text in terminal

cat # View file content
# Options for cat  command
cat -n # Add line numbers to output
cat -b # Add line numbers to text only ignoring blank lines
cat -s # Remove extra blank lines
cat file.txt  file.txt-2   > Download.txt # Concatenate files and save to new file
cat file.txt | grep  "SearchTerm" # Search for a term in file.txt

cp # Copy files and directories
# Options for cp command
cp -r # Copy all files and directories recursively 
cp -i # Prompt before overwrite
cp -v # Verbose mode, show files being copied

mv # Move files and directories
mv -i # Prompt before overwrite
mv csrf.txt rename.txt  # Rename a file
mv -v rename.txt changed.txt # Move with verbose output 

rm # Remove files and directories
# Options for rm command
rm -r # Remove directories and their inside files or contents 
rm -f # Force remove files without prompt
rn -i # Prompt before every removal

touch # Create an empty file

mkdir # Create a new directory 
# Options for mkdir command
mkdir -p # Create a parent directory along with the subdirectory
mkdir -v # Verbose mode, show directories being created
mkdir -m 755 # Set permissions while creating a directory 

rmdir # Remove directory

man # Display user manual 

