from flask import Flask, render_template, request           
from sendemail import send_email
import git

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('./anandudagatti/MS_Constructions')
        origin = repo.remotes.origin
        repo.create_head('master', 
    origin.refs.master).set_tracking_branch(origin.refs.master).checkout()
        origin.pull()
        return '', 200
    else:
        return '', 400

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
      result = request.form
      subject ='New Customer Contact Info'
      to_list = "automail.msconstructions@gmail.com"
      cust_email = ''
      cust_name = ''
      msg =''
      for key, value in result.items():
        msg = msg + '\n' + '{} : {}'.format(key, value)
        if(key=='Email'):
          cust_email=value

        if(key=='Name'):
          cust_name=value

      send_email.send_email(to_list,subject,msg)
      print(msg)    

      subject ='Auto Mail MS Constructions'
      msg ='Hi ' + cust_name + ',' + '\n\n' + 'Thank you for Contacting MS Constructions.' + '\n' + 'Our Team will get back to you soon.'  + '\n\n' + 'Regards,' + '\n' + 'MS Constructions'

      send_email.send_email(cust_email,subject,msg)
      print(msg)    
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
