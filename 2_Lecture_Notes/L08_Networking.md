# Lecture 7:  Networking
### March 6, 2017
Intro to Networking

--------------------------


## (P) ----- Networks ------
Networks are represented as **graphs**, $G=(V,E)$  

Completely connected graphs would be a nightmare to the internet, every device would have to link to every device. Instead, our nodes are divided into **end-points** and **switches**, where end-points are devices, and switches are junctions that join many end-points.

### Naming and Addressing
- Each machine needs a unique identifier/name
- Each node learns a _minimum cost_ route to every other reachable node.
- "Minimum cost" => naively running Dijkstra's Algorithm

### Routing Protocols
- Many routing protocols exist.
- Networks are dynamic. Protocols must be re-run and updated.
    - Path = full route
    - Route = piece of path that 1 node is responsible for.

### Packets
Packets include [HEADER [DATA]]
- HEADER
    - Source
    - Destination
    - Meta data
- DATA

Switches use queues to handle traffic, where they have a **finite** queue of packets to dispatch. If a switch happens to be full, the packet gets _dropped_.   

### Reliability
There are different Reliable Transport Protocols.
- When sending packages, the receiver can send an acknowledgement, know as an _"Ack"_ to verify that it was received and not dropped.

**HIERARCHY AS A MEANS OF SCALABILITY**

### Layering
![7_osi_layers](http://partsincomputers.com/wp-content/uploads/2016/06/osi-layer.jpg)

Layering made the internet more flexible. (does it still?)
1. Application
2. Presentation
3. Session   :: SSL (SecureSocketsLayer)
4. Transport :: TCP (TransmissionControlProtocol)
5. Network   :: ICMP (internet control message protocol )
6. Data Link :: IP
7. Physical  :: Ethernet

#### DDoS and Security
Direct Denial of Service Attack:
Overloading a server
- Packet filtering is expensive.
"The internet was not designed with accountability in mind."

- The internet is not encrypted by default. All packets cab be sniffed.

### History of The Internet
![ARPANET](https://upload.wikimedia.org/wikipedia/commons/b/bf/Arpanet_logical_map%2C_march_1977.png)
(see MIT, Stanford, WPAFB, Pentagon)

- The Launch of Sputnik inspired ARPA (which is now DARPA)
    - ARPA net (combined addressing and transport)
- We needed reliable communication links
- MIT Owns all IP addresses in 18.x.x.x block (16 million)
    - "Class A block"
    - HP owns all of 15. and 16. block

- 1978: Flexibility encouraged layering
- 1979: Link state routing / EGP
    - Broken into hierarchy of autonomous systems
- 1982: DNS
- 1985: Congestion Control
- 1991: BGP: Border Gateway Protocol ;
    - Money $$$
    - CIDR
- 1993: [Video](http://www.cbc.ca/archives/entry/a-computer-network-called-internet)

- 1993: $$$ COMMERICIALIZATION $$$

HISTORY INFLUENCES DESIGN
