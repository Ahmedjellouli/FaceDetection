import time
import cv2
import dlib
from moviepy.editor import *
import screeninfo

class Image:
        def __init__(self,detectors, Image, Path, Save = False):
            self.Image = Path + Image
            self.detectors = detectors
            self.Path  = Path
            self.Save = Save

        def detectFaces(self):
            print(self.Image)
            self.Image = cv2.imread(self.Image, cv2.IMREAD_UNCHANGED)
            self.__resize()
            self.detectors.frame = self.Image
            self.Image = self.detectors.FrontalFace()
            self.Image = self.detectors.eyes()
            self.Image = self.detectors.landmarks()
            cv2.imshow('Faces in this image', self.Image)

            if self.Save:
                cv2.imwrite('Faces in this image.png', self.Image)
            cv2.waitKey(0)
        def __resize(self  ):
            screen = screeninfo.get_monitors()[0]
            Imgwidth = self.Image.shape[1]
            print(Imgwidth)

            screenwidth, screenheight = screen.width-100, screen.height-100
            print(screenwidth,screenheight)
            if Imgwidth>screenwidth:
                fx = screenwidth / Imgwidth
                self.Image = cv2.resize(self.Image, None, fx=fx, fy=fx, interpolation = cv2.INTER_CUBIC)
            Imgheight = self.Image.shape[0]
            print(Imgheight)
            if  Imgheight> screenheight:
                fx = screenheight / Imgheight
                self.Image = cv2.resize(self.Image, None, fx=fx, fy=fx, interpolation=cv2.INTER_CUBIC)
            print(self.Image.shape)


        


class detectInVideo:
    def __init__(self, detectors, Path,  Video  ):
        self.Path = Path
        self.Video = Path + Video
        self.VideoDst = Path +"[Face detected] " + Video
        self.detectors = detectors



    def detectFaces(self):
        videoCapture = cv2.VideoCapture(self.Video)
        fps = videoCapture.get(cv2.CAP_PROP_FPS)
        size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        print("size = ", size)
        videoWriter = cv2.VideoWriter(self.VideoDst , cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
        print("fps = ", fps)
        success, self.frame = videoCapture.read()
        length = int(videoCapture.get(cv2.CAP_PROP_FRAME_COUNT))
        print("length = ",length)
        FrameCount = 0
        oldProcessValue = 0
        bars = ""
        InitTime = time.time()
        while success:  # Loop until there are no more frames.
            self.detectors.frame = self.frame
            self.frame =  self.detectors.FrontalFace()
            self.frame = self.detectors.eyes()
            self.frame = self.detectors.landmarks()
            videoWriter.write(self.frame )
            success, self.frame  = videoCapture.read()
            FrameCount += 1


            process = 100 + ((FrameCount - length) / length) * 100


            if int(process) != oldProcessValue:
                oldProcessValue = int(process)
                Fps = float(FrameCount / ( time.time()-InitTime ))
                estimateTime= (length-FrameCount)/Fps
                h = int(estimateTime / (60 * 60))
                min = int((estimateTime - 60 * 60 * h) / 60)
                s = (estimateTime - min * 60 - h * 60 * 60)

                Fps = "{:.2f}".format(Fps)
                bars = bars + "|"
                sys.stdout.write('\r ' + "%02d" % (oldProcessValue,) +"%"  )
                print(bars + " "*(100-oldProcessValue)  + "| [" +str(Fps) + "frame/s  " +"%02d" % (h,)+":"+"%02d" % (min,)+":"+"%02d" % (s,)+" ]", sep='', end='', flush=True)
        videoCapture.release()
        # self.AddAudio()


    def AddAudio(self):
        #extract Audio from original video
        video = VideoFileClip(os.path.join(self.Path, "", self.Video))
        video.audio.write_audiofile(os.path.join(self.Path, "", "sound.mp3"))
        print(self.VideoDst)

        videoclip = VideoFileClip(self.VideoDst)
        audioclip = AudioFileClip(self.Path +"sound.mp3")


        videoclip.audio = CompositeAudioClip([audioclip])
        videoFile = str(self.VideoDst).lower()
        videoFile = videoFile.replace(".mp4","1.mp4")
        videoclip.write_videofile(videoFile)


class detectors:

     def __init__(self , frame, detectFFace =False, detectEyes= False ,detectLandmarks= False ):
         self.detectFFace = detectFFace
         self.detectEyes  = detectEyes
         self.detectLandmarks  =detectLandmarks
         self.detector = dlib.get_frontal_face_detector()
         # Load the predictor
         self.predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

         self.frame = frame


     def FrontalFace(self):

         if self.detectFFace:
             face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
             self.drawRectagle(face_cascade)
         return self.frame


     def eyes(self):
         if self.detectEyes:
            face_cascade = cv2.CascadeClassifier('cascades/haarcascade_eye.xml')
            self.drawRectagle(face_cascade)
         return self.frame

     def landmarks(self):
         if self.detectLandmarks:



             # Convert image into grayscale
             gray = cv2.cvtColor(src= self.frame, code=cv2.COLOR_BGR2GRAY)

             # Use detector to find landmarks
             Rects = self.detector(gray)

             for Rect in Rects:
                 x1 = Rect.left()  # left point
                 y1 = Rect.top()  # top point
                 x2 = Rect.right()  # right point
                 y2 = Rect.bottom()  # bottom point

                 for Point in range(1, 68):
                     landmarks = self.predictor(image=gray, box=Rect)
                     x = landmarks.part(Point).x
                     y = landmarks.part(Point).y

                     # cv2.rectangle(img ,(x1,y1), (x2,y2) , color= (255,255,255) ,thickness=1 )
                     cv2.circle( self.frame, (x, y), 0, (150, 150, 28), 3)
         return self.frame

     def drawRectagle(self,face_cascade ):
         gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
         faces = face_cascade.detectMultiScale(gray, 1.3, 5)
         for (x, y, w, h) in faces:
             self.frame = cv2.rectangle(self.frame, (x, y), (x + w, y + h), (150, 150, 28), 1)



