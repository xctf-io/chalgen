Module chal_types.chalenv
=========================

Classes
-------

`ChallengeEnvironment`
:   

```
Ancestors:
    - chal_types.challenge.GeneratedChallenge

Descendants:
    - chal_types.chalenv.FacebookDjango
    - chal_types.chalenv.FileshareFlask
    - chal_types.chalenv.JekyllBlog
    - chal_types.chalenv.ShellServer
    - chal_types.chalenv.StaticSite
    - chal_types.chalenv.TwitterFlask
    - chal_types.chalenv.VirtualMachine
    - chal_types.forensics.forensics.FileEvidence
```

`FacebookDjango`
:
```
Facebook clone
    
Config:
    users - Users of the site
    posts - Posts posted by users
    profiles - Profiles of the users
    comments - Comments posted by users

Ancestors:
    - chal_types.chalenv.ChallengeEnvironment
    - chal_types.challenge.GeneratedChallenge
```

`FileshareFlask`
:   

```
Fileshare Flask
    
Config:
    username - Username to login
    password - Password to login
    files - Files to upload

Ancestors:
    - chal_types.chalenv.ChallengeEnvironment
    - chal_types.challenge.GeneratedChallenge
```

`JekyllBlog`
:   

```
A simple blog
    
Config:
    title - the name of the blog
    email - the email of the author
    author - the name of the author
    description - description of the blog
    posts - list of markdown files to include as posts

Ancestors:
    - chal_types.chalenv.ChallengeEnvironment
    - chal_types.challenge.GeneratedChallenge
```

`ShellServer`
:   

```
Shell Server

Config:
    None

Ancestors:
    - chal_types.chalenv.ChallengeEnvironment
    - chal_types.challenge.GeneratedChallenge
```

`StaticSite`
:   

```
Static Site
    
Config:
    None

Ancestors:
    - chal_types.chalenv.ChallengeEnvironment
    - chal_types.challenge.GeneratedChallenge
```

`TwitterFlask`

```
Twitter clone
    
Config:
    users - Users of the site
    followers - Users that follower other users, each user must exist in `users`
    messages - Messages posted on twitter by users
    dms - Dms sent on twitter by users

Ancestors:
    - chal_types.chalenv.ChallengeEnvironment
    - chal_types.challenge.GeneratedChallenge
```

`VirtualMachine`
:   

```
Virtual Machine
    
Config:
    None

Ancestors:
    - chal_types.chalenv.ChallengeEnvironment
    - chal_types.challenge.GeneratedChallenge
```