# Lecture 6: Kernels and VMs
### Feb 27, 2017

----------------------

## ----- Monolithic vs Microkernels -----

### Monolithic Kernels
- Monolithic Kernels have no hard enforced modularity.
- Use soft modularity like OOP, locks, etc.
    - forces engineers to write better code
    - causes bugs
- Single bug can crash whole kernel.

Linux Kernels are basically just 1 large C program   

### Microkernels
=> Hard enforced modularity.    
=> Single bug only takes out single microkernel.


#### If they're so great, why is Linux Monolithic?
(not good nor bad reasons)
- Communication costs: have separate modules means they have to communicate, a lot. (they use IPC - interprocess communication)
- Crashes are still bad.
    - If the filesystem microkernel crashes, does it matter if your applications microkernel works?
- Dependencies
- Redesign takes a lot of work.
- Makes iteration difficult.

### Designing with a Monolithic Kernel  
How do we deal with bugs in the linux kernel without redesigning Linux from scratch?   **Virtualization!**   
- Just like virtual machines (VMs), you can virtualize parts of the OS.   
- A VM has a host machine and guest machine.
- VMs cant run in kernel mode (non modular)
- VMs communicate to the Virtual Machine Monitor (VMM)

##### The Virual Machine Monitor (VMM):
- Deals with priviledged instructions
- Allocates resources
- Dispatches events
- the VMM runs in kernel mode.

1. Guest OS in user mode
2. Privileged instructions throw exceptions
3. VMM will *trap* them and *emulate* them.

##### Virtualizing Hardware: one layer further   
[===GuestOS====]  (loads PTR (page table register))    
[Virtual Hardware] (Uses GuestOS page table )   
[=====VMM==== ]   (combines GuestOS PT and VMM PT => host page table)  
[=Phys. Hardware] (Uses the Host Page Table)

* In modern hardware the physical hardware is aware of both page tables and performs the translation from guest virtual to host physical itself
* VMMs are not targeted at Monolithic kernels. They are just a possible solution.


1. Kernel Mode
2. User Mode
3. VMM Mode


VMMs and Microkernels are solving orthogonal problems
