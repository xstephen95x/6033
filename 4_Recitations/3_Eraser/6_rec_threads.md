# Recitation 6: Eraser
> Tues Feb 28 2017
> Karen Sullen (martin is away)

-----------------------------

Fun facts:
- Valgrind was the gate to valhalla.
- AltaVista was the first major web search engine
- Before search engines, there were just directory files (quickly got out of hand)
- Person who makes the IT system on the T actually took 6.033

### Discussion on Valgrind
- Prior to Valgrind, they did many static checks like "happens before" logic.
- Valgrind does dynamic checks at runtime, but makes runtime slower, and can make behavior slightly different. (30x as slow)
- Valgrind edits the binary (risky). In a perfect world, you should never edit the executable code with the test suite. Must be very certain that it wont mutate any code.
- False positives kept arising
    - Reads dont need mutual exclusion
    - Eraser watches words in memory not actual vars in the programming language. Doesn't always know if memory is re-allocated.
    - If 1 thread only accesses it, its not a race condition
- Violates abstraction, looks into binary code and locks and such.
- It assumes using pthread class. Can't use your own.
- Published in ACM (Assoc. of Computer Machinery)


### Thread vs Process:
- Processes dont share memory!
    - If one process fails, all don't fail.
- Threads within the same process use same memory space.
    - This means there is less context switching which is faster
    - But, this also decreases modularity and separation

### Locks
- Some mode needs to be mutually exclusive during execution. Ie, needs to be atomic
- Specifically, its a binary semaphore. (only thread that locks a lock can unlock it)

### Eraser:
Eraser is powered by the **Lockset Algorithm**
- The Lockset algorithm's set can only decrease in size, as it iteratively takes the intersection.

NOTE: **ERASER issues no guarantees about results.**

Virgin -(read/write)--> Exclusive --()--> Shared


## ------ Reading Questions -------

--------------
1. **What are the goals of Eraser?**   
The main goal of Eraser is to create a create a test suite for debugging multi-threaded code which uses locks for its concurrency policy. Concurrent code is very error-prone due to its nondeterminism. Eraser provides software for dynamically detecting race conditions in lock-based multi-threaded programs.


2. **How was it designed to meet those goals?**   
Unlike its predecessors, Eraser uses monitoring techniques to watch every shared memory reference dynamically as the program executes, and makes sure that consistent locking is occurring on each variable. Prior software was only able to do so statically, or using a *happens-prior* method, which have significant drawbacks. Ultimately, Eraser was implemented with the *Lockset* algorithm with a few optimizations around read-only data and initialization.


3. **Why do we need a tool like Eraser? (Or why do the authors believe that we need such a tool?)**    
Perhaps the most convincing argument for needing Eraser was when it detected race conditions in undergraduate's homework. Programming asynchronously or programming to enforce synchronization is error prone and extremely non-intuitive. Just as simple unit tests that check that synchronous code obeys the spec, tools like Eraser are needed to check race conditions. Simple unit tests are inadequate in concurrent programming due to nondeterminism.
