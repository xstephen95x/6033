# Lecture 10: New Technologies on the Internet.
## Mon March 20, 2017
### P2P networks, File Sharing, VoIP, CDNs.
### File sharing, BitTorrent, Skype/VoIP, etc.

Today: We have a network which works reliably.
- Connection [X]
- Routing [X]
- Transport [X]
- Applications???

-----------------------------------
### File Sharing
Model:  **Client <--> Server**
- Single point of failure (the server)

Model: **CDN**: Content Distribution Network
- Have servers in different geographical areas to serve fast file access
- Must continually buy more servers in more areas to scale.
- as users scale to inf. cost scales to infinity dollars.

Model: **P2P**: Peer-to-Peer sharing
- every user is also a server.
- after receiving a piece of a file, the user also seeds that piece of the file
- Uses an overlay network (overtop of existing internet)
- In theory, this scales to infinity without costs scaling to infinity.

##### BitTorrent:
How do we incentivize users to seed files?

1. We create a torrent file, HP.torrent, which contains information about the file, such as the URL of the tracker.
2. A tracker (a computer which knows the IP address of all peers using the file) sends a list of peers involved in the swarm.
3. the downloader begins receiving blocks of the file (in any order)

- To incentivize users to seed files, users who send the most receive the most in the next round.
- The process of giving free-bandwidth is

Is BitTorrent the best way to share files?
- having many peers makes it very fault tolerant in terms of access to the file
- Though, having a single tracker computer means there is still a single point of failure.
- Trackers also have a list of all users in the swarm, which is not private.!

##### BitTorrent DHT: Distrubuted Hash Tables
**Improvement** BitTorrent without trackers! => Decentralization.         
- Instead of using a tracker machine, have a distributed data structure
    - Each machine stores a portion of the DHT's keys.
- Instead of having an accessible list of all users in swarm, use a hashed data structure.
    - keys => URLs of files
    - put(URL, IP Addr of Peer)
    - get(URL) => list of peers

------------------------------------
### Voice over IP (VoIP)
DISCLAIMER: Skype is a proprietary technology. Skype information is non-official and secret.
Skype actually closely models the BitTorrent protocol.


Skype uses a P2P network to improve the quality of VoIP.

=> NAT: Network Address Translator (has some public IP)

The skype network has a set of private users that sit behind a NAT.     
- When a user behind the NAT sends a packet, the NAT routes it and labels itself as the sender.

S => N_1 => (S) => N_2 => R     

In the middle of the network, we have a (S), which is a "Super Node" which acts as a telephone operator, and configures the connection.     

Different from file-sharing, VoIP must acquire blocks mostly in order.

### CDNs
They do some really awesome things, like Akamai down the street.
