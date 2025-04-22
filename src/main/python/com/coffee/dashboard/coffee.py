from flask import Blueprint, request, jsonify, flash, redirect, url_for
from flask_login import login_required, current_user
from datetime import datetime
from app import db

coffee = Blueprint('coffee', __name__)

@coffee.route('/add_coffee', methods=['POST'])
@login_required
def add_coffee():
    coffee_data = {
        'user_id': current_user.get_id(),
        'type': request.form.get('type'),
        'size': request.form.get('size'),
        'notes': request.form.get('notes'),
        'date': datetime.now()
    }
    
    db.coffee_records.insert_one(coffee_data)
    flash('Coffee entry added successfully!', 'success')
    return redirect(url_for('dashboard'))

@coffee.route('/get_coffee_stats')
@login_required
def get_coffee_stats():
    user_id = current_user.get_id()
    
    # Get daily consumption for the past week
    pipeline = [
        {'$match': {'user_id': user_id}},
        {'$group': {
            '_id': {'$dateToString': {'format': '%Y-%m-%d', 'date': '$date'}},
            'count': {'$sum': 1}
        }},
        {'$sort': {'_id': -1}},
        {'$limit': 7}
    ]
    daily_stats = list(db.coffee_records.aggregate(pipeline))
    
    # Get coffee type distribution
    pipeline = [
        {'$match': {'user_id': user_id}},
        {'$group': {
            '_id': '$type',
            'count': {'$sum': 1}
        }}
    ]
    type_stats = list(db.coffee_records.aggregate(pipeline))
    
    return jsonify({
        'daily_stats': daily_stats,
        'type_stats': type_stats
    })