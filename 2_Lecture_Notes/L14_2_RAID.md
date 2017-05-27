# Lecture 14: Reliability via Replication
### Monday April 3, 2017
Day after spring break.

----------------------

### Reliability via Replication.
Many systems mitigate types of failures by replicating data.   

**Reliability** Means:    
- Fault Tolerance
- Fault Recovery
- Redundant

### Fault Tolerance
How to design Fault-tolerance systems in 3 easy steps:     

1. **Identify** all possible failures.
    - Software Failures
    - Hardware Failures
    - Other Failures: magnetic fields, etc.
2. **Detect** and **Contain** the faults.
    - Find faults quickly
    - Limit propagation of fault
    - Check checksums
3. **Handle** the fault.
    - Do Nothing.
    - Fail Fast
    - Fail Stop

### Disappointing Truths

1. Of all things that can fail, we can never guarantee any component to 100% reliability. All reliabilities are probabilities.

2. Reliability always comes at a cost. More reliability usually costs more.

3. Perfect Reliability is impossible, as its impossible all possible failures can be enumerated.

4. Software faults must assume at some low-level that code is absolutely correct. Usually "mission critical" code.

### Quantifying Reliability
System Availability:     
- **MTTF** = Mean Time to Fail
- **MTTR** = Mean Time to Repair
- **MTBF** = Mean time between Failures = MTTF + MTTR
- **Availability** = MTTF / (MTTF + MTTR) = MTTF/MTBF

Averaging Availability:  
- it is more likely that a disk array will fail than a single disk. Thus, its MTTF is smaller than a single disk.


### Disk Failures.    
If a CPU fails, it can be replaced. If a cable fails, it can be replaced. Disks have data which could be lost when it fails, and therefore can be the most costly failures.

To test disks, they can run X disks for 3X hours, to get estimates well into the future.   

Disks are more likely to to fail when  young || old.    
1. "Infant Mortality" =>  P(error) is High
2. "Stable Operating Period" => P(error) is low
3. "Burnout"  => P(error) is High

### RAID - Redundant Array of Independent Disks
RAID -> writing data to multiple places in a system.     

* RAID1 =>
    - basically, just mirrors the disk.
    + Can recover from any single-disk failure
    - requires 2*n disks.
* RAID 2-6
    - all use Striping / Interleaving
* RAID4 => (dedicated parity disk) _1977_
    - Imagine 2 bits [1] [0], given a 3rd bit that is the XOR of the first 2, we can infer a lost bit.
    - Given N disks, a n+1th **parity disk** which holds the xor of the other disks, any disk can be recovered.
    - a **parity disk** XOR's the same number sector on each disk with eachother.
    - The parity disk can also be recovered.
    - Only requires 1 additional disk to do backups.
    - Easily recovers individual sectors, not just whole disk.
    - BUT, every single write has to modify the (itself + parity disk).
        - Every transaction has 2 reads and 2 writes.

* RAID5 => parity spread out
    - Protects against single-disk failure while maintaining good performance.
    - RAID5 is used today.
    - n+1 Disks needed to cover single disk failure.
    - Individual sectors are assigned parity sectors, distributed on many disks so that 1 disk doesn't have to handle every single write.
    - minimum of 3 disks (D1 xor D2 = Parity)

* RAID6
    - RAID6 is also used today
    - Has different error correction algorithm.

--------------------------------------------------------------------------------
--------------------------------------------------------------------------------

6.033: Fault Tolerance: Reliability via Replication
Lecture 14
Katrina LaCurts, lacurts@mit.edu
0. Introduction
    - Done with OSes, networking
    - Now: how to systematically deal with failures, or build "fault-tolerant" systems
    - We'll allow more complicated failures and also try to recover from failures
    - Thinking about large, distributed systems. 100s, 1000s, even more machines, potentially logated across the globe.
    - Will also have to think about what these applications are doing, what they need
