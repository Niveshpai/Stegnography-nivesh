from flask import Flask, render_template, request
import cv2
import logging


logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__, static_folder="static", template_folder=".")

# Character encoding dictionaries
d = {chr(i): i for i in range(255)}
c = {i: chr(i) for i in range(255)}

# Delimiter to mark the end of the message
END_MARKER = "###END###"

def encrypt_image(image_path, message, password):
    img = cv2.imread(image_path)
    if img is None:
        return None

    # Store the password inside the image along with the secret message
    full_message = password + "|" + message + END_MARKER  

    height, width, _ = img.shape
    n, m, z = 0, 0, 0

    if len(full_message) > width * height:
        return None  # Message is too large for the image

    for i in range(len(full_message)):
        img[n, m, z] = d[full_message[i]]
        n += 1
        m += 1
        z = (z + 1) % 3

    encrypted_path = "/app/static/encrypted.png"
    cv2.imwrite(encrypted_path, img)
    return encrypted_path

def decrypt_image(image_path, entered_password):
    img = cv2.imread(image_path)
    if img is None:
        return "Decryption failed"

    n, m, z = 0, 0, 0
    extracted_data = ""

    while True:
        char = c[img[n, m, z]]
        if extracted_data.endswith(END_MARKER):  
            extracted_data = extracted_data.replace(END_MARKER, "")
            break
        extracted_data += char
        n += 1
        m += 1
        z = (z + 1) % 3

    # Ensure extracted data contains "|"
    if "|" not in extracted_data:
        return "Decryption failed"

    stored_password, secret_message = extracted_data.split("|", 1)

    # Check if entered password matches the stored one
    if entered_password != stored_password:
        return "Not authorized"

    return secret_message


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/encrypt", methods=["POST"])
def encrypt():
    image = request.files["image"]
    message = request.form["message"]
    password = request.form["password"]

    if image:
        image_path = "static/uploaded.png"
        image.save(image_path)
        encrypted_path = encrypt_image(image_path, message, password)
        if encrypted_path:
            encrypted_image_url = f"https://stegnography-nivesh.onrender.com/static/encrypted.png"
            return {"status": "success", "encrypted_image": encrypted_image_url}
        else:
            return {"status": "error", "message": "Encryption failed"}

@app.route("/decrypt", methods=["POST"])
def decrypt():
    image = request.files["image"]
    password = request.form["password"]

    if image:
        image_path = "static/decrypt.png"
        image.save(image_path)
        decrypted_message = decrypt_image(image_path, password)
        
        if decrypted_message:
            return {"status": "success", "message": decrypted_message}

    return {"status": "error", "message": "Decryption failed"}

if __name__ == "__main__":
    app.run(debug=True)
