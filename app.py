from flask import Flask, render_template
import requests, schedule

app= Flask(__name__)

def indo():
    api_url = "https://api.kawalcorona.com/indonesia"
    rstl = requests.get(api_url).json()
    return rstl

def jawabarat():
    api_url = "https://api.kawalcorona.com/indonesia/provinsi/"
    rstl = requests.get(api_url).json()
    cek = rstl[1]
    ambil_disc = cek ["attributes"]
    a = [ambil_disc]
    return a

r_indo=schedule.every(2).seconds.do(indo)
r_jawabarat=schedule.every(2).seconds.do(jawabarat)

data_indo=indo()
data_jawabarat=jawabarat()


@app.route("/")
def index():
    return render_template("index.html", data_indo=data_indo, data_jawabarat=data_jawabarat)

if __name__=="__main__":
    app.run(debug=True)