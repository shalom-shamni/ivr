from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ivr', methods=['GET'])
def handle_ivr():
    # שליפת הפרמטרים מה-URL
    phone = request.args.get('PBXphone')
    pbx_num = request.args.get('PBXnum')
    pbx_did = request.args.get('PBXdid')
    call_id = request.args.get('PBXcallId')
    call_type = request.args.get('PBXcallType')
    call_status = request.args.get('PBXcallStatus')
    extension_id = request.args.get('PBXextensionId')
    extension_path = request.args.get('PBXextensionPath')
    client_data = request.args.get('dataGet')
    print(client_data)
    # כאן צריך להיות קוד שבודק בדאטהבייס האם המספר מופיע, ולדרוש סיסמה

    # במידה ויש סיסמה, יתבצע כאן אימות
    
    # כאן יהיה קוד שיפנה את המאזין לפונקציה המתאימה לפי הקשתו, או לחיבור אם איננו מנוי
    

    # הדפסתם ללוג (לבדיקה)
    print(f"שיחה מזוהה: {phone} | סטטוס: {call_status} | שלוחה: {extension_path}")

    # החזרת כל הפרטים כ־JSON
    return jsonify({
        "type": "getDTMF",
        "name": "dataGet",
        "max": 10,
        "min": 9,
        "timeout": 5,
        "skipKey": "#",
        "skipValue": "NO_VALUE",
        "confirmType": "digits",
        "setMusic": "yes",
        "files": [
            {
                "text": "ברוכים הבאים... מערכת עסק-קל לניהול עסק דרך הטלפון"
            }
        ]
    }
)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

