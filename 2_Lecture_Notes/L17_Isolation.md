# Lecture 17: Isolation
### Apr 12, 2017
Conflict Serializability and two phase locking.

--------------------------------------------------------------------------------

## --- Isolation ----
GOAL: Reliable systems from unreliable parts.    
Transactions provide atomicity and isolation, while not hindering performance.

**Atomicity** => shadow copies, **logs**,
**Isolation** => _today_: Two Phase Locking

#### --- New Stuff ---
- Run x transactions concurrently, and have it "appear" as if they appear sequentially.

- Naive approach: Actually run them sequentially via a single global lock.
    - "appear to have run sequentially"
    - very poor performance

- Fine-grained Locking  
    - opens up many bugs

### Serializable
- Definition of serializable/sequential varies depending on task and context
    - just final written state is the same
    - all intermediate states and final state are the same
- Final-state serializable: final states of all serializable schedules are the same

### Conflict Serializability
- 2 operations conflict if :
    1. they both operation on the same object
    2. at least one of them is a write  
- Many concurrent reads are fine.

- A schedule is **conflict serializable** if the order of all of its conflicts is the same as the order of the conflicts in some sequential schedule.   

### Conflict Graphs
- Nodes are transactions
- edges are directed

1. Draw the conflict Graph
    - Two operations conflict if they operate on the same object and
    - An edge from Ti to Tj IFF Ti and Tj have a conflict between them and the first step in the conflict occurs in Ti.
2. Check if it has cycles.
    - Acyclic conflict graph <=> conflict-serializable

##### Example

T1: read(x); T2: write(x)
 T3: read(y); T1: write(y)
 T3: read(y); T2: write(y)
 T4: read(y); T1: write(y)
 T4: read(y); T2: write(y)
 T1: write(y); T2: write(y)

         |----------<--
         v            |
 T1 --> T2 <-- T3    T4
 ^^            |      |
 ||------<-----|      |
 |                    |
 |----------<---------|

### Two-phase Locking (2Pl)
Generating Conflict-serializable Schedules:
1. Each shared variable has a lock. (Fine-grained locking)
2. Before **any** operation on a variable, the transaction must acquire the corresponding lock
3. after a transaction releases a lock, it **may not** acquire any other locks.
    - In strict 2PL locks are held until after the transaction commits

Phases     
- Acquire phase
- Release phase

Problem: 2Pl can cause deadlocks:
- take advantage of atomicity and abort one of the transactions.
    - use 'wait-dependency graphs'  which capture the locks each  transaction has and the ones it wants. Cycle in  wait-dependency graph => deadlock
    - Just tell locks to wait (x) seconds before aborting


### Improving Performance:
- Reader-writer Locks
    - separate reader and writer locks
        - Can acquire a reader lock at the same time as other readers.
        - Can acquire a writer lock only if there are no other readers or writers.
    - What about fairness? If readers keep acquiring the lock, and a writer is waiting?
        - Typically: if writer is waiting, new readers wait too.
    - Reader-writer locks improve performance
    - As described, they allow for concurrent reads.
    - We can also release read locks prior to commit
        - Why? Once a transaction T has acquired all its locks (reached its "lock point") any conflict transaction will run later
        - If T reaches its lock point and will no longer access X, releasing read locks on X will be fine
        - Hold write locks until commit, though, in case the transaction aborts.

- Can also improve performance by relaxing our requirements for serializability/isolation.
    - Read-committed or snapshot isolation (see hands-on)
    - Important: there are a ton of tradeoffs between performance and isolation semantics.
    -  view serializable vs conflict serializable
        - Informally: a schedule is view serializable if the final written state as well as intermediate reads are the same as in some serial schedule.
        - view-serializability is NP-hard to check. much harder than conflict

--------------------------------------------------------------------------------

Proof that 2PL produces a conflict-serializable schedule
- (i) Suppose not. Suppose the conflict graph produced by an execution of 2PL has a cycle, which without loss of generality, is T1 --> T2 --> ... --> Tk --> T1.
- (ii) We'll show that a locking protocol that produces such a schedule must violate 2PL.
- (iii) Let the shared variable -- the one that causes the conflict -- between T_i and T_{i+1} be represented by x_i.     
 T1 and T2 conflict on x1     
 T2 and T3 conflict on x2     
 ...    
 Tk and T1 conflict on x_k    
- (iv) This means that:    
 T1 acquires x1.lock    
 T2 acquires x1.lock and x2.lock   
 T3 acquires x2.lock and x3.lock    
 ...    
 Tk acquires x_k.lock and x_{k-1}.lock     
 T1 acquires x_k.lock     
- (v) Time flows down in the above step. Since the edges go from T_i  to T_{i+1}, T_i must have accessed x_i before T_{i+1}.    
- (vi) For T2 to have acquired its locks -- in particular, x1.lock --
 T1 must have previously released x1.lock. Thus:   
 T1 acquires x1.lock    
 T1 releases x1.lock   
 T2 acquires x1.lock and x2.lock   
 T3 acquires x2.lock and x3.lock    
 ...    
 Tk acquires x_k.lock and x_{k-1}.lock    
 T1 acquires x_k.lock    
- (vii) Focusing just on the steps that involve T1:
 T1 acquires x1.lock   
 T1 releases x1.lock   
 T1 acquires x_k.lock    
- (viii) T1 violates 2PL; it acquires a lock after releasing a lock
- (ix) Therefore, cyclic conflict graph => 2PL was violated.
 Alternatively, 2PL => acyclic conflict graph
