# Recitation 3 (R04)
> DNS:    
> Naming, Names, Values,    
> recitation 2 cancelled by snow

## Questions for Class
- What is the purpose of DNS? :: Naming system
- How does it work? ::
- Why was it designed to work that way?

## Class Notes
- Resolve:   Names => values
- Resolve:   Implicit context names => values

www.mit.edu => 18.9.22.69 :: domain name => IPv4 addr
32bits per IPv4 addr

Naming Systems:
- DNS
- File system
- building system at MIT (32-144)

A url has a name system inside a namesystem.
-> There are layers

The internet and IP still works without DNS.

## DNS Algorithm
- root name server:
- edu, com, etc name servers
- client
1. on connect, client can ask for root name server
2. client asks root for address
3. root refers to edu name server
4. recursive referals to name servers until
- Lookups are cached on local machine

**Alias == Synonym**
