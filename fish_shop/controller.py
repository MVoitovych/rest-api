from main import app

@app.route('/')
def index():
    return "Hooray"

@app.route('/<id>')
def get_id(id):
    return id

@app.route("/fish", methods = ["GET"])
def get_fish():
    return "Get fish"

@app.route("/fish", methods = ["POST"])
def post_fish():
    return "Post fish"