from rest_api import db
from hashlib import md5

class User(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	nickname=db.Column(db.String(64),nullable=False,unique=True)
	email=db.Column(db.String(120),nullable=True )
	password=db.Column(db.String(64))

	def get_id(self):
		try:
			return unicode(self.id)
		except NameError:
			return str(self.id)

	def __repr__(self):
		return '<User %r>' % (self.nickname)
