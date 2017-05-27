# Rec 8 IP
### Mar 7 2017
### Martin Rinard



## Background
From 1988, before the Internet was commercialized.   

## Basis of Networks:

**Unreliable Datagrams** => IP.
- Great implementer's freedom.
- Given address, it will fire the packet at that address. Maybe it gets there. Maybe not.
    - Fire and forget. No state recorded.
- Datagram: unit of transfer associated with networks => Sending IP Packets.
- On a high level: The entire interface of the internet:
    - `Internet.Accept_IP_Packet(datagram)`
        - No order is guaranteed
        - No arrival is guaranteed
        - Packets can be duplicated
- The internet can unreliably send datagrams as packets. Thats it.
- To transfer a movie, you layer on top of this.

**Reliable Transport Protocol** => TCP
- Built on top of IP
- => Reliable Streams
- TCP gives:
    - Stream of data is sent, stream of data arrives.

#### Historical Contexts on Design Decisions
- Build during Cold-War paranoia of 1960s
    - Military / ARPANET / DARPA
    - Even if Ruskies blow up half the US, the rest of the internet still works.
    - TCP on top of IP for robustness

#### Other networks
=> Stifling monotheistic conceptual time in terms of networks. Everyone only knows the internet.

- Connection Based Network:
    - Pre-determined Quality of Service
    - send a stream of bytes
    - Finds path, determines bandwidth, reserves buffers, establishes connection, then sends.
    - Has handware support ($$$)
    - All nodes must have cooperation

- Our Internet:
    - Has no pre-determined quality.
    - No gaurantees
    - BUT, if half the network blows up, it still works the same.
    - Don't have to establish a secure connect to send data.


### Wisdom of Martin Rinard
- We think only network is internet

Truth about life:
- In many cases it is better to be confidently wrong, than inconfidently right.
- Also, you gotta be able to walk away from positions, by preserving ambiguity => "Plausible Deniability" => Confidently take an ambiguous position. Learn the tactics of the other side.
TAKE THE MINUTES OF THE MEETINGS => you get to manipulate the truth.

- Number one priority: Manipulate the evaluation metric.
    - As soon as you figure out a metric to evaluate on, people will figure out how to optimize that metric in insane and creative ways.
    - Ask yourself "how is everyone around me manipulating the evaluation metric"

## ------- Reading Notes ------
>  "The Design Philosophy of the DARPA Internet Protocols" by David Clark. Skip Section 10.

## -------- Reading Questions ---------
* What were three of the most important goals of the early Internet?
    The fundamental goal of the internet was to connect and utilize existing interconnected networks. More Specifically,
    1. Internet Communication must continue despite any loss of networks or gateways. -> Reliability
    2. The Internet architecture must permit distributed management of its resources
    3.The Internet architecture must accommodate a variety of networks
* How was it designed to meet those goals?
    A number of design considerations were invoked, as the needs of the internet changed. A layered approach, separating transmission, addressing, physical links, etc, allowed for modularity and scalability in the network. Additionally, a standard, but loose, system was introduced. Packets were used, but with no definite size; packets we not totally guaranteed to arrive, etc.
* Why were those goals important (or, why does the author believe that those goals were important)?
    - The author stresses that the goals were listed in order of priority, and that the fact that this originated as a military project pushed reliability to the top and accountability to the bottom. The original internet was designed to robust and quick to get into operation. The author believes that if commercial interests instead of military began the initial implementation, priorities would have been different.
