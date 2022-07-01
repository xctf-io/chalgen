Module chal_types.forensics.forensics
=====================================

Classes
-------

`BinaryAudio(name, flag, config)`
:   

```
Use binary audio to find flag
    
Config:    
    text - additional text to say

Ancestors:
    - chal_types.challenge.GeneratedChallenge
```

`BrokenPNGHeaderChallenge(name, flag, config)`
:   

```
Flag is located in the image, whose header is broken
    
Config:    
    orig_img - The relative path of the image to use

Ancestors:
    - chal_types.challenge.GeneratedChallenge
```

`ChangeExtension(name, flag, config)`
:   

```
Change the file extension to access the file
    
Config:    
    orig_file - txt file
    out_ext - new extension

Ancestors:
    - chal_types.challenge.GeneratedChallenge
```

`ChromiumHistory(name, flag, config)`
:   

```
Do forensic analysis on a chromium cache folder
    
Config:    
    script - puppeteer script to run

Ancestors:
    - chal_types.challenge.GeneratedChallenge
```

`DiffImages(name, flag, config)`
:   

```
Flag is located in the byte difference between two images
    
Config:    
    orig_img - The relative path of the image to use

Ancestors:
    - chal_types.challenge.GeneratedChallenge
```

`DocxCarving(name, flag, config)`
:   

```
Carve out files from a docx file
    
Config:    
    main_file - main file to be released
    hidden_file - file to be hidden in main_file (Note: the contents of this file contain the flag)
    dest_path - path within the docx to put the hidden_file

Ancestors:
    - chal_types.challenge.GeneratedChallenge
```

`EditContrast(name, flag, config)`
:   

```
Ancestors:
    - chal_types.challenge.GeneratedChallenge
```

`EditNotepad(name, flag, config)`
:   

```
Open in Notepad to find flag
    
Config:    
    orig_img - image file

Ancestors:
    - chal_types.challenge.GeneratedChallenge
```

`EncryptedZipChallenge(name, flag, config)`
:   

```
An encrypted zip challenge
    
Config:    
    files_dir - files to be included with the challenge
    password - the password used to encrypt the files
    word_list - [optional]

Ancestors:
    - chal_types.challenge.GeneratedChallenge
```

`Ext4FileRecovery(name, flag, config)`
:   

```
Recover a file 
    
Config:    
    deleted_evidence - A directory containing the evidence that will be deleted
    fluff - A directory containing data to be added to the filesystem

Ancestors:
    - chal_types.challenge.GeneratedChallenge
```

`FileCarving(name, flag, config)`
:   

```
Carve out a file from another file
    
Config:    
    main_file - main file to be released
    hidden_file - file to be hidden in main_file (Note: the contents of this file contain the flag)

Ancestors:
    - chal_types.challenge.GeneratedChallenge
```

`FileEvidence()`
:   

```
File Evidence
    
Config:    
    None

Ancestors:
    - chal_types.chalenv.ChallengeEnvironment
    - chal_types.challenge.GeneratedChallenge
```

`GitReassemblyChallenge(name, flag, config)`
:   

```
Determine flag by reassambling parts from git
    
Config:    
    text - extra text to include in git file
    num_parts - number of parts to split the flag into
    git_email - email of user 
    git_name - name of user

Ancestors:
    - chal_types.challenge.GeneratedChallenge
```

`GitRevertChallenge(name, flag, config)`
:   

```
Determine secret information from old commits
    
Config:    
    text - extra text to include in git file
    file - non-secret file name
    file_contents - non-secret file contents
    git_email - email of user 
    git_name - name of user

Ancestors:
    - chal_types.challenge.GeneratedChallenge
```

`HiddenStuffInPDF(name, flag, config)`
:   

```
Find the hidden stuff in the pdf
    
Config:    
    file - pdf file to mess with

Ancestors:
    - chal_types.challenge.GeneratedChallenge
```

`ImageExifChallenge(name, flag, config)`
:   

```
Flag is located in image meta data
    
Config:    
    orig_img - The relative path of the original image to use
    metadata_key - The metadata key to store the flag under
    flag_transform - The method to use to transform the flag (so you can't solve it with strings)
    lat - latitude of gps exif
    lng - longitude of gps exif

Ancestors:
    - chal_types.challenge.GeneratedChallenge
```

`InvisibleChars(name, flag, config)`
:   

```
Use invisible characters to hide the flag
    
Config:    
    hide_text - text before invisible characters

Ancestors:
    - chal_types.challenge.GeneratedChallenge
```

`LSB(name, flag, config)`
:   

```
Least Significant Bit Encoding
    
Config:    
    orig_img - The relative path of the image to use

Ancestors:
    - chal_types.challenge.GeneratedChallenge
```

`ReverseAudio(name, flag, config)`
:   

```
Reverse the audio to hear the flag
    
Config:    
    text - additional text to say

Ancestors:
    - chal_types.challenge.GeneratedChallenge
```

`SpectrogramChallenge(name, flag, config)`
:   

```
Flag is located in the spectrum data of the audio file
    
Config:    
    orig_img - The relative path of the image to use
    orig_audio - Original audio before the spectogram
    output_wav - The relative path to the wav output file

Ancestors:
    - chal_types.challenge.GeneratedChallenge
```

`SteghideChallenge(name, flag, config)`
:   

```
Hide flag using steghide
    
Config:    
    text - addon text
    image - image to hide information in
    password - add password (optional)
    wordlist - wordlist for password cracking (optional)

Ancestors:
    - chal_types.challenge.GeneratedChallenge
```