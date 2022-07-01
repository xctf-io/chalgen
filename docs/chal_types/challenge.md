Module chal_types.challenge
===========================

Functions
---------

    
`chal_to_kube_config(chal, registry_base_url, local)`
:   

    
`gen_kube(kube_dir, chal_kube_configs, local)`
:   

    
`get_kube_deployment(chal, local, namespace='challenges')`
:   

    
`get_kube_ingress(chals, namespace='challenges')`
:   

    
`get_kube_service(chal, namespace='challenges')`
:   

    
`mkdir_p(path)`
:   

    
`push_container(chal_config, local)`
:   

Classes
-------

`ChallengeHost(url, chals_dir)`

```
Methods
    - add_chal(self, file)
    - create(self)
```

`GeneratedChallenge`
:   

```
Descendants:
    - chal_types.binary_exploit.SimpleOverflow
    - chal_types.chalenv.ChallengeEnvironment
    - chal_types.crypto.Base64Challenge
    - chal_types.crypto.BinaryChallenge
    - chal_types.crypto.CBCPaddingOracle
    - chal_types.crypto.CaesarCipherChallenge
    - chal_types.crypto.ECBBlockDuplication
    - chal_types.crypto.HashExtension
    - chal_types.crypto.HexChallenge
    - chal_types.crypto.MD5Challenge
    - chal_types.crypto.RSAChallenge
    - chal_types.crypto.SHA256Challenge
    - chal_types.crypto.VigenereChallenge
    - chal_types.crypto.XorChallenge
    - chal_types.forensics.forensics.BinaryAudio
    - chal_types.forensics.forensics.BrokenPNGHeaderChallenge
    - chal_types.forensics.forensics.ChangeExtension
    - chal_types.forensics.forensics.ChromiumHistory
    - chal_types.forensics.forensics.DiffImages
    - chal_types.forensics.forensics.DocxCarving
    - chal_types.forensics.forensics.EditContrast
    - chal_types.forensics.forensics.EditNotepad
    - chal_types.forensics.forensics.EncryptedZipChallenge
    - chal_types.forensics.forensics.Ext4FileRecovery
    - chal_types.forensics.forensics.FileCarving
    - chal_types.forensics.forensics.GitReassemblyChallenge
    - chal_types.forensics.forensics.GitRevertChallenge
    - chal_types.forensics.forensics.HiddenStuffInPDF
    - chal_types.forensics.forensics.ImageExifChallenge
    - chal_types.forensics.forensics.InvisibleChars
    - chal_types.forensics.forensics.LSB
    - chal_types.forensics.forensics.ReverseAudio
    - chal_types.forensics.forensics.SpectrogramChallenge
    - chal_types.forensics.forensics.SteghideChallenge
    - chal_types.forensics.networking.KeyboardInput
    - chal_types.forensics.networking.PCAPLogin
    - chal_types.forensics.networking.PingPCAP
    - chal_types.forensics.networking.SQLLog
    - chal_types.forensics.qr_code.BrokenQRCode
    - chal_types.forensics.qr_code.QRCodeChallenge
    - chal_types.phishing.PhishingDefenseChallenge
    - chal_types.reversing.DocxMalware
    - chal_types.reversing.SimpleJarRE
    - chal_types.reversing.SimpleStringRE
    - chal_types.web.RobotsTxtChallenge
    - chal_types.web.TemplateInjection

Class Variables:
    - security
```