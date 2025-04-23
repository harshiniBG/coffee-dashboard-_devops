from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the home page"

@app.route('/dashboard')
def dashboard():
    # This should redirect if not logged in
    return redirect(url_for('login'))

# ... existing code ...