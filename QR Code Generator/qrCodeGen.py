import qrcode

# img = qrcode.make("It's me Shaury")
# img.save("qrtest.png")

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=20, border=5)
qr.add_data("HEY!")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qrtest1.png")
