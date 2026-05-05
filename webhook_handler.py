from flask import Flask, request, jsonify
import config
import hmac
import hashlib
from database import add_user
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    signature = request.headers.get('X-Razorpay-Signature')
    
    # Simple Signature Verification (Pseudo-code for brevity)
    # verify_signature(data, signature, config.RZP_WEBHOOK_SECRET)
    
    if data['event'] == 'subscription.charged':
        u_id = data['payload']['subscription']['entity']['notes']['user_id']
        plan = data['payload']['subscription']['entity']['plan_id']
        # Logic to add user to DB
        add_user(int(u_id), "Monthly", datetime.now() + timedelta(days=30), "SUB_ID")
        
    return jsonify({"status": "ok"}), 200

def start_webhook():
    app.run(host='0.0.0.0', port=10000)
