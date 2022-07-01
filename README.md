[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.mcpshsf.com/#https://github.com/breadchris/mcps-hsf-chalgen)

# chalgen

chalgen generates challenges which are nodes in an evidence map

## Prerequisites

- Follow the documentation [here](https://pygraphviz.github.io/documentation/stable/install.html) to install `pygraphviz` for your system
- Install Docker from [here](https://docs.docker.com/engine/install/)
- Install kubectl from [here](https://kubernetes.io/docs/tasks/tools/)

## Basic setup

Install the requirements:

```console
pip install -r requirements.txt
```

Run the application:

``` console
python chalgen.py --help
```

Example challenge generator command

```console
python chalgen.py gen --chal-config tests/test_ctf/base64/chal.yaml
```

To run the tests:

```console
pytest
```

## TODO

* take all created evidence and integrate it into this

## Challenge Options

### Forensics

#### Base

- [ ] IRC Server
- [ ] Windows VM
- [ ] Linux VM

#### Challenges

- [ ] netcat into a server
    - [ ] Send ASCII data
  - [ ] Send non ASCII data
- [ ] SSH into server
- [x] Image metadata
- [ ] Git
	- [ ] File in git objects
	- [x] Recover files from series of git commits (and git stash?)
- [ ] PCAP - (use scapy)
	- [ ] Follow http stream to get username and passwords
	* [ ] Recording of keyboard input
	- [ ] Recording of bluetooth traffic
- [x] Encrypted ZIP
- [ ] PDF [NSA Guide](http://www.itsecure.hu/library/file/Biztons%C3%A1gi%20%C3%BAtmutat%C3%B3k/Alkalmaz%C3%A1sok/Hidden%20Data%20and%20Metadata%20in%20Adobe%20PDF%20Files.pdf)
- [x] Carve out file from file
- [x] Extract file from docx
- [ ] Android file system
	- [ ] Recover browser history from db
	- [ ] Find location history and map it
- [ ] Re-assemble images from parts
- [ ] Fix broken torrent file
- [x] EXT4 deleted file recovery
- [x] Image in audio (Audacity thing)
- [ ] Memory dump analysis
- [x] Diff two images to get some value
- [ ] Run program written in an esoteric language [such as this](https://tcode2k16.github.io/blog/posts/picoctf-2019-writeup/general-skills/#mus1c)
- [ ] Given a text file with numbers, convert to an audio file and listen to it for the flag (Girls Go CyberStart 2019, no links yet)

### Cryptography

#### Challenges

- [x] Base 64
- [x] Binary
- [x] Caesar cipher
- [x] Vigenere cipher - https://ctf101.org/cryptography/what-is-a-vigenere-cipher/
- [x] Given a bunch of hashes, reverse them to get flag
- [x] Substitution
- [x] Xor
	- [x] Single byte
	- [x] Multi byte xor (needs solver)
- [ ] ECB use repeated chunks
- [ ] Padding Oracle
- [x] Hash length extension
- [ ] RSA - https://github.com/sourcekris/RsaCtfTool
### Web

#### Base Images

- [ ] Blog
- [ ] Twitter Clone - https://github.com/mesosphere/tweeter-go
- [ ] Facebook Clone
- [ ] Portfolio site
- [ ] Pokemon GO

#### Challenges

- [ ] Flag in cookies
- [ ] Authorization done client side
- [ ] Path Traversal (CSAW RED 2019 Prelims, also https://medium.com/hackstreetboys/ritsec-ctf-2018-writeup-web-72a0e5aa01ad)
- [ ] Exposed files
	- [ ] .htpasswd
	- [ ] robots.txt
	- [ ] .git
- [ ] SQLi Injection
	- [ ] report error (basic)
	- [ ] union select
	- [ ] like query
	- [ ] blind
- [ ] XSS
- [ ] Obfuscated javascript
- [ ] PHP
	- [ ] Deserialize
	- [ ] Using "==" to do stupid things
- [ ] SSRF
- [x] Jinja template injection (https://0day.work/jinja2-template-injection-filter-bypasses/)

### Reverse Engineering / Programming

- [ ] ELF Binary
	- [ ] Flag as a string in binary
	- [ ] Flag is xor'd in function in binary
	- [ ] Simple crackme
- [ ] APK
	- [ ] Flag in resources
	- [ ] Follow data from java to cpp lib
- [ ] Reverse engineer merscenne twister random generator
- [ ] Constraint solving ([like this](https://raw.githubusercontent.com/breadchris/Just4Fun/14e7564ac2d3e359d88698a4499a74bc7f0aa369/leakz/HSF-Finals/Hacktivist-Website/check.py))
- [ ] Reverse custom encryption [csaw hsf necronomicon](https://github.com/breadchris/Just4Fun/blob/14e7564ac2d3e359d88698a4499a74bc7f0aa369/leakz/HSF-Finals/Encryption-Software/crypt.c)
- [ ] Weird architecture (Apollo landing asm?)
- [ ] Reverse engineer jar file

### Binary Exploitation

- [ ] Buffer overflow
	- [ ] Into data --> change value
	- [ ] Into EIP --> call give shell
	- [ ] Into Canary --> use data leak to guess canary
	- [ ] Leak out canary because process is forking (brute_cookie: https://trailofbits.github.io/ctf/exploits/binary2.htm)
	- [ ] ASLR on, ROP chain with provided parts
	- [ ] ASLR on, ROP chain without provided parts (ret2libc)
- [ ] Format string
	- [ ] Leak out flag with %s
	- [ ] Change value of stack variable with address
	- [ ] Load arbituary address and write to it (GOT table)
	
### Scripting

Some challenges for writing a basic python script on repl.it

### Hardware

Some challenges that use Tinker to reverse hardware components

## Evidence Guidelines

* A challenge may provide an option to include data within it to make it story relevant
* A challenge is expected to be solvable by itself. If a challenge is not solvable by itself (i.e. encrypted zip has unguessable password), then a connection must be specified for the challenge.
* Challenges may specify a way to embed another challenge inside of themselves.

Some questions that should be answered:

* How much perscription do we want to give challenges?
* If we are creating an sql injection challenge, do we give them website and the vuln code?
* Need to figure out how the vuln plugs into a website. Have a module system for the website that you drop in views for challenges.

## Generating Evidence Connections

// TODO
