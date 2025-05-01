from flask import Flask, render_template, request, redirect, flash, url_for
from flask_talisman import Talisman
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired
from pqc.crypto_utils import generate_keys, encrypt_message, decrypt_message
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
Talisman(app)

app.secret_key = os.getenv('FLASK_SECRET_KEY', 'supersecretkey')  # fallback

class EncryptForm(FlaskForm):
    message = TextAreaField('Message to Encrypt', validators=[DataRequired()])
    submit = SubmitField('Encrypt')

class DecryptForm(FlaskForm):
    ciphertext = TextAreaField('Ciphertext to Decrypt', validators=[DataRequired()])
    submit = SubmitField('Decrypt')

public_key = None
private_key = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global public_key, private_key

    encrypt_form = EncryptForm()
    decrypt_form = DecryptForm()
    encrypted_message = None
    decrypted_message = None

    if 'generate_keys' in request.form:
        public_key, private_key = generate_keys()
        flash('Keys generated successfully!', 'success')
        return redirect(url_for('index'))

    if encrypt_form.validate_on_submit() and 'encrypt' in request.form:
        if public_key is None:
            flash('Please generate keys first.', 'danger')
        else:
            message = encrypt_form.message.data.encode('utf-8')
            encrypted_message = encrypt_message(public_key, message).decode('utf-8')
            flash('Message encrypted successfully!', 'success')

    if decrypt_form.validate_on_submit() and 'decrypt' in request.form:
        if private_key is None:
            flash('Please generate keys first.', 'danger')
        else:
            try:
                ciphertext = decrypt_form.ciphertext.data.encode('utf-8')
                decrypted_message = decrypt_message(private_key, ciphertext)
                flash('Message decrypted successfully!', 'success')
            except Exception as e:
                flash('Decryption failed. Please check your ciphertext.', 'danger')

    return render_template('index.html',
                           encrypt_form=encrypt_form,
                           decrypt_form=decrypt_form,
                           encrypted_message=encrypted_message,
                           decrypted_message=decrypted_message,
                           public_key=public_key.hex() if isinstance(public_key, bytes) else public_key,
                           private_key=private_key.hex() if isinstance(private_key, bytes) else private_key)

if __name__ == "__main__":
    app.run(debug=True)
