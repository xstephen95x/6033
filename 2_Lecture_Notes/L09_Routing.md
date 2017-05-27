# Lecture 9: Routing
> Wed Mar 8, 2017.    
> Katrina LaCurts

### The Internet of Problems
- Routing Scalability
- Transport
- Adoption of new application

## Routing
Routing on the internet happens through **BGP** and uses AS Advertisements.
- Routing is based on __Protocols__

Naive:
- Allow every switch in the network to know a minimum cost route to every other switch in network.

BUT:
- Networks are not static
- nodes/machines fail
- cables get cut
- weather is unpredictable
- cost between links is dynamic

## Distributed Routing
- Centralized routing can not scale.

1. Nodes learn about their neighbors via "HELLO" protocols. (they ping their neighbors iteratively)
2. Nodes learn about other nodes via Advertisements
    - Adverts change to make error handling easier
    - Failures are reflected in the topology
3. Nodes determine minimum cost routes to other nodes that theyve learned about. (Dijkstra)

## Important Internet Layers:
1. __Application Layer__:
    - BGP, TLS, SSL, HTTP, IMAP, FTP, SSH,
2. __Transport Layer__
    - TCP: TransmissionControlProtocol
    - UDP: UserDatagramProtocol
        - provides a best-effort datagram
3. __Internet Layer__:
    - IP
4. __Link Layer__:
    - Ethernet

## Specific Protocols:
=> **Link State Routing**  
- Uses flooding of Advertisements
- Has a high overhead (flooding)
- Has a low convergence time (good)


=> **Distance Vector Routing**
- uses only neighbors
- nodes cannot infer topology
- Low overhead (only looks at neighbors)
- high convergence time

=> **Path Vector Routing**
1. Advertisements include the whole path, to better detect loops
2. Hierarchy of Routing: Route between ASes or within ASes
    - **AS** = Autonomous System
    - AS3 = MIT , out of AS35000 groups
    - [List](http://www.bgplookingglass.com/list-of-autonomous-system-numbers)
3. Topological Addressing: assign addresses in continuous blocks to make advertising easier.

Problems:
- ASes also need means to implement __Policy__
- ASes dont send traffic through a path without financial incentive (greedy routing)
    - Packet filtering is very expensive.
    - Many paths may exist but an AS may not advertise all routes that it knows.
    - ASes **hide** topology from eachother

AS Relationships:
- Customer/Provider (Transit)
    - Export Policy:
        - Tell your customers about all links
        - Tell links only about customers
    - Import Policy:
        - Customer > Peer > Provider
- Peers (P2P)
    - Peers all free mutual access to each others _customers_, and only when it saves money.

## Internet Service Providers (ISPs)
**Everyone on the internet is a customer of someone**   
ISPs come in tiers.
1. Tier I -->
    - Only about 10-15 of these
    - they are all mutual peers!
2. Tier II:
    - Comcast:AS7922
3. Tier III:
    - Home internet, single home ISP
    - usually soley purchase routing

## BGP: Border Gateway Protocol
- A type of **Path-Vector Routing**
- Uses "KeepAlive" instead of "HELLO" protocols
- Advertisements contain a lot
- Advertisements only sent to neighbors
- Runs **On top of TCP**
    - network is reliable, doesn't need to keep pinging

### AS Hierachy Relationships.
- Transit Customer: an ISP advertised all of its customer's routes.
- Transit Provider:  
- Peering: 

#### Does BGP scale?
- Internet is currently using it, so it must
- Though, routing tables reaching max size
- Is getting more complicated by economic and geo-political interests
- Suffers human configuration errors
