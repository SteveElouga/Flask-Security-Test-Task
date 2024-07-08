from flask import Blueprint, jsonify
from .extensions import app

views_bp = Blueprint("views", __name__)

@views_bp.get('/')
def get_view():
    return jsonify({
        "message":"Hello World!"
    })