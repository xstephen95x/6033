# Tutorial #X Evaluation of DP
### Apr 21, 2017

--------------------------------------------------------------------------------

### Things you can calculate with numbers:
- Radio Bandwidth
    - are you exceeding the max radio bandwidth
- Disk storage  
    - servers /dbs
    - bus control       

- Radio (latency):
    - How long does it take a bus to _get_ a frequency on the network?
        - # of possible frequencies, # of busses trying to communicate to the server

### Things you can estimate

- Recovery:
    - How long does it take a bus to respond to a failure?

- Network Latency:
    - how much time does it take for data from the busses to reach the servers?
        - can you quickly respond to a failure?
        - are you encrypting/decrypting?

- Accuracy:
    - are your methods for counting passengers (mix of lasers and images) accurate?

- Bus => Failed route (Eval. Failure Recovery Algorithm)
    - speed
    - traffic
    - distance
    - O(recovery time) , consider radius of boston, average traffic, etc.
- MBTA Targets
    - Reliability: Hard to prove that we will meet standards

- Evaluate algorithms/server configuration.

### Hard to calculate
- Traffic: whats the average traffic in boston?


### Evaluate Scale:
- Bandwidth of radio network

- Bottlenecks:  
    - number of busses during failure
- number of radio requests the server can receive in an epoch


- Failure Recovery: switching people to different routes


### Evaluation of our System:
- Evaluate the network
    - How many packets would the busses need to send for normal operations?
    - whats the O() with most busses full (sending security images) and all busses deployed?
- Evaluate How well the system recovers
