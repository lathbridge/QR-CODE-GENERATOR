import qrcode

# Function to generate and save a QR code
def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

if __name__ == "__main__":
    # Replace 'your_data' with the text or URL you want to encode
    data_to_encode = "https://www.linkedin.com/in/emmanuel-oduro-lathbridge-8b41b517a/"
    
    # Replace 'output.png' with the desired output filename
    output_filename = "mycode.png"
    
    generate_qr_code(data_to_encode, output_filename)
    
    print(f"QR code saved as {output_filename}")
