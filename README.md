# Detect Faces in video or image easily 
![](Faces%20in%20this%20image.png)

### Prerequisites

after all make sure that you have already install the folowing librarys:

- opencv
```
pip install opencv-python
```
- dlib "Require Cmake"
```
pip install dlib
```
```
pip install cmake
```
- time
```
pip install time
```
- moviepy
```
pip install moviepy
```
- screeninfo
```
pip install screeninfo
```
### How to use this code

- put in "path" video/image the directory where your Video/image exist:

```
VideoPath ="D:\XX\XX\FaceDetection\Videos\\" #video folder path
ImagePath ="D:\xx\xx\FaceDetection\Faces\\" #Image folder path

``` 
- Fonctionnalities avaliable in this code:

``` 
        - detectFFace     = True or false to detect frontale face
        - detectEyes      = True or false to detect eyes
        - detectLandmarks = True or false to detect 68 landmarks 
``` 
        
- put your video/image name correctly:

        - ... .mp4
        - ... .jpg
- start detection with 
        - Image.detectFaces() : to detect faces in image
        - Video.detectFaces() : to detect faces in Video
        - Video.AddAudio()     : to add audio to Video after face detection


