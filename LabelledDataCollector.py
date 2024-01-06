import os 
import cv2
import time
import uuid

IMAGES_PATH = "TensorFlow/workspace/images/collectedimages"

labels = ["Hello", "Thank You", "Yes", "No", "Iloveyou"]

number_images = 6

for label in labels:
    os.makedirs("TensorFlow\workspace\images\collectedimages\\"+label, exist_ok=True)
    cap = cv2.VideoCapture(0)
    print("Collecting images for {}".format(label))
    time.sleep(5)
    for image_num in range(number_images):
        ret, frame = cap.read()
        image_name = os.path.join(IMAGES_PATH, label, label+"."+"{}.jpg".format(str(uuid.uuid1())))
        cv2.imwrite(image_name, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()