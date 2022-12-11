import logging
from flask import request, jsonify, make_response
import os
# import multiprocessing as mp
from models.Person import Person, person_schema, persons_schema
from service.FaceRecognizeService import find_matches_in_data_base, verify_images
from app import app
from repository.PersonRepository import db, ma
import logging

logging.basicConfig(format='%(asctime)s %(message)s',
                    filename='C:\FaceRecognizeLogs\logs\logs.log',
                    filemode='w',  # w - override logs
                    encoding='utf-8', level=logging.DEBUG)


# pool = mp.Pool(1)


# Create person
@app.route('/person', methods=['POST'])
def add_person():
    id = request.json['id']
    image_url = request.json['image_url']
    user_name = request.json['user_name']
    new_person = Person(id, image_url, user_name)
    db.session.add(new_person)
    db.session.commit()
    return person_schema.jsonify(new_person)

# Upload image
@app.route('/upload', methods=['POST'])
def upload_photo_to_data_base():
    logging.info("uploading started...")
    imageDataBase = request.files['image']
    user_id = request.form["user_id"]
    checkedPerson = Person.query.get(user_id)
    user_name = request.form["user_name"]
    if(checkedPerson is not None):
        return {"message": "User already uploaded"}
    image_url = os.path.join("C:\Images", imageDataBase.filename[0:9]) + ".jpg"
    imageDataBase.save(image_url)
    new_person = Person(user_id, image_url, user_name)
    if(os.path.exists(r"C:\Images\representations_vgg_face.pkl")):
        os.remove(r"C:\Images\representations_vgg_face.pkl")
    try:
        find_matches_in_data_base(image_url)
    except Exception as error:
        logging.info(error)
        return {"message": "Can't upload photo, please try again"}
    db.session.add(new_person)
    db.session.commit()
    logging.info("uploading finished")
    return {"message": "Photo saved successfully to data base"}


# Upload image to camera
@app.route('/camera', methods=['POST'])
def upload_photo_to_camera():
    logging.info("verification started...")
    imageCamera = request.files['image']
    imageCamera.save(os.path.join("C:\Camera", imageCamera.filename) + ".jpg")
    image_url = os.path.join("C:\Camera", imageCamera.filename + ".jpg")
    logging.info('%s  received camera image', image_url)
    result = find_matches_in_data_base(image_url)
    logging.info('%s  received matches ', result.shape[0])
    if (result.shape[0] > 0):
        matched = result.iloc[0].identity
        logging.info('match status %s', matched)
        verified = verify_images(image_url, matched)
        logging.info('verified status %s', verified)
    else:
        return {"message": "Matches not found"}
    if (verified):
        user_id = matched[10:][:9]
        logging.info('verified user id %s', user_id)
        checkedPerson = Person.query.get(user_id)
        userName = checkedPerson.user_name
        logging.info("verification finished")
        return {"verified": verified, "userName": userName}
    else:
        logging.info("verification finished")
        return {"message": "Matches not found"}

# Get all persons
@app.route('/persons', methods=['GET'])
def get_persons():
    all_persons = Person.query.all()
    result = persons_schema.dump(all_persons)
    return jsonify(result)

# Get single person
@app.route('/person/<id>', methods=['GET'])
def get_person(id):
    person = Person.query.get(id)
    if(person is None):
        error = make_response(
            jsonify({'message': 'Person with id ' + id + ' not found'}), 404)
        return error
    return person_schema.jsonify(person)
