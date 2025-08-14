import qrcode
url=input("Enter your url,text,number e.g https://google.com: ") # user input for text they want to encode
qr=qrcode.QRCode(
    version=1, #pixels...1 means 21x21
    error_correction=qrcode.constants.ERROR_CORRECT_L,#how strong the qr code is...L,M,H
    box_size=10,# the size of the boxes
    border=4,# the border,the white part you see around the code
)

qr.add_data(url) # adds the url for compiling

qr.make(fit=True) #making the entire message fit in the qr code

image=qr.make_image(fill_color="black",back_color="white") #slecting the colors of the qr code


image.save("qrcode.png") # saving your qr code

print("QR code generated and saved as qrcode.png") #success message
