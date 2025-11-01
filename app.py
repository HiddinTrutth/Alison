from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message as MailMessage
from models import db, Message

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# -------------------------------
# Database Configuration
# -------------------------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# -------------------------------
# Flask-Mail Configuration
# -------------------------------
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'alisonrhesterlpc@gmail.com'        # replace with your Gmail
app.config['MAIL_PASSWORD'] = 'bkrqtwusstcmmnui'     # Gmail App Password (not your normal one)
app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_USERNAME']

mail = Mail(app)
# -------------------------------

# -------------------------------
# ROUTES
# -------------------------------
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route('/submit_contact', methods=['POST'])
def submit_contact():
	name = request.form['name']
	email = request.form['email']
	subject = request.form['subject']
	message = request.form['message']

	# Save to database
	new_message = Message(name=name, email=email, subject=subject, message=message)
	db.session.add(new_message)
	db.session.commit()

	# Send email
	mail_msg = MailMessage(
		subject=f'New Contact Form Submission: {subject}',
		sender=app.config['MAIL_USERNAME'],
		recipients=['alison@thrive-wc.com']
	)
	mail_msg.body = f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage:\n{message}"
	mail.send(mail_msg)

	flash('Your message has been sent successfully!', 'success')
	return redirect(url_for('thank_you'))


@app.route('/thank_you')
def thank_you():
	return render_template('thank_you.html')


# -------------------------------
# APP RUNNER
# -------------------------------
if __name__ == "__main__":
	app.run(debug=True)
