from main import app, db
from models import Fish


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
    fish = Fish(id=1, name="salmon", origin="Norway")
    db.session.add(fish)
    db.session.commit()
    return "fish created"