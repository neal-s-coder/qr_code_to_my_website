import qrcode

# Website URL
url = "https://neal-s-coder.github.io/"

# Generate QR code
qr_code = qrcode.make(url)

# Save the QR code as an image file in the current directory
file_path = "qr_code_neal_website.png"  # No directory path
qr_code.save(file_path)

print(f"QR code saved to: {file_path}")
