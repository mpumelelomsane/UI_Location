from flask import Flask, request, jsonify, render_template
import firebase_admin
from firebase_admin import credentials, auth
import requests
import os

from flask import Blueprint  # Correct import

# Define the Blueprint for login
login_bp = Blueprint("login", __name__)

# Firebase API key (found in your Firebase project settings)
API_KEY = os.getenv("FIREBASE_API_KEY")  # Preferably use environment variables

@login_bp.route('/login', methods=['POST'])
def login_user():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    try:
        login_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}"
        payload = {
            "email": email,
            "password": password,
            "returnSecureToken": True
        }

        response = requests.post(login_url, json=payload)
        response_data = response.json()

        if response.status_code == 200:
            id_token = response_data.get("idToken")
            return jsonify({"message": "Login successful", "idToken": id_token}), 200
        else:
            error_message = response_data.get("error", {}).get("message", "Unknown error occurred")
            return jsonify({"message": error_message}), 400

    except Exception as e:
        return jsonify({"message": str(e)}), 500



    
    


