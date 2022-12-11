from repository.PersonRepository import db, ma

# Model
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(200), unique=True)
    user_name = db.Column(db.String(120))
    def __init__(self, id, image_url, user_name):
        self.id = id
        self.image_url = image_url
        self.user_name = user_name

# Person Schema
class PersonSchema(ma.Schema):
    class Meta:
        fields = ('id', 'image_url', 'user_name')


# Init schema
person_schema = PersonSchema()
persons_schema = PersonSchema(many=True)