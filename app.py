from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from utils import fetch_reply

app = Flask(__name__)   #this is used to make flask class object

@app.route("/")   #run this function if this url is called
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    print(request.form)
    msg = request.form.get('Body')
    sender = request.form.get("From")

    # Create reply
    text=''
    resp = MessagingResponse()
    text,reply=fetch_reply(msg,sender)
    if text=='dog':
        resp.message(reply).media(reply)
    else:
        resp.message(reply)

   
    return str(resp)
if __name__ == "__main__":
    app.run(debug=True)



