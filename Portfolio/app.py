from flask import Flask, request, render_template, url_for, redirect
import smtplib 
from email.message import EmailMessage

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sendemail/', methods = ['POST'])
def sendemail():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        
        if not all ([name, email, subject, message]):
            return render_template("index.html", error = 'All fields are required!')
        
        # set credentials
        email = 'muhammadfaizanlite@gmail.com'
        password = 'Kicksoffgoogle@1010'
   
        # sender and receiver
        msg = EmailMessage()
        msg['To'] = "moeizarshad378@gmail.com"
        msg['From'] = "muhammadfaizanlite@gmail.com"
        msg['subject'] = "For Another Flask Purpose"
        msg.set_content("First Name: " + str(name)
                      + "\nEmail: " + str(email)
                      + "\nSubject: " + str(subject)
                      + "\nMessage: " + str(message))
        
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.ehlo() # identify your server to Gmail SMTP server
                server.starttls()
                server.login(email, password)
                server.send_message(msg)
                server.quit()
                
            return request(url_for('index'))
               
        except Exception as e:
            return f'Failed to send email: {str(e)}', 500
        
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug = True)