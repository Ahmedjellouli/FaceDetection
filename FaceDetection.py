import cv2
from Utils import *

# for more details on how to use this code see : https://github.com/Ahmedjellouli/FaceDetection


VideoPath ="D:\PythonApp\OpenCV\FaceDetection\Videos\\" #video folder path
ImagePath ="D:\PythonApp\OpenCV\FaceDetection\Faces\\" #Image folder path



Video = detectInVideo(detectors = detectors(frame=None , detectFFace=False , detectEyes=False ,detectLandmarks=True),
                      Path = VideoPath ,
                      Video = "... .mp4"  # put your Video name Video.mp4

                      )

Image = Image(detectors = detectors(frame=None ,  detectFFace=True , detectEyes=True ,detectLandmarks=True ),
              Path=ImagePath ,
              Image = "Dev Patel.png" ,  # put your image path here e.g : D:\image.jpg
              Save = True
              )
Image.detectFaces()   #to detect faces in image
# Video.detectFaces()  #to detect faces in Video
# Video.AddAudio()     #to add audio to faces after face detection

