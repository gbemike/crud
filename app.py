from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow
import os

# initialise app
app = Flask(__name__)
# set up base directory
basedir = os.path.abspath(os.path.dirname(__file__))
# set up database in same directory as flask app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
# removes warning in console
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# initialise DB
db = SQLAlchemy(app)
# initialise Marshmallow
ma = Marshmallow(app)

# create person class
class Person(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(120))
  track = db.Column(db.String(120))
  # used the init constructor to initialise Person
  def __init__(self, username, track):
    self.username = username
    self.track = track

# person schema
class PersonSchema(ma.Schema):
  class Meta:
    fields = ('id', 'username', 'track')

# initialise schema
person_schema = PersonSchema()
persons_schema = PersonSchema(many=True)

@app.route("/", methods = ["GET"])
def get_persons():
  return jsonify({'msg':'Hello World'})

# create new person
@app.route("/api", methods = ["POST"])
def add_person():
  # get username and track
  username = request.json('username')
  track = request.json('track')
  # get instance of new person
  new_person = Person(username, track)
  # add new person to db
  db.session.add(new_person)
  # make change to database
  db.session.commit()
  
  return person_schema.jsonify(new_person)

# run Server
if __name__ == '__main__':
  app.run(debug=True)