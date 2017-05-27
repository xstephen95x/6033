# Rec 7 : MapReduce
> March 2 2017
> Asian Lady who didn't say her name

## Hands-On notes:
- Python's multiprocessing lib: `from multiprocessing import Pool`
    - https://docs.python.org/2/library/multiprocessing.html
    - Pool acts as a pool of worker threads.
## Background
- This paper was published in 2004, pretty new development.
- Unveiled at prestigious Usenix Symposium, and ACM Symposium on OSs (SOSP)
- Usenix Association: Advanced Computing Systems Association -
- Authors Jeff Dean and Sanjay Ghemawat
- Important for modern *Internet Scale Computing*


### MapReduce
**About**: the Map Reduce approach
- Abstracts away parallelization
- Provides robust way to handle failure

### Model
- Highly parallelized system which takes a map and reduce function
- Is a functional approach.
- It is not domain specific. It is good at search, not at sort.

### Use Cases
- Word Count
- Grep
- frequency count / aggregation
- Reverse web-link graph
- Inverted Index
- Distributed Sort

### Bad Cases
- Any computation with side effects
- Any computation that mutates data, writes to a DB,

### Implementation
- Magic of MapReduce is in the job sorting/partitioning after map, before reduce
1. Partition into Jobs
2. Specify Master and Worker machines
3. Workers work on Map jobs
4. Mapped data is stored to disk
5. Reduce workers sort all data
6. Reduce workers reduce each unique key
7. When all jobs are complete, master resumes and returns final answer

- Reduce uses RPCs (remote procedure calls)

### Fault Tolerance
##### Master failure
Master failure is bad. Checkpoints can be saved, so computation can be resumed from points other than the begining, but if they master fails the computation must exit.

##### Child Failure
The master periodically pings each worker, with an expected response time. If the master doesn't hear back in time, all of that machine's tasks are reset and reassigned to a new worker.   

### Performance Issues
- Straggler machines
    - Can assign 'back up' machines, and if one machine finishes all assigned tasks, it can begin on back-up tasks if another machine is slower

## ------ Reading Questions ---------

1. **What are the performance goals of MapReduce (both the programming model + its implementation)?**
One of the key goals of the MapReduce model is that it can be a highly distributed and parallel computation. This goal of making the computation work on hundreds to thousands of machines simultaneously is enforced for the bigger goal of speed and performing quickly on very large datasets, while using lower amounts of memory. It follows from nature of being a highly-parallel computation, that strong fault tolerance must also be a goal.

2. **How was MapReduce implemented at Google to meet those goals?**
The MapReduce implementation at Google was designed to use one of their large distributed, high performance computer networks. On top of the simple functional discipline of using a map() function, intermediate storage, and reduce() function, they detail how their network of computers acts. Specifically, that there is a master computer which assigns tasks to worker machines. The way in which the system hashes and partitions the tasks is also crucial to its parallelizability <-(not sure if word). Additionally, they implemented the system such that if any one machine fails, they simply re-assign all tasks that were ran /were to be run on that machine to one of the other numerous machines.

3. **Why was MapReduce implemented in this way?**
The functional style of MapReduce lowers the amount of memory/state that needs to be kept. Additionally, the highly distributed approach allowed for substantial speed-up without the usually error-prone issues which arrive in threaded or highly-parallel computations, due to the simple task-reassigning system.
