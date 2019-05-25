"""
Acknowledgement
Code was adapted from TutLab 9 01_capture.py and 02_encode.py
which in turn was adapted from
https://www.hackster.io/mjrobot/real-time-face-recognition-an-end-to-end-project-a10826
and
https://www.pyimagesearch.com/2018/06/18/face-recognition-with-opencv-python-and-deep-learning/
"""
import os
import pickle
import cv2
from imutils import paths
import face_recognition


def capture_photo(username):
    folder = './dataset/{}'.format(username)
    # Start the camera
    cam = cv2.VideoCapture(0)
    # Set video width
    cam.set(3, 640)
    # Set video height
    cam.set(4, 480)
    # Get the pre-built classifier that had been trained on 3 million faces
    face_detector = cv2.CascadeClassifier(
        'haarcascade_frontalface_default.xml')

    img_counter = 0
    while img_counter <= 10:
        key = input('Press q to stop or ENTER to continue: ')
        if key == 'q':
            break

        ret, frame = cam.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        if not faces:
            print('No face detected, please try again')
            continue

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            img_name = '{}/{:04}.jpg'.format(folder, img_counter)
            cv2.imwrite(img_name, frame[y: y + h, x: x + w])
            print('{} written!'.format(img_name))
            img_counter += 1

    cam.release()


def encode():
    image_paths = list(paths.list_images('dataset'))

    # initialize the list of known encodings and known names
    known_encodings = []
    known_names = []

    # loop over the image paths
    for (i, image_path) in enumerate(image_paths):
        # extract the person name from the image path
        print("[INFO] processing image {}/{}".format(i + 1, len(image_paths)))
        name = image_path.split(os.path.sep)[-2]

        # load the input image and convert it from RGB (OpenCV ordering)
        # to dlib ordering (RGB)
        image = cv2.imread(image_path)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # detect the (x, y)-coordinates of the bounding boxes
        # corresponding to each face in the input image
        boxes = face_recognition.face_locations(
            rgb, model='hog')

        # compute the facial embedding for the face
        encodings = face_recognition.face_encodings(rgb, boxes)

        # loop over the encodings
        for encoding in encodings:
            # add each encoding + name to our set of known names and encodings
            known_encodings.append(encoding)
            known_names.append(name)

    # dump the facial encodings + names to disk
    print("[INFO] serializing encodings...")
    data = {"encodings": known_encodings, "names": known_names}

    with open('encodings.pickle', "wb") as file:
        file.write(pickle.dumps(data))
