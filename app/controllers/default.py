from app import app

@app.route('/')
def echo():
    return 'Ola mundo'