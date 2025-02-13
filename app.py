from flask import Flask, render_template, request, send_file
import cv2
import numpy as np
import os

app = Flask(__name__, static_folder="static", template_folder="templates")

# Dictionary for encoding and decoding characters
d = {chr(i): i for i in range(255)}
c = {i: chr(i) for i in range(255)}

def encrypt_image(image_path, message, password):
    img = cv2.imread(image_path)
    if img is None:
        return None

    height, width, _ = img.shape
    n, m, z = 0, 0, 0

    if len(message) > width * height:
        return None  # Message is too large

    for i in range(len(message)):
        img[n, m, z] = d[message[i]]
        n += 1
        m += 1
        z = (z + 1) % 3

    encrypted_path = "static/encrypted.png"
    cv2.imwrite(encrypted_path, img)
    return encrypted_path

def decrypt_image(image_path, message_length, password):
    img = cv2.imread(image_path)
    if img is None:
        return None

    n, m, z = 0, 0, 0
    message = ""

    for i in range(message_length):
        message += c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3

    return message

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
            return {"status": "success", "encrypted_image": encrypted_path}
    
    return {"status": "error", "message": "Encryption failed"}

@app.route("/decrypt", methods=["POST"])
def decrypt():
    image = request.files["image"]
    message_length = int(request.form["length"])
    password = request.form["password"]

    if image:
        image_path = "static/decrypt.png"
        image.save(image_path)
        decrypted_message = decrypt_image(image_path, message_length, password)
        if decrypted_message:
            return {"status": "success", "message": decrypted_message}

    return {"status": "error", "message": "Decryption failed"}

if __name__ == "__main__":
    app.run(debug=True)
