from flask import Flask, request

app = Flask(__name__)


@app.route('/')      # argument / means main page of app
def index():
    # print(request.headers)   # request is a global object
    # print(f' method: {request.method}')
    # print(f' method: {request.path}')
    # print(f' method: {request.url}')
    # print(request.headers['Authorization'])
    # print(request.headers['Content-Type'])
    # print(request.json)
    # print(request.json['name'])
    # print(request.json.get('name'))


    return 'Hello from Flask!!!!!'

if __name__ == '__main__':
    app.run(debug=True)  # run app    # debuy = True -> auto restart after any change, more info about errors

