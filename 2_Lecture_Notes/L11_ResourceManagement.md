# Lecture 11: Resource Mgmt
### Wed March 15, 2017

## Class Notes
TCP Congestion Control

Dropped packets ==> Congestion => Delay Increase
- TCP Reacts to drops, and packets aren't dropped until queues are full.
- Traffic on the internet is inherently 'bursty'
    - Queues / buffers absorb these bursts
- We want _transient_ queues.
    - hard in practice.
- Instead, we want to make queues smarter.

### Queue Management (from a Switch)
1. droptail.
    - Packets come in
        - IF space in queue, packets are put in the queue
        - ELSE: packet is dropped from the queue.
    - Bad for latency sensitive things like voice calls
    - High delays and synchronizes flows.
    - Super simple
2. RED - Random Early Detection
    - drop packets before the queue is full.
    - drops based on average queue size,
    - Prevents queue from oscillating, by using averages
    - But, drops more packets
3. ECN - Explicit Detection Notification
    - Very similar to RED, but *marks* packets rather than drops them.
    - Complex and hard to pick parameters     

==> Can we have **latency guarantees**?
- How about **two queues**
- Have a normal queue, and **priority queue**.
- what if we want to allocate bandwidth to different types of traffic?


### Delay Based Scheduling
1. Priority Queuing
    - Put latency sensitive traffic in its own queue and serve that queue first.

### Bandwidth Based Scheduling
NOTE: Packets are not all the same size.
1. Round Robin  
    - Send a packet from each queue, iteratively.
2. Weighted Round-robin   
    - Iteratively send packets from each queue, but not all in 1:1:1 ratio. Some send multiple per turn, some less.
3. Deficit Round-robin
    - keep track of bytes sent

```python
# Weighted Round Robin
while (rounds):
    for q in queues:
        q.norm = q.weight/q.mean_packet_size

    min = min([x for x.norm in queues])
```
```python
# Deficit Round Robin
while (rounds):
    for q in queues:
        q.credit += q.quantum
        while q.credit >= size(next packet p):
            q.credit -= size(p)
            send(p)
```

### Recap:
These are _orthogonal_ (do not overlap) approaches to TCP.
Method of in-network management
1. Queue Management
2. Delay-based scheduling
3. Bandwidth-based scheduling

Is in-network resource Management a good idea?

#### Net Neutrality
- Should Comcast be able to pay ISPs to have its traffic prioritized over its competitor like Netflix?