1. Building fault-tolerant systems
    - General approach:
        1. Indentify possible faults (software, hardware, design, operation, environment, ...)
        2. Detect and contain
        3. Handle the fault
    - do nothing, fail-fast (detect and report to next  higher-level), fail-stop (detect and stop), mask, ...
    - Caveats
        - Components are always unreliable. We aim to build a reliable system out of them, but our guarantees will be probabilistic
        - Reliability comes at a cost; always a tradeoff. Common tradeoff is reliability vs. simplicity.
        -  All of this is tricky. It's easy to miss some possible faults in step 1, e.g. Hence, we iterate.
        - We'll have to rely on *some* code to work correctly. In practice, there is only a small portion of mission-critical code. We have stringent development processes for those components.
2. Quantifying reliability
 - Goal: increase availability
 - Metrics:
 MTTF = mean time to failure
 MTTR = mean time to repair
 MTBF = mean time between failures (MTTF + MTTR)
 availability = MTTF / MTBF
 - Example: Suppose my OS crashes once every month, and takes 10
 minutes to recover.
 MTTF = 30 days = 720 hours = 43,200 minutes
 MTTR = 10 minutes
 MTBF = 43,210 minutes
 availability = 43,200 / 43,210 = .9997
 => two hours of downtime per year
3. Reliability via Replication
 - To improve reliability, add redundancy
 - One way to add redundancy: replication
 - Today: replication within a single machine to deal with disk
 failures
 - Tomorrow in recitation: replication across machines to deal
 with machine failures.
4. Dealing with disk failures
 - Why disks?
 - Starting from single machine because we want to improve
 reliability there first before we move to multiple machines
 - Disks in particular because if disk fails, your data is gone.
 Can replace other components like CPU easily. Cost of disk
 failure is high.
 - Are disk failures frequent?
 - Manufactures claim MTBF is 700K+ hours, which is bogus.
 - Likely: Ran 1000 disks for 3000 hours (125 days) => 3 million
 hours total, had 4 failures, and concluded: 1 failure every
 750,000 hours.
 - But failures aren't memoryless: disk is more likely to fail at
 beginning of its lifespan and the end than in the middle (see
 slides)
5. Whole-disk failures
 - General scenario: entire disk fails, all data on that disk is
 lost. What to do? RAID provides a suite of techniques.
 - RAID 1: Mirror data across 2 disks.
 - Pro: Can handle single-disk failures
 - Pro: Performance improvement on reads (issue two in parallel),
 not a terrible performance hit on writes (have to issue two
 writes, but you can issue them in parallel too)
 - Con: To mirror N disks' worth of data, you need 2N disks
 - RAID 4: With N disks, add an additional parity disk. Sector i on
 the parity disk is the XOR of all of the sector i's from the data
 disk.
 - Pro: Can handle single-disk failures (if one disk fails, xor
 the other disks to recover its data)
 - Can use same technique to recover from single-sector errors
 - Pro: To store N disks' worth of data we only need N+1 disks
 - Pro: Improved performance if you stripe files across the
 array. E.g., an N-sector-length file can be stored as one
sector
 per disk. Reading the whole file means N parallel 1-sector
reads
 instead of 1 long N-sector read.
 - RAID is a system for reliability, but we never forget about
 performance, and in fact performance influenced much of the
 design of RAID.
 - Con: Every write hits the parity disk.
 - RAID 5: Same as RAID 4, except intersperse the parity sectors
 amongst all N+1 disks to load balance writes. (see slide for
 diagram)
 - You need a way to figure out which disk holds the parity sector
 for sector i, but it's not hard.
 - RAID 5 used in practice, but falling out in favor of RAID 6,
 which uses the same techniques but provides protection against
 two disks failing at the same time.
6. Your future
 - RAID, and even replication, don't solve everything.
 - E.g., what about failures that aren't independent?
 - Wednesday: we'll introduce transactions, which let us make some
 abstractions to reason about faults
 - Next-week: we'll get transaction-based systems to perform well on
 a single machine.
 - Week after: we'll get everything to work across machines.
