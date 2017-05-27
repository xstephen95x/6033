# L03 : Operating Systems:
### Feb 15, 2017
##### Enforcing Modularity on a single machine.    
NOTE: L02 cancelled due to snow.     
-> Naming is important. Client Server works.     
--------------------------------------

### (P)----- OSs:  Operating Systems ------  
Operating systems handle many issues with modularity:    
+ Multiplexing
+ Isolation
+ Cooperation/Communication
+ Portability
+ Performance

**Operating Systems => Enforcing modularity on a single machine => Using Virtualization**    



```c

/* fork() => forks a child process */

#include	<stdio.h>
#include	<unistd.h>

void (*m)();
void f() {
	printf("child	is	running	m	=	%p\n",	m);
}

int main()	{
	m =	f;
	if	(fork()	==	0)	{
		printf("child	has	started\n");
		int	i;
		for	(i	=	0;	i	<	15;	i++){
			sleep(1);
			(m)();
		}
	} else {
		printf("parent	has	started\n");
		sleep (5);
		printf("parent	is	running; let's write to	m	=	%p\n",	m);
		m = 0;
		printf("parent tries to invoke m = %p\n", m);
		(m)();
		printf("parent	is	still	alive\n");
	}
}
```

**OSs Enforce modularity via virtualization**
- virtualized memory
- virtualized Communication links
- virtualized CPU

------------
## (P) ------ Virtual Memory ------

**TLAs**:
- **EIP** = Extended Instruction Pointer
- **MMU** = Memory Management Unit
- **RAM** = Random Access Memory


What is Memory?
- RAM: Fast, Volatile

[CPU] : interpret instructions   
[RAM] : store instructions , data

[CPU_1] -> [RAM]  <- [CPU_2]  
Multiple, virtual, CPUs access the **same** physical RAM.    

#### Problem
-  memory needs partitions / boundaries. We dont want programs accessing each other's instructions on accident. #modularity   

#### Solution
-> Create virtual address spaces which map to the physical address space.   
-> the **MMU translates: (virtual addr)=>(physical addr)** for each program using a look-up table.   

[CPU_1] -> [MMU] -> [RAM]  

-> Use a **page table** to efficiently handle look-ups from the MMU.  

#### Indexing the Page Table:
Rather than storing a mapping from every physical address => virtual address, Paging is used.    

Given a 32-bit Physical Address:  
- 2^32 virtual addresses can be named (regarless of page table scheme, as there needs to be a bi-jective mapping) 
- 1 Page (typically) = **2^12 bits per page**
- 2^32 - 2^12 = **2^20 Pages.**    
- [0100010011011101 | 00101] => [page #; offset]   
-> first {20} bits = page # ; last {12} = offset  
-> offset is not translated. only page #   

### Translating



Not all pages reside in RAM at all times. (storage is bigger than memory.)

Information Bits:        
- **Dirty Bit - D**      
- **Present Bit - P**: 1 if in DRAM, 0 if in storage.
- **Read Bit - R** : 1 if program can read it, 0 if not
- **Write Bit - W**: 1 if program can write it, 0 if not

#### Improvements
Given the above model, RAM must be allocated on initialization (as it must be contiguous), which quickly uses up all memory.

[2nd outer | 1st outer | inner | offset ]   
To avoid this problem:     
-> use layers of page tables.  
-> Each child table can be allocated as needed. Hierarchy is good for scale.   
-> Potentially many more page faults / slower

#### Processor Execution Modes:
1. User Mode
2. Kernel Mode  

User triggers a page fault?   
-> page fault is a special interrupt   
-> kernel should take over and fetch page, as the kernel handles all page faults and interrupts  

- All system calls are interrupt (handled by kernel)

```c
interrupt(x){
    u_k-bit = k;
    handler = handlers[x];
    call(handler)
    u_k = user;
}
```

Virtualization doesnt work for everything.   
->

**OSs Enforce modularity via virtualization and abstraction**
-> Virtual Memory uses the MMU and Page tables to keep from corrupting memory between programs.

##### Quiz question: translate virtual => physical address

//END
