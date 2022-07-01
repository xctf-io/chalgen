Module chal_types.web
=====================

Classes
-------

`RobotsTxtChallenge`

``` 
Flag is located in the robots file
 
Config:
    index - Custom index.html page
    text - Optional additional information

Ancestors:
    - chal_types.challenge.GeneratedChallenge
 ```

`TemplateInjection`

```
Flag is located in flag.txt

Config:
    author - author of mad lib generator
    blacklist - blackist for disallowed words(leave as [] for a blank blacklist)
    files - optional additional files to add to webroot

Ancestors:
    - chal_types.challenge.GeneratedChallenge
```