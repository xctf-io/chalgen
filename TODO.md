## TODO

* Use [kompose](https://kompose.io/) to simplify the tool
* Add more challenges
* Allow for partial competition generation
	* Stub flag
* Integrate with CTFg
* Improve GUI / port tool to web

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
	- [x] Recording of keyboard input
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
	- [x] robots.txt
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