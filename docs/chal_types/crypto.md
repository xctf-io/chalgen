Module chal_types.crypto
========================

Classes
-------

`Base64Challenge`
    
```markdown
A simple base64 decoding challenge

Config:
    None

 Ancestors:
    - chal_types.challenge.GeneratedChallenge
```

`BinaryChallenge`
    
```markdown
A simple binary decoding challenge

Config:
    None

Ancestors:
    - chal_types.challenge.GeneratedChallenge
```

`CBCPaddingOracle`

```markdown
Config:
    key - The key to use
    secret - The secret value to append before flag

Ancestors:
    - chal_types.challenge.GeneratedChallenge
```


`CaesarCipherChallenge`
    
```markdown
A simple Caesar cipher challenge
    
Config:
    shift - The amount to shift the alphabet by

Ancestors:
    - chal_types.challenge.GeneratedChallenge   Solve the Caesar cipher challenge
```

`ECBBlockDuplication`

```markdown
Config:
    key - The key to use
    secret - The secret value to append before flag

Ancestors:
    - chal_types.challenge.GeneratedChallenge
```


`HashExtension`
    
```markdown
A simple SHA1 hash extension challenge

Config:
    key - The secret for HMAC
    author - The author of the website
    text - Additional text in the secret file, in order to connect to other challenges
    custom_files - Custom files on the web server

Ancestors:
    - chal_types.challenge.GeneratedChallenge
```


`HexChallenge`
    
```markdown
A simple hex decoding challenge

Config:
    None

Ancestors:
    - chal_types.challenge.GeneratedChallenge
```

`MD5Challenge`
    
```markdown
A reverse MD5 hash challenge

Config:
    None

Ancestors:
    - chal_types.challenge.GeneratedChallenge
```

`RSAChallenge`
    
```markdown
RSA challenge

Config:
    None

Ancestors:
    - chal_types.challenge.GeneratedChallenge
```

`SHA256Challenge`
    
```markdown
A reverse SHA256 hash challenge

Config:
    None

Ancestors:
    - chal_types.challenge.GeneratedChallenge
```

`VigenereChallenge`
    
```markdown
A decode vigenere challenge

Config:
    key: word/phrase used to encrypt plaintext

Ancestors:
    - chal_types.challenge.GeneratedChallenge
```

`XorChallenge`
    
```markdown
A single or multi byte xor challenge

Config:
    key - A single byte key to xor the flag with
    text - Optional text to put before the flag to make sure there is enough text to correctly recover the flag

Ancestors:
    - chal_types.challenge.GeneratedChallenge
```
