"""
facial_recog.py
===============

Acknowledgement
Code was adapted from TutLab 9 01_capture.py, 02_encode.py, and 03_recognise.py
which in turn was adapted from
https://www.hackster.io/mjrobot/real-time-face-recognition-an-end-to-end-project-a10826
and
https://www.pyimagesearch.com/2018/06/18/face-recognition-with-opencv-python-and-deep-learning/
"""
import time
import os
import pickle
import cv2
import imutils
from imutils import paths
from imutils.video import VideoStream
import face_recognition


class FacialRecog():
    """
    Handles taking pictures, encoding them and recognising known people
    """
    def __init__(self):
        self.face_detector = cv2.CascadeClassifier(
            './framework/reception/haarcascade_frontalface_default.xml')

    def capture_photo(self, username):
        """Captures a photo"""
        folder = './dataset/{}'.format(username)
        if not os.path.exists(folder):
            os.makedirs(folder)
        # Start the camera
        cam = cv2.VideoCapture(0)
        # Set video width
        cam.set(3, 640)
        # Set video height
        cam.set(4, 480)
        # Get the pre-built classifier that had been trained on 3 million faces

        img_counter = 0
        while img_counter <= 10:
            key = input('Press q to stop or ENTER to continue: ')
            if key == 'q':
                break

            ret, frame = cam.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_detector.detectMultiScale(gray, 1.3, 5)

            if len(faces) == 0:
                print('No face detected, please try again')
                continue

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                img_name = '{}/{:04}.jpg'.format(folder, img_counter)
                cv2.imwrite(img_name, frame[y: y + h, x: x + w])
                print('{} written!'.format(img_name))
                img_counter += 1

        cam.release()

    def encode(self):
        """Encodes the dataset into a pickled dataset"""
        image_paths = list(paths.list_images('dataset'))

        # initialize the list of known encodings and known names
        known_encodings = []
        known_names = []

        # loop over the image paths
        for (i, image_path) in enumerate(image_paths):
            # extract the person name from the image path
            print("[INFO] processing image {}/{}".format(
                i + 1, len(image_paths)))
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
                # add each encoding + name to our set of known names
                # and encodings
                known_encodings.append(encoding)
                known_names.append(name)

        # dump the facial encodings + names to disk
        print("[INFO] serializing encodings...")
        data = {"encodings": known_encodings, "names": known_names}

        with open('encodings.pickle', "wb") as file:
            file.write(pickle.dumps(data))

    def facial_recog_login(self, state, login):
        """
        Constantly searches for a known face
        """
        # load the known faces and embeddings
        # print('[INFO] loading encodings...')

        while not os.path.isfile('encodings.pickle'):
            time.sleep(3.0)

        data = pickle.loads(open('encodings.pickle', 'rb').read())

        # initialize the video stream and then allow the
        # camera sensor to warm up
        print('[INFO] starting video stream...')
        video_stream = VideoStream(src=0).start()
        time.sleep(2.0)

        # loop over frames from the video file stream
        while True:
            # grab the frame from the threaded video stream
            if state.is_logged_in():
                time.sleep(3.0)
                continue

            frame = video_stream.read()

            # convert the input frame from BGR to RGB then resize it to have
            # a width of 750px (to speedup processing)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            rgb = imutils.resize(frame, width=240)

            # detect the (x, y)-coordinates of the bounding boxes
            # corresponding to each face in the input frame, then compute
            # the facial embeddings for each face
            boxes = face_recognition.face_locations(rgb, model='hog')
            encodings = face_recognition.face_encodings(rgb, boxes)
            names = []

            # loop over the facial embeddings
            for encoding in encodings:
                # attempt to match each face in the input image to our known
                # encodings
                matches = face_recognition.compare_faces(
                    data['encodings'], encoding)
                name = 'Unknown'

                # check to see if we have found a match
                if True in matches:
                    # find the indexes of all matched faces then initialize a
                    # dictionary to count the total number of times each face
                    # was matched
                    matched_idxs = [i for (i, b) in enumerate(matches) if b]
                    counts = {}

                    # loop over the matched indexes and maintain a count for
                    # each recognized face face
                    for i in matched_idxs:
                        name = data['names'][i]
                        counts[name] = counts.get(name, 0) + 1

                    # determine the recognized face with the largest number
                    # of votes (note: in the event of an unlikely tie Python
                    # will select first entry in the dictionary)
                    name = max(counts, key=counts.get)

                # update the list of names
                names.append(name)

            # loop over the recognized faces
            for name in names:
                # print to console, identified person
                if name == 'Unknown':
                    continue

                login(name)
                # Set a flag to sleep the cam for fixed time
                time.sleep(3.0)

        # do a bit of cleanup
        video_stream.stop()
