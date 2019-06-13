from flask import Flask, render_template, request           
from sendemail import send_email

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/", methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
      result = request.form
      subject ='Test Subject'
      to_list = "automail.mscontructions@gmail.com"
      msg =''
      for key, value in result.items():
        msg = msg + '\n' + '{} : {}'.format(key, value)
      send_email.send_email(to_list,subject,msg)
      print(msg)
    return render_template("home.html",result = result)

if __name__ == "__main__":
    app.run(debug=True)