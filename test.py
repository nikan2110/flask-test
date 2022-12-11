from deepface import DeepFace


image_data_base = r"C:\Images\346412612.jpg"
image_camera = r"C:\Camera\346412612.jpg"

# result = DeepFace.verify(img1_path = image_data_base, img2_path = image_camera)
# print(result['verified'])

# result = DeepFace.find(img_path=image_camera, db_path='C:\Images', detector_backend='retinaface')
# if result.shape[0] > 0:
#         print(result.iloc[0].identity)

test = "C:\Images/346412612.jpg"
print(test[10:][:9])