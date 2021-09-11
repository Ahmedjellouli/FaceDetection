import cv2
from Utils import *


VideoPath ="D:\PythonApp\OpenCV\FaceDetection\Videos\\" #video folder path
ImagePath ="D:\PythonApp\OpenCV\FaceDetection\Faces\\" #Image folder path

# choose what you want to detect in detectors class
        # detectFFace = True or false
        # detectEyes= True or false
        # detectLandmarks= True or false

Video = detectInVideo(detectors = detectors(frame=None , detectFFace=False , detectEyes=False ,detectLandmarks=True),
                      Path = VideoPath ,
                      Video = "... .mp4"  # put your Video name Video.mp4

                      )

Image = Image(detectors = detectors(frame=None , detectFFace=False , detectEyes=False ,detectLandmarks=True ),
              Path=ImagePath ,
              Image = "... .jpg"   # put your image path here e.g : D:\image.jpg
              )
Image.detectFaces()   #to detect faces in image
Video.detectFaces()  #to detect faces in Video
Video.AddAudio()     #to add audio to faces after face detection


















































# Video.detectFaces()   #to detect faces in video

# def detectImageFaces(Image):
#     img = cv2.imread(Image, cv2.IMREAD_UNCHANGED)
#     img = resize(img)
#     FrontalFace(img)
#     cv2.imshow('Faces in this image', img)
#
#     # cv2.imwrite('Faces in this image.jpg', img)
#     cv2.waitKey(0)

# def resize( img):
#     screen = screeninfo.get_monitors()[0]
#     Imgwidth = img.shape[1]
#     print(Imgwidth)
#
#     screenwidth, screenheight = screen.width - 100, screen.height - 100
#     print(screenwidth, screenheight)
#     if Imgwidth > screenwidth:
#         print("here")
#         fx = screenwidth / Imgwidth
#         img = cv2.resize(img, None, fx=fx, fy=fx, interpolation=cv2.INTER_CUBIC)
#     Imgheight = img.shape[0]
#     print(Imgheight)
#     if Imgheight > screenheight:
#         fx = screenheight / Imgheight
#         img = cv2.resize(img, None, fx=fx, fy=fx, interpolation=cv2.INTER_CUBIC)
#     print(img.shape)
#     return img
#
#
# def FrontalFace(frame):
#         face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#         for (x, y, w, h) in faces:
#             frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
#         return frame
#
# path = 'Faces\scientifiques.jpg'
# detectImageFaces(path)

#
# class classa :
#     def __init__(self, a ):
#          self.a = a(c=0, b = 2)
#
#
#     def bPlus(self):
#
#
#         # print(self.a.bPlus())
#         a = self.a.bPlus()
#
#         return self.a
#
#     def plus(self):
#         self.a += 1
#         return self.a
#
#
#
#
#
# class classb :
#
#     def __init__(self, b,c):
#          self.b= b
#          self.c = c
#
#     def bPlus(self):
#
#         self.b+=1
#         print(self.b)
#         return self.b
#
#     def plus(self):
#         self.b += 1
#         return self.b
#
# a = classa(a = classb)
# a.bPlus()
#

