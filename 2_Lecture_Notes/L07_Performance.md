# Lecture 7: Performance
### March 1, 2017

--------------------------


## Enforcing Modularity:
* memory => virtual memory    
* communication => bounded buffers    
* CPU => threads/ virtual processes   
* Most OS's today exist as **Monolithic Kernels**

## Kernel Faults in Monolithic Kernels
- Linus Torvalds says microkernels are just marketing

## Virtual Machine Monitor --> VMM
=> Virtual Machines enforce modularity between multiple OSes running on the same physical machine.

## Get systems to work well:
- `host.txt` was what preceded DNS.

[client] <--(internet)--> [serverCPU][serverDisk]

=> the network is a part of the system too.

### How to Improve Performance in 2 easy steps:
1. **Measure** the system to find the bottleneck
    - Throughput :: #(tasks)/time
    - Latency :: amount of time for a single task
    - Utilization :: %(system resources used)
2. **Relax** the bottleneck
    - Cache data
    - Batch requests
    - Exploit Concurrency
    - Exploit Parallelism
    - Use better/newer algorithms/hardware/software



### Loads and Latency
1. Light Load => low latency + low throughput
2. Moderate Load => low latency + high throughput
3. High Load => high latency + maximized throughput

- Latency is what affects UX  

## Hard Disk Drives
Composed of a cylinder of platters with a number of tracks which circle around each platter, and each track is divided into sectors. Each track has 500-1200 sectors.

For **Read/Write**:
1. Seek to desired track (8-9 ms)
2. Wait for platter to rotate (0-8ms)
3. Do I/O operation (35-62 MB/sec)

##### Improve throughput:
- **Batch** reads/writes together
- Sequential access > random access
- De-frag HDD

##### Caching
Average Access Time:    
=> (time time * hit rate) + (miss time * miss rate)

Caching only works if you:
- Have temporal Locality
- Or have spacial Locality
- Read heavy system (write heavy slows down caching)
