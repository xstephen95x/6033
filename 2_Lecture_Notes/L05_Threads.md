# Lecture 5 - Threads
### Feb 22, 2017
Threads, Condition Variables, Preemption

-----------------------------------------------

### Last Lecture:
- Bounded buffers
- Race Conditions
- Locks / atomicity

### ----- Threads - Virtualization of the CPU -----
=> Thread -> Virtual processor

Thread API:
- **suspend()** : save state of thread in memory
- **resume()**  : restore state of thread from memory

1. What is a thread's state?
-> values of registers, stack, program_counter, heap, pointer to page table
2. When do we suspend and resume?
-> periodically.

### Using Threads:
state -> { RUNNING, RUNNABLE}

=> **Threads Table**: list of current Threads with [stack pointers (sp), page table registers  (PTR), thread_id, is_running]  
=> **CPUs table**: list of all CPUs + id of the thread currently running     
=> **t_lock**:    

```py
yield():
    acquire(t_lock)
    id = cpus[CPU].thread
    threads[id].state,sp,ptr = RUNNABLE,SP,PTR

    do:
        id = (id +1) mod N
    while threads[id].state != RUNNABLE
    # resume new thread
    release(t_lock)
```

### stuff - seems boring

- wait
- yield_wait
-
