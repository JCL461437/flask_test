import flask

app = flask.Flask(__name__)

# Basic games index
@app.route('/games', methods=["GET"])
def games_index(): 
    return "Games"

# Route with query parameters
@app.route('/games/query', methods=["GET"])
def games_index_query(): 
    query = flask.request.args  # returns query parameters as a dictionary
    return f"Query params: {query}"

# Dynamic route for games by name
@app.route('/games/<name>', methods=["GET"])
def games_show_dynamic(name): 
    return f"Game: {name}"

# Route with cookies
@app.route('/games/cookies/<name>', methods=["GET"])
def games_show_cookies(name): 
    cookies = flask.request.cookies
    res = flask.make_response(f"Hello {name}")
    res.headers['Content-type'] = 'text/plain'
    res.set_cookie('subscribed', 'true')  # set a cookie
    return res

# Route for sending a file (static image)
@app.route('/static_game_image', methods=["GET"])
def games_show_image(): 
    return flask.send_file("static/with_fren_emies_logo.jpeg")

# Loading a template
@app.route('/<path>')
def home(path):
    return flask.render_template("index.html", path=path)

# Start the app
app.run(debug=True)
