#!/usr/bin/env python3
"""
Sunrise Intelligence — Windsor.ai Proxy Backend
Runs on Railway or localhost:5000
Solves CORS issues by proxying API calls to Windsor.ai
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Read API key from environment
WINDSOR_API_KEY = os.getenv('WINDSOR_API_KEY')
WINDSOR_BASE_URL = "https://api.windsor.ai/v1"

if not WINDSOR_API_KEY:
    print("⚠️  WINDSOR_API_KEY not found in environment")
    print("   Set it in Railway environment variables")

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'ok',
        'windsor_configured': WINDSOR_API_KEY is not None
    })

@app.route('/api/windsor/data', methods=['GET'])
def windsor_data():
    """
    Proxy endpoint for Windsor.ai data
    Query params: connector, account_id, fields, date_preset
    """
    
    if not WINDSOR_API_KEY:
        return jsonify({'error': 'Windsor API key not configured'}), 500
    
    try:
        # Get params from query string
        connector = request.args.get('connector')
        account_id = request.args.get('account_id')
        fields = request.args.get('fields', '').split(',')
        date_preset = request.args.get('date_preset', 'last_30d')
        
        if not connector or not account_id:
            return jsonify({'error': 'Missing connector or account_id'}), 400
        
        # Call Windsor.ai API
        url = f"{WINDSOR_BASE_URL}/data"
        headers = {
            'Authorization': f'Bearer {WINDSOR_API_KEY}',
            'Content-Type': 'application/json'
        }
        
        params = {
            'connector': connector,
            'account_id': account_id,
            'fields': ','.join(fields),
            'date_preset': date_preset
        }
        
        response = requests.get(url, headers=headers, params=params, timeout=10)
        
        if response.status_code != 200:
            return jsonify({
                'error': f'Windsor API error: {response.status_code}',
                'details': response.text
            }), response.status_code
        
        return jsonify(response.json())
    
    except requests.exceptions.Timeout:
        return jsonify({'error': 'Windsor API timeout'}), 504
    except requests.exceptions.ConnectionError:
        return jsonify({'error': 'Connection error to Windsor API'}), 503
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/windsor/connectors', methods=['GET'])
def windsor_connectors():
    """
    Get available Windsor.ai connectors
    """
    if not WINDSOR_API_KEY:
        return jsonify({'error': 'Windsor API key not configured'}), 500
    
    try:
        url = f"{WINDSOR_BASE_URL}/connectors"
        headers = {
            'Authorization': f'Bearer {WINDSOR_API_KEY}',
            'Content-Type': 'application/json'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code != 200:
            return jsonify({'error': f'Windsor API error: {response.status_code}'}), response.status_code
        
        return jsonify(response.json())
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Get port from environment (Railway sets PORT)
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', False)
    
    print("🌅 Sunrise Intelligence — Windsor.ai Proxy Backend")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"✓ Running on port {port}")
    print(f"✓ Windsor API Key configured: {bool(WINDSOR_API_KEY)}")
    print()
    
    app.run(debug=debug, host='0.0.0.0', port=port)

