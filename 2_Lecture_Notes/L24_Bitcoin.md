# Lecture 24: Cryptocurency
### Wed May 10, 2017

--------------------------------------------------------------------------------

## --- Class Notes ---

- Need secure channels

## Anonymity
- TOR and Bitcoin


### Bitcoin:
- Currency
    - medium for exchange
    - store of value
- Physical Currency
    - anonymous but IRL
    - cant double spend
    - can't repudiate tx (transaction)
    - don't need third party to verify transactions
    - difficult to monitor and tax txs
    - hard to counterfeit
    - cant use on the internet
- Credit Card
    - completely not anonymous
    - works online
    - is tracked
    - requires a 3rd party to handle transaction (bank)
- Digital Cryptocurrency
    - Decentralized (No Banks)
    -  

### How do Cryptocurrencies work
- Need to avoid a centralized bank.

- say "I, Stephen, Send X, 1 BTC, (id 1231423)"
    - sign it with your key
    - use sequence numbers for duplicates
- Key issue (without banks) is double spending (Main technical Challenge)
    - how do we know you have bitcoin and didn't spend it?
- The receiver publishes a log saying he received your coins
    - what if both txs happen at the same time? (or i DDoS other people)
- well, wait to accept transactions until you can verify it with other people

- Sybil Attack - User creates multiple identities to try to subvert the network
    - make it hard to make many accounts
    - but, still make it anonymous
        - make it computationally hard to make accounts then or make it cost.

- __Mining Bitcoins__:
    - "trying random numbers and hashing them"
    - Goal: add a block of transactions to the blockchain
        - Solve a __proof of work__ to validate a block of transactions
    - **H(t|x) < target**
        - t = bitstring of the block of transactions `1010001001011011010001...`
        - x = randomly chose number (a cryptographic nonce)
        - target = dynamically adjusted target, varying difficulty
    - (criticism: a lot of computation for useless goal)
    - (Pro: good way to thwart Sybil attacks)
    - Monetary reward in place for miners (halfs every 4 years)
    - Need an ordering on coins/transactions
- Mining Collisions:
    - What happens when 2 miners mine the same block at the same time?
        - The blockchain will __Fork__
        - miners only acknowledge the longest fork

### The Blockchain:
1. How do we use the log (blockchain) to verify transactions?
2. What if 2 people find x at once?
3. How do we prevent double spending?

- The blockchain is a distributed public ledger

- Run mining servers in iceland (its cold there and servers like cold)
- 
