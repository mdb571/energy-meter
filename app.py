from flask import Flask, render_template as render,request
from twilio.rest import Client
from twilio import twiml
from dotenv import load_dotenv
import os
import requests
load_dotenv()

app = Flask(__name__)
ACCOUNT_SID=os.environ.get('ACCOUNT_SID')
AUTH_TOKEN=os.environ.get('AUTH_TOKEN')
client = Client('','')

@app.route('/')
def index():
    return render("index.html")

@app.route('/recharge')
def recharge():
    print("Recharge requested")
    amount = int(request.args.get('amount'))
    rupees=int(request.args.get('rupees'))
    phone='+91'+request.args.get('phone')
    rupees+=amount
    message = client.messages \
                    .create(
                        body="Energy Meter Balance Alert:\nYour energy meter has been recharged Rs:"+str(amount)+"\nTotal Balance:"+str(rupees)+"\nEelctricity Has Been Connected\nThank you",
                        from_='+15392245359', #use your twilio no here
                        to=phone, #use your verified phone no. here
                    )
    url='https://api.thingspeak.com/update?api_key=R3HL6661AHSHY2HY&field1='+str(rupees)
    requests.get(url)
    return("Recharge Succesfull")

@app.route('/alert')
def alert():
    print("Alert Send")
    message = client.messages \
                    .create(
                        body="Your connection has been cut due to low balance. Please recharge immediately to restore connection.",
                        from_='+15392245359', #use your twilio no here
                        to='+918606068522', #use your verified phone no. here
                    )
    return("Alert Sent")
if __name__ == "__main__":
    app.run(debug=False)



