from flask import Flask, request, jsonify
from datetime import datetime
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/ivr", methods=["GET", "POST"])
def ivr_entry():
    data = request.args.to_dict()
    logging.info(f"🔔 קריאה התקבלה: {data}")

    phone = data.get("PBXphone")
    extension = data.get("PBXextensionId")
    main_menu_choice = data.get("mainMenu")  # האם מדובר בהקשה מהתפריט?

    # שלב 1: בדיקה אם למאזין יש מנוי
    if not is_active_user(phone):
        return jsonify({
            "type": "extensionChange",
            "extensionIdChange": "200"  # שלוחת הצטרפות
        })

    # שלב 2: אם אין הקשה, שלח תפריט
    if not main_menu_choice:
        return jsonify(get_main_menu())

    # שלב 3: ניתוב לפי ההקשה שבוצעה
    return jsonify(route_main_menu_choice(main_menu_choice))


# תפריט ראשי למנויים
def get_main_menu():
    return {
        "type": "simpleMenu",
        "name": "mainMenu",  # ישלח חזרה עם ההקשה
        "times": 3,
        "timeout": 5,
        "enabledKeys": "1,2,3,4,5,6,7,8",
        "files": [
            {
                "text": "נא בחר שלוחה"
            }
        ]
    }


# פונקציה שמחזירה JSON לפי ההקשה מהמאזין
def route_main_menu_choice(choice):
    if choice == "1":
        return {
            "type": "extensionChange",
            "extensionIdChange": "101"  # שלוחת הנפקת קבלה
        }
    elif choice == "2":
        return {
            "type": "extensionChange",
            "extensionIdChange": "102"  # שלוחת ביטול קבלה
        }
    elif choice == "3":
        return {
            "type": "extensionChange",
            "extensionIdChange": "103"  # עדכון פרטים
        }
    elif choice == "4":
        return {
            "type": "extensionChange",
            "extensionIdChange": "104"  # שמיעת זכויות
        }
    elif choice == "5":
        return {
            "type": "extensionChange",
            "extensionIdChange": "105"  # השארת הודעה
        }
    elif choice == "6":
        return {
            "type": "extensionChange",
            "extensionIdChange": "106"  # בקשת דיווח שנתי
        }
    else:
        return {
            "type": "extensionChange",
            "extensionIdChange": ".."  # חזרה אחורה אם הקשה לא חוקית
        }


# הדמיה של בדיקת מנוי פעיל
def is_active_user(phone):
    active_numbers = ["0501234567", "0507654321"]
    return phone in active_numbers


if __name__ == "__main__":
    app.run(debug=True, port=5000)
