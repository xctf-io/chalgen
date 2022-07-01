Module chal_types.forensics.networking
======================================

Classes
-------

`KeyboardInput`
:   

```
Find what someone typed based on usb traffic
    
Config:
    text: additional text before flag
    rand_backspaces: add random backspaces to increase dificulty(doesn't change message)

Ancestors:
    - chal_types.challenge.GeneratedChallenge
```

`PCAPLogin`
:   

```
Find the login credentials in PCAP

Config:
    username - username to find
    password - password to find

Ancestors:
    - chal_types.challenge.GeneratedChallenge
```

`PingPCAP`
:   

```
Find the data in ping requests
    
Config:
    text: additional data to add to communication(optional)

Ancestors:
    - chal_types.challenge.GeneratedChallenge
```

`SQLLog`
:   

```
Find what the attacker got in a sql injection attack

Config:
    flag_user: username of attacked user
    other_users: other users in database(at least one)
    file: optional param to add a file through LOADFILE

Ancestors:
    - chal_types.challenge.GeneratedChallenge
```