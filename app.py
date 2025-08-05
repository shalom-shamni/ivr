from flask import Flask, request

app = Flask(__name__)

@app.route('/hello', methods=['POST', 'GET'])
def hello():
    print("📥 קיבלתי בקשה מה-IVR")
    print("Headers:", dict(request.headers))
    print("Body:", request.data.decode())
    return "OK"

if __name__ == '__main__':
    app.run()
