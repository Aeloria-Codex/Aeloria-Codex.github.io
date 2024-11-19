from flask import Flask, render_template, request, make_response, url_for, jsonify
from flask_frozen import Freezer
from flask_session import Session
from flask_htmlmin import HTMLMIN
from flask_sslify import SSLify
import json, os, re

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')

app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['FREEZER_DESTINATION'] = 'docs'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['MINIFY_HTML'] = True
app.config['MINIFY_PAGE'] = True
freezer = Freezer(app)
Session(app)
HTMLMIN(app)
sslify = SSLify(app)

# Home page
@app.route('/')
def index():
    mode = request.cookies.get('mode', 'light-mode')
    return render_template('index.html', guides=GUIDES, mode=mode)

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

# References page
@app.route('/references.html')
def references():
    return render_template('references.html')

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

##################################################################################################################################
# Sitemap
##################################################################################################################################
@app.route('/sitemap.xml')
def sitemap():
    routes = [
        {'loc': url_for('index', _external=True)},
        {'loc': url_for('job_leveling', _external=True)},
        {'loc': url_for('crafter_leveling', _external=True)},
        {'loc': url_for('tank_pulling', _external=True)},
        {'loc': url_for('astrologian_leveling', _external=True)},
        {'loc': url_for('bard_leveling', _external=True)},
        {'loc': url_for('black_mage_leveling', _external=True)},
        {'loc': url_for('blue_mage_leveling', _external=True)},
        {'loc': url_for('dancer_leveling', _external=True)},
        {'loc': url_for('dark_knight_leveling', _external=True)},
        {'loc': url_for('dragoon_leveling', _external=True)},
        {'loc': url_for('gunbreaker_leveling', _external=True)},
        {'loc': url_for('machinist_leveling', _external=True)},
        {'loc': url_for('monk_leveling', _external=True)},
        {'loc': url_for('ninja_leveling', _external=True)},
        {'loc': url_for('paladin_leveling', _external=True)},
        {'loc': url_for('pictomancer_leveling', _external=True)},
        {'loc': url_for('reaper_leveling', _external=True)},
        {'loc': url_for('red_mage_leveling', _external=True)},
        {'loc': url_for('sage_leveling', _external=True)},
        {'loc': url_for('samurai_leveling', _external=True)},
        {'loc': url_for('scholar_leveling', _external=True)},
        {'loc': url_for('summoner_leveling', _external=True)},
        {'loc': url_for('viper_leveling', _external=True)},
        {'loc': url_for('warrior_leveling', _external=True)},
        {'loc': url_for('white_mage_leveling', _external=True)}
    ]
    response = make_response(render_template('sitemap.xml', urlset=routes))
    response.headers['Content-Type'] = 'application/xml'
    return response

##################################################################################################################################
# Auto Json
##################################################################################################################################
# Path to your rendered HTML files
html_files = [
    "templates/crafter-leveling.html",
    "templates/job-leveling.html",
    "templates/tank-pulling.html",
    "templates/job-leveling/astrologian-leveling.html",
    "templates/job-leveling/bard-leveling.html",
    "templates/job-leveling/black-mage-leveling.html",
    "templates/job-leveling/blue-mage-leveling.html",
    "templates/job-leveling/dancer-leveling.html",
    "templates/job-leveling/dark-knight-leveling.html",
    "templates/job-leveling/dragoon-leveling.html",
    "templates/job-leveling/gunbreaker-leveling.html",
    "templates/job-leveling/machinist-leveling.html",
    "templates/job-leveling/monk-leveling.html",
    "templates/job-leveling/paladin-leveling.html",
    "templates/job-leveling/ninja-leveling.html",
    "templates/job-leveling/pictomancer-leveling.html",
    "templates/job-leveling/reaper-leveling.html",
    "templates/job-leveling/red-mage-leveling.html",
    "templates/job-leveling/sage-leveling.html",
    "templates/job-leveling/samurai-leveling.html",
    "templates/job-leveling/scholar-leveling.html",
    "templates/job-leveling/summoner-leveling.html",
    "templates/job-leveling/viper-leveling.html",
    "templates/job-leveling/warrior-leveling.html",
    "templates/job-leveling/white-mage-leveling.html",
]

# Function to extract information from an HTML file
def extract_info(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # Extract title from block tag
        title_match = re.search(r'{%\s*block\s+title\s*%}(.*?){%\s*endblock\s*%}', content)
        title = title_match.group(1).strip() if title_match else 'Untitled'
        
        description_match = re.search(r'{%\s*block\s+description\s*%}(.*?){%\s*endblock\s*%}', content)
        description = description_match.group(1).strip() if title_match else 'Untitled'
        
        keywords_match = re.search(r'{%\s*block\s+keywords\s*%}(.*?){%\s*endblock\s*%}', content)
        keywords = keywords_match.group(1).strip() if title_match else 'Untitled'
        
        # Generate the URL based on file name or template logic
        url = f"/{os.path.basename(file_path)}"
        
        return {
            "id": str(html_files.index(file_path) + 1),  # Simple ID based on index
            "title": title,
            "description": description[:500],
            "keywords": keywords,
            "url": url
        }

# List to hold all the search data
search_data = []

# Loop through all HTML files and extract info
for html_file in html_files:
    search_data.append(extract_info(html_file))

# Save the JSON to a file
with open('search.json', 'w', encoding='utf-8') as json_file:
    json.dump(search_data, json_file, indent=2)

##################################################################################################################################
# Search
##################################################################################################################################

with open('search.json', 'r', encoding='utf-8') as file:
    GUIDES = json.load(file)

@app.route('/search')
def search():
    # This route will return search results as JSON
    return jsonify(GUIDES)

if __name__ == '__main__':
    freezer.freeze()
    app.run(debug=True)