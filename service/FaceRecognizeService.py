from deepface import DeepFace
import logging

from utils.Constants import BACK_END_DETECTOR, BASE_URL_DATA_BASE_IMAGES, MODEL_NAME

logging.basicConfig(format='%(asctime)s %(message)s',
                    filename='C:\FaceRecognizeLogs\logs\logs.log',
                    filemode='w',  # w - override logs
                    encoding='utf-8', level=logging.DEBUG)

def verify_images(image_camera, image_data_base):
    logging.info('%s  received camera image', image_camera)
    logging.info('%s  received data base image', image_data_base)
    result = DeepFace.verify(img1_path=image_camera, img2_path=image_data_base, model_name=MODEL_NAME, enforce_detection=False)
    return result['verified']

def find_matches_in_data_base(image_camera):
    logging.info('%s  received camera image', image_camera)
    result = DeepFace.find(img_path=image_camera,
                           db_path=BASE_URL_DATA_BASE_IMAGES, model_name=MODEL_NAME, detector_backend=BACK_END_DETECTOR)
    return result
