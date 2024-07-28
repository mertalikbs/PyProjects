import qrcode

#First, we decided QR Code's version, error correction level, and box size.
qr = qrcode.QRCode(
  version=1,
  box_size=25,
  border=1,
  error_correction=qrcode.constants.ERROR_CORRECT_L,)

#Then, we added the data we want to attach to our QR code.
isContinue = True

while isContinue == True:
  data = input("Enter the data you want to attach to your QR code: ")
  qr.add_data(data)
  qr.make(fit=True)
  img = qr.make_image(fill_color="black", back_color="white")
  img.save("qrcode.png")
  print("Your QR code has been saved as qrcode.png")
  isContinue = input("Do you want to add more data to your QR code? (y/n) ")
  isContinue = True if isContinue.lower() == "y" else False