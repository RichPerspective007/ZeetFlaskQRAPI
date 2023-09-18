from flask import Flask, request, send_file
import qrcode

app = Flask(__name__)

@app.route('/generate_qr', methods=['POST'])
def generate_qr_code():
    data = request.get_json()
    if data is not None and 'values' in data:
        values = data['values']

        # Create a QR code with the concatenated values
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(','.join(values))
        qr.make(fit=True)

        # Generate the QR code image
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image to a temporary file
        img.save('temp_qr.png')

        # Send the image file as a response
        return send_file('temp_qr.png', mimetype='image/png')
    else:
        return 'Invalid input data', 400

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
