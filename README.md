# Detect Faces in video or image easily 
![](Faces/Dev Patel.jpg)

after all import those librarys:
        # time
        # cv2
        # dlib
        # moviepy
        # screeninfo

1 - put in path video/image the directory where your Video/image exist
2 - choose what you want to detect in your video/image in detectors class
        # detectFFace = True or false
        # detectEyes= True or false
        # detectLandmarks= True or false
        
3 - put your video/image name correctly
        # ... .mp4
        # ... .jpg
3 - start detection with 
        # Image.detectFaces() : to detect faces in image
        # Video.detectFaces() : to detect faces in Video
        #Video.AddAudio()     : to add audio to Video after face detection


