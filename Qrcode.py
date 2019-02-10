# to use qrcode library we need to install it first
# pip install qrcode
import qrcode

# create qrcode
qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=20,
        border=1,
    )

# The data that you want to store
data = "Kim Kosei"

# Add data
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image()

# Save it somewhere, change the extension as needed:
img.save("image.png")
# img.save("image.bmp")
# img.save("image.jpeg")
# img.save("image.jpg")
