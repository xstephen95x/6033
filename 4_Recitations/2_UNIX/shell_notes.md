# UNIX Information

### Shell Languages
- TCSH - TC Shell
- bash - bash shell


### Lower-Level Details
- Each Shell script running is, in effect, a *subprocess of the parent shell*
- All commands executed from the shell start with 3 open file descriptors
    - 0: stdin 1: stdout 2: stderr 


### Common UNIX commands

- **cat**    -> concatenate
    - `$ cat foo.txt bar.txt > foobar.txt`

- **fmt**    -> format
    - formats text to standard output
    - `-u` for uniform spacing

- **grep**   -> global regex and print
    - `$ grep OPTIONS pattern FILE`
    - `fgrep` / `grep -F` : Fixed String
    - `egrep` / `grep -E` : extended regex w/ logic
    - `-i` ignore case
    - `-w` whole word match
    - `-o` only matching
    - `-v` to invert regex logic (complement)

- **head**   -> print the head of the file
    - `-n K` print first K lines of file. Default=10
    - `-c K` print first K bytes of file

- **ls**   -> list
    - `-a` : list all + hidden
    - `-lh`: list each file in detail human readable

- **ps**   -> print processes data
    - `-aux` : print all

- **sort**   -> sorts

- **tail**   -> print tail of file

- **top**    -> display processes paginated, interactive

- **wc**     ->     word count for each file in dir  
    - `-m` `-c` `-l` displays chars, bytes, and lines

- **yes**    ->  output a string repeatedly until killed    

-----------------------
### REGEXs
for using grep
- put inside of '  '
- *  -> zero or more
- +  -> one or more
- ?  -> once or none
- {3,} -> 3 or more
- ^  => start of line
- $  => end of line
- '^ [] $' to enforce for a whole line
- ' \<  \>' to enforce for whole words

### Shell layout
- `/etc` contains all configure (text) files

### Shell Wildcards
- `&` or "ampersand"
    - e.g. `~$ sleep 30 &`
    - & makes it run asynchronously
    - "If a command is terminated by the control operator &, the shell executes the command in the background in a subshell".
    - the variable `$!` holds the child PID.


### Links

There are 2 kinds of links:
- **symbolic links** - `ln -s {target} {link name}`
    - creates a text file of the absolute path to use as a virtual link
- **Hard Link** - `ln {target}{link}`
    - creates a file called {link} and points its inode to the same entry.
    - is the same file, mutates both.
