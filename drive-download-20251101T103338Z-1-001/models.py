from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Message(db.Model):
	__tablename__ = 'messages'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	email = db.Column(db.String(120), nullable=False)
	subject = db.Column(db.String(150), nullable=False)
	message = db.Column(db.Text, nullable=False)
	date_sent = db.Column(db.DateTime, default=datetime.utcnow)

	def __repr__(self):
		return f"<Message {self.name} - {self.email}>"
