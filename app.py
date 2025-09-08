from flask import Flask, request
app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello World!'

@app.route("/user/<username>")
def user(username):
    return f"user{username}"

if __name__ == '__main__':
    app.run(debug=True)#디버그 모드, 실제운영시엔 비활성화