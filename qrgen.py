import pandas as pd
import qrcode

# Read the Excel sheet into a pandas dataframe
df = pd.read_csv('data.csv')

# Loop through each row in the dataframe and generate a QR code
for index, row in df.iterrows():
    # Extract the text from the dataframe
    qr_text = row[0]

    # Create a QR code object and encode the text
    qr = qrcode.QRCode(version=None, box_size=10, border=4)
    qr.add_data(qr_text)
    qr.make(fit=True)

    # Generate an image file for the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"{qr_text}.png")
