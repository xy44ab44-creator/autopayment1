import os
from flask import Flask, request
from db import mark_paid

app = Flask(__name__)

@app.route("/cashfree-webhook", methods=["POST"])
def webhook():
    data = request.json
    print(data)

    if data.get("type") == "PAYMENT_SUCCESS_WEBHOOK":
        order_id = data["data"]["order"]["order_id"]
        mark_paid(order_id)

    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
