from flask import Flask, render_template, request
import random 

price = 500

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/bestilling")
def bestilling():
    return render_template('bestilling.html')

@app.route("/om_oss")
def om_oss():
    return render_template('om_oss.html')

@app.route("/index")
def home():
    return render_template('index.html')

@app.route("/valg")
def valg():
    countries = ["Japan", "Norge", "Tyskland", "Slovenia", "USA", "Australia"]
    destination = request.args.get("destination")
    return render_template("valg.html", destination=destination, countries=countries)


@app.route("/sendt", methods=["POST", "GET"])
def sendt():
    destination = request.form.get("destination")
    days = int(request.form.get("days"))
    depart = request.form.get("depart")
    email = request.form.get("email")
    insurance = request.form.get("insurance")
    idNum = random.randint(1, 999)
    
    totalprice = price * days

    return render_template("sendt.html", destination=destination, days=days, email=email, insurance=insurance, depart=depart, idNum=idNum, totalprice=totalprice)



if __name__ == "__main__":
    app.run(debug=True)