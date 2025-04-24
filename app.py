from flask import Flask, render_template, request, jsonify, send_from_directory
import os
from flask_mail import Mail, Message

app = Flask(__name__, static_folder='static')

# Configure Flask-Mail
app.config.update(
    MAIL_SERVER='smtp.gmail.com',  # Change to your email provider
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='janmauricegotze@gmail.com',  # Change to your email
    MAIL_PASSWORD='yyga dowr eubc jnrk',     # Change to your app password
    MAIL_DEFAULT_SENDER=('Your Portfolio', 'janmauricegotze@gmail.com')
)

mail = Mail(app)

# Serve the static HTML files
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

# Handle all other static files
@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('static', path)

# Handle contact form submissions
@app.route('/send-email', methods=['POST'])
def send_email():
    try:
        data = request.get_json()
        name = data.get('name', '')
        email = data.get('email', '')
        message_content = data.get('message', '')
        
        # Input validation
        if not name or not email or not message_content:
            return jsonify({'success': False, 'message': 'All fields are required'}), 400
            
        # Create email message
        msg = Message(
            subject=f"Portfolio Contact: {name}",
            recipients=['coc.acc.ascalter@gmail.com'],  # Where you want to receive messages
            body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message_content}",
            reply_to=email
        )
        
        # Send email
        mail.send(msg)
        
        return jsonify({'success': True, 'message': 'Message sent successfully!'})
    except Exception as e:
        print(f"Error sending email: {e}")
        return jsonify({'success': False, 'message': 'Failed to send message'}), 500

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
