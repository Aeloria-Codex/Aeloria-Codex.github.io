from flask import Flask, render_template, request, jsonify, make_response
from flask_frozen import Freezer
from flask_session import Session
import os, requests, base64

app = Flask(__name__, 
            static_url_path='',
            static_folder='static',
            template_folder='templates')

app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['FREEZER_DESTINATION'] = 'docs'
app.config['SESSION_TYPE'] = 'filesystem'
freezer = Freezer(app)
Session(app)

# Home page
@app.route('/')
def index():
    mode = request.cookies.get('mode', 'light-mode')
    return render_template('index.html', mode=mode)

# Crafter Leveling page
@app.route('/crafter-leveling.html') 
def crafter_leveling():
    return render_template('crafter-leveling.html')

@app.route('/toggle-mode', methods=['POST'])
def toggle_mode():
    current_mode = request.cookies.get('mode', 'light-mode')
    new_mode = 'dark-mode' if current_mode == 'light-mode' else 'light-mode'
    
    response = make_response({'mode': new_mode})
    response.set_cookie('mode', new_mode, max_age=30*24*60*60)  # 30 days
    return response

# 404 page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    freezer.freeze()
    app.run(debug=True)
