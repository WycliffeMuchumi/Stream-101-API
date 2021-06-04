from app import app


@app.route('/', methods=['GET'])
def videos():
    return 'Hello World, welcome to Stream-101-API!'