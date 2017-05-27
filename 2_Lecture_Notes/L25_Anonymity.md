# Lecture 25: Anonymity
### 5/15/17

--------------------------------------------------------------------------------

## In the news....
WannaCry Ransomware attack happened on Friday.
- Used ransom ware encryption
- had a kill-switch (C&C server, kinda)
- Some dude registered the kill-switch, and stopped the attack in the US.
- didn't use a domain-flux system

## encryption
1. Symmetric
    - AES
        - Very Fast, variable size

2. Asymmetric
    - Public Key, Private Key
    - RSA
    - pub/priv keys for encryption and for signatures use different kinds of keys

## How Tor Works...


- Being tracked at all is the same as being tracked all the time

- no packet should say from original sender to the target
- no entity in the network should receive a packet from orig sender and send directly to target
- no entity in the network should keep state that links sender to target
- data should no appear the same across multiple packets

- TOR provides no E2E encryption, need TLS on top of TOR

- Katrina likes TOR
