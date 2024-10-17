from flask import Flask, render_template, request, make_response
from flask_frozen import Freezer
from flask_session import Session
from flask_minify import minify
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
@app.route('/job-leveling.html')
def job_leveling():
    return render_template('job-leveling.html')

# Crafter Leveling page
@app.route('/crafter-leveling.html')
def crafter_leveling():
    return render_template('crafter-leveling.html')

# Crafter Leveling page
@app.route('/tank-pulling.html')
def tank_pulling():
    return render_template('tank-pulling.html')

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

##################################################################################################################################
# Job Leveling Routes
##################################################################################################################################

@app.route('/paladin-leveling.html')
def paladin_leveling():
    return render_template('job-leveling/paladin-leveling.html')
@app.route('/warrior-leveling.html')
def warrior_leveling():
    return render_template('job-leveling/warrior-leveling.html')
@app.route('/dark-knight-leveling.html')
def dark_knight_leveling():
    return render_template('job-leveling/dark-knight-leveling.html')
@app.route('/gunbreaker-leveling.html')
def gunbreaker_leveling():
    return render_template('job-leveling/gunbreaker-leveling.html')
@app.route('/white-mage-leveling.html')
def white_mage_leveling():
    return render_template('job-leveling/white-mage-leveling.html')
@app.route('/scholar-leveling.html')
def scholar_leveling():
    return render_template('job-leveling/scholar-leveling.html')
@app.route('/astrologian-leveling.html')
def astrologian_leveling():
    return render_template('job-leveling/astrologian-leveling.html')
@app.route('/sage-leveling.html')
def sage_leveling():
    return render_template('job-leveling/sage-leveling.html')
@app.route('/monk-leveling.html')
def monk_leveling():
    return render_template('job-leveling/monk-leveling.html')
@app.route('/dragoon-leveling.html')
def dragoon_leveling():
    return render_template('job-leveling/dragoon-leveling.html')
@app.route('/ninja-leveling.html')
def ninja_leveling():
    return render_template('job-leveling/ninja-leveling.html')
@app.route('/samurai-leveling.html')
def samurai_leveling():
    return render_template('job-leveling/samurai-leveling.html')
@app.route('/reaper-leveling.html')
def reaper_leveling():
    return render_template('job-leveling/reaper-leveling.html')
@app.route('/viper-leveling.html')
def viper_leveling():
    return render_template('job-leveling/viper-leveling.html')
@app.route('/bard-leveling.html')
def bard_leveling():
    return render_template('job-leveling/bard-leveling.html')
@app.route('/machinist-leveling.html')
def machinist_leveling():
    return render_template('job-leveling/machinist-leveling.html')
@app.route('/dancer-leveling.html')
def dancer_leveling():
    return render_template('job-leveling/dancer-leveling.html')
@app.route('/black-mage-leveling.html')
def black_mage_leveling():
    return render_template('job-leveling/black-mage-leveling.html')
@app.route('/summoner-leveling.html')
def summoner_leveling():
    return render_template('job-leveling/summoner-leveling.html')
@app.route('/red-mage-leveling.html')
def red_mage_leveling():
    return render_template('job-leveling/red-mage-leveling.html')
@app.route('/pictomancer-leveling.html')
def pictomancer_leveling():
    return render_template('job-leveling/pictomancer-leveling.html')
@app.route('/blue-mage-leveling.html')
def blue_mage_leveling():
    return render_template('job-leveling/blue-mage-leveling.html')


if __name__ == '__main__':
    freezer.freeze()
    app.run(debug=True)
