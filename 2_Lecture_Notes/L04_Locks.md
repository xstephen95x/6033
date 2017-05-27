# Lecture 4 - locks
### Feb 21, 2017
Bounded buffers, locks, concurrency
----------------------------

### (P) Virtualization
Memory => virtual memory     
communication  => bounded buffer     
(Assume) 1 program per CPU

##### Bounded buffers
Bounded buffers are very simple data structures.
- Store up to N messages
- send(m)
-  m <- receive()

NOTE: concurrency is bad. Can't assume anything.

Concerns:
- When is it okay to write?
- When is it okay to read?
- Where to read/write?

##### Examples

buffer = {
    N = 5   
    in = total # of messages written   
    out= total # of messages read    
}
=> write:  in-out < N
=> read :  N > out

This configuration has race conditions.

##### Race Conditions
-> Depend on timing.
Race conditions can execute correctly or incorrectly at random.
To fix race conditions, you need to use **locks**

### ----- Locks ------

Lock: only allows 1 CPU to use a segment of code at 1 time.
API:
- acquire(lock) :
- release(lock) :

##### Deadlocks
When using locks, code can be structured so that code which releases a lock, is locked, and the code can never be unlocked. This is known as a 'deadlock'.

Locks can be implemented as semaphores.

##### Atomic Actions
Code atomicity is the notion that a segment of code must be ran as a single unit of code (an atom) that cannot be interrupted.

Many OS operations need to be atomic. Even simple 2-line actions such as moving a directory link need to be atomic.
