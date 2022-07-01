Module chal_types.forensics.qr_code
===================================

Classes
-------

`BrokenQRCode`

```
Fix a broken QR code
    
Config:
    fluff - some text fluff to include in the challenge

Ancestors
    - chal_types.challenge.GeneratedChallenge
```



`QRCodeChallenge(name, flag, config)`
:   

```
Create a QR Code with 
    
Config:
    fluff - some text fluff to include in the challenge
    background_image - background image to overlay 
        file - filename of background image
        x_pos - x coordinate of qr code placement
        y_pos - y coordinate of qr code placement

Ancestors:
    - chal_types.challenge.GeneratedChallenge
```
