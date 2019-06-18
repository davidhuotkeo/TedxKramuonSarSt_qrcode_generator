# TedxKramuonSarSt_qrcode_generator
Using Qrcode to tracking the audiences' attendance

## How to use

Install qrcode library in python using pip

```bash
pip install qrcode
```

create new file and write like this

```python
from Qrcode import *

qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=20,
        border=1,
    )

q = QRcode(qr)
q.input_data('David is awesome')
q.generate('david', 'png')
```

We are ready to go.
