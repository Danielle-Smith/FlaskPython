from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

subscribers = []

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/subscribe')
def subscribe():
  return render_template('subscribe.html')

@app.route('/form', methods=["POST"])
def form():
  first_name = request.form.get("first_name")
  last_name = request.form.get("last_name")
  email = request.form.get("email")

  if not first_name or not last_name or not email: 
    error_statement = "All Form Fields Required..."
    return render_template("subscribe.html", 
      error_statement=error_statement, 
      subscribers=subscribers, 
      first_name=first_name, 
      last_name=last_name, 
      email=email)

  message = "You have been subscribed to my email newsletter"
  server = smtplib.SMTP("smtp.gmail.com", 587)
  server.starttls()
  server.login("danielle@natesdesign.com", "PASWORD")
  server.sendmail("danielle@natesdesign.com", email, message)

  subscribers.append(f"{first_name} {last_name} | {email}")
  return render_template('form.html', subscribers=subscribers)

if __name__ == '__main__':
    app.run(debug=True)