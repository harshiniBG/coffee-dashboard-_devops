from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
from app import db, User

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = db.users.find_one({'username': username})
        
        if user and check_password_hash(user['password'], password):
            user_obj = User(user)
            login_user(user_obj)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.', 'danger')
    
    return render_template('auth.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        if password != confirm_password:
            flash('Passwords do not match!', 'danger')
            return redirect(url_for('auth.register'))
        
        if db.users.find_one({'username': username}):
            flash('Username already exists!', 'danger')
            return redirect(url_for('auth.register'))
        
        if db.users.find_one({'email': email}):
            flash('Email already registered!', 'danger')
            return redirect(url_for('auth.register'))
        
        hashed_password = generate_password_hash(password)
        user_id = ObjectId()
        
        db.users.insert_one({
            '_id': user_id,
            'username': username,
            'email': email,
            'password': hashed_password
        })
        
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('auth.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('index'))