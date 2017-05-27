# L01 : Administrivia

## General Systems.
What is a system?    
=> A group of interconnected components w/ expected behavior, observed with an interface.    
=> Internet is a __huge__ system.

- Systems are __constrained__ by __complexity__.
    - complexity brings:: Size, costs, slower performance, bugs.
    1. Emergent Properties
    2. Incompensataible Scaling
    3. Propagation of effects

- opposite(complexity) = Simplicity, scalability, reliability, performant, secure.

### Mitigating Complexity: Enforcing Design Principles
- **Modularity** => Layers, hierarchy, independence, invariance
- **Abstraction** => OOP, non-leaky abstractions,

### Enforcing Modularity
The theme of 6.033!    
- Client/Server model  (RPC: Remote Procedure Calls)
- Stub Clients   

=> Response/Request Model:     
    - uses UIDs to prevent unknown duplicates.
