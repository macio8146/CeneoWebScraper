from app import app 

@app.route('/')
@app.route('/index')
def index():
    return "Hello, Maciej Jastrzębski"


@app.route('/name/<name>')
def name(name):
    return f"Hello, {name}!"