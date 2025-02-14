# Image Steganography Web App

This project is a web-based steganography application that allows users to securely hide and extract secret messages within images using Flask and OpenCV.

## Features
- **Encrypt Message**: Hide a secret message inside an image with password protection.
- **Decrypt Message**: Retrieve the hidden message using the correct password.
- **Secure Encoding**: Uses pixel manipulation to embed the data.
- **User-Friendly UI**: Simple interface for encryption and decryption.

## Tech Stack
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Libraries**: OpenCV, Base64

## Project Structure
```
.
|-- README.md
|-- api
|   `-- index.py  # Flask backend
|-- requirements.txt  # Dependencies
|-- templates
|   `-- index.html  # Frontend UI
`-- vercel.json  # Deployment configuration
```

## Installation & Usage

### Prerequisites
- Python 3.9 or Python 3.12
- pip (Python package manager)

### Setup
1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/image-steganography.git
   cd image-steganography
   ```
2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
3. **Run the Flask app**
   ```sh
   python api/index.py
   ```
4. **Access the web app**
   Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## Deployment
This project is configured for deployment on **Vercel**. To deploy:

Go to the official website : [Vercel](http://vercel.com/)

Follow the on-screen instructions to deploy successfully.


## Author
Developed by **Nivesh Pai**. 🚀

