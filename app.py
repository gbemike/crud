import os

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

'''
GET /api should return all persons/users
POST /api should create a new person
PUT /api/:userId should update a person
DELETE /api/:userId should delete a persons
'''
# Initialize app
app = Flask(__name__)

# Set up base directory
basedir = os.path.abspath(os.path.dirname(__file__))

# Set up database in the same directory as the Flask app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')

# Remove warning in console
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize DB
db = SQLAlchemy(app)

# Create person class
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120))
    track = db.Column(db.String(120))

    # Used the init constructor to initialize Person
    def __init__(self, username, track):
        self.username = username
        self.track = track

@app.route("/")
def home():
    return "Hello World"


# Route to get all persons
@app.route("/api", methods=["GET"])
def get_persons():
    persons = Person.query.all()
    persons_list = [{'id': person.id, 'username': person.username, 'track': person.track} for person in persons]
    return jsonify(persons_list)

# Route to create a new person
@app.route("/api", methods=["POST"])
def add_person():
    # Get data from JSON request
    data = request.json
    username = data.get('username')
    track = data.get('track')

    # Create a new person instance
    new_person = Person(username, track)

    # Add new person to the database 
    db.session.add(new_person)

    # Commit the change to the database
    db.session.commit()

    # Return a JSON response
    return jsonify({'id': new_person.id, 'username': new_person.username, 'track': new_person.track})

@app.route("/api/<int:id>", methods=["GET"])
def get_person(id):
    person = Person.query.get(id)
    person_data = {'id': person.id, 'username': person.username, 'track': person.track}
    return jsonify(person_data)

@app.route("/api/<int:id>", methods=["PUT"])
def update_person(id):
    # fetch product
    person = Person.query.get(id)
    # Get data from JSON request
    data = request.json
    new_username = data.get('username')
    new_track = data.get('track')
    # checks if username and track exist in json request data 
    if new_username:
        person.username = new_username
    if new_track:
        person.track = new_track
    
    db.session.commit()

    return jsonify({'message':'success'})

@app.route("/api/<int:id>", methods=["DELETE"])
def delete_person(id):
    person = Person.query.get(id)
        
    db.session.delete(person)
    db.session.commit()

    return jsonify({'message':'Deleted Successfully'})


if __name__ == '__main__':
    app.run(debug=True)
