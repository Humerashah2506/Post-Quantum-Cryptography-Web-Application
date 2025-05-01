# Post-Quantum Cryptography WebApp
# github link:
https://github.com/Humerashah2506/Post-Quantum-Cryptography-Web-Application
## Overview
This project demonstrates a basic web application that uses Post-Quantum Cryptography (Kyber512) for encrypting and decrypting messages.

## Features
- Key generation (Public/Private Keys)
- Message encryption using public key
- Message decryption using private key
- Secure HTTP headers with Flask-Talisman
- Simple and interactive Bootstrap UI

## Tech Stack
- Python 3.x
- Flask
- pqcrypto library (Kyber512)
- Bootstrap 5
- Flask-WTF, Flask-Talisman
- Gunicorn (for deployment)

## How to Run Locally
1. Create and activate virtual environment
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask app
    ```bash
    python app.py
    ```

4. Open browser at `http://127.0.0.1:5000/`

## Deployment
Deploy easily to Render or PythonAnywhere. Create a `Procfile` and connect your GitHub repo to Render.

---
