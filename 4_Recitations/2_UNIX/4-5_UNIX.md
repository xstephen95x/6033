## Recitation 3: UNIX File System
> Feb 16 2017; Martin Rinard.    
----------------------------

### ----- Paper Background -----

- Paper was written: 1974
- Dominant computing platform in 1974: IBM
- Key problem UNIX solved: Persistent, consistent file system.

UNIX File System present an abstraction: Read and write disk blocks (512 byte)  
Before UNIX, there were many different file APIs for different programs. Many
had different encodings, and were not cross-compatible.     
UNIX provided a single file abstraction: a file of bytes.

### File system :

**Types of Files**:
- _Directory_
- _File_
- _Special File_

Mounting:
Calling mount makes replaces a leaf in the FS DAG with a link to the root of the new drive, and appends the entire subtree.
About:      
- The filesystem abstraction is a DAG  
- file points to directory, which holds file info (i_number,)  
- i_number indexes into a table, and returns the disk block number the file starts at   
- You can nest index tables. Allocating an index table means you dont have to know the size of the file, just allocate a starting point.    
    - You can use doubly and triply indirect lookups.

Interface:
- `fd = open(fn,f1)`
- `n = read(fd,buffer,n)` //fd = file descriptor
- `n = write(fd,buffer,n)`
- `loc = lseek(fd,offset,base)`
- A _File Descriptor_ is a small integer used to identify the file in subsequent calls mutate the file.

If save the same file in 2 places,     
user/a/foo.txt -> both point to same file in storage.    
user/b/bar.txt ->     
=> If you delete both, the file is no longer reachable.     
=> **Computer security attacks go past abstractions.**    
=> "Repetition is the soul of pedagogy"

Pipes:   

-------------------------------
> Feb 23   UNIX 2


modularity => not sharing

The introduction of general purpose computing is inefficient
-> computation specific hardware

(1computer1program) -> Batch multiprocessing -> timesharing

- fork()
- exec() command

- process time sharing is not equal
- processes communicate via pipes
- In UNIX the fs code and networking code execute in the same address space. They never used microkernels.

UNIX = Monolithic kernel
other = microkernels

#### UNIX Interface
- `fork()` - the command to create a new process (so you now have a "parent" and "child" process). They do not have any shared memory, but do share all open files. You can pass information between parent and child with a pipe (pipe()), and this must be set up by a common ancestor of both parent and child processes. They can work on things in parallel, or you could have the parent wait() for the child to complete execution before resuming the parent process.   



#### QUIZ:
longest file i can have if i only have 10 direct pointers.   
=> 10x the block size
=>

UNIX File System:
- Ordinary Files
- Special Files
- Directories
