# Facial Recognition Software

## Security system prototype/Liveness Detector
A facial recognition system build in Python with OpenCv, dlib. Capable of dataset collection, system training and real-time face recognition as well as liveness detection.Comes with a very simple GUI build in AppJar.

I came to this idea because a simple facial recognition software can surely identify a person, but cannot differentiate whether the person is actually there or if a photo of the person is shown. Hence I created a system that uses the fact that a photo cannot blink to tell whether the person is real or not.


## The software works in 3 phases:

### 1st Phase
Starting with the Collect button, we will simply create a dataset, where we will store for each id, a group of photos in gray with the portion that was used for face detecting. The user is promt to enter his id and username and a text file containing the details of clients is updated
### 2nd Phase
On this second phase, with the Train button we  take all user data from our dataset and "trainer" the OpenCV Recognizer. This is done directly by a specific OpenCV function. The result will be a .yml file that will be saved on a "trainer/" directory. Each face is matched with an id from the client.txt file
### 3rd Phase
 Here, we will capture a fresh face on our camera and if this person had his face captured and
 trained before, the recognizer will make a "prediction" returning its id and an index, shown how confident the recognizer is with this match.Also, using a dlib’s pre-trained facial landmark detector the system detects if the person blinks and hence concluding if the person is Real or a photo.

### Limitations

Of course the system is just a prototype and has a lot of limitations as well as plenty of room for improvements
- Due to my assumtpion that the liveness detector will be tested only in one person per time,as soon as the system concludes that a person is real, if a new person appears the system will still output a "Real" indicator.
- Furthermore, the recognition itself is not entirely accurate reaching most of the times up to 50% confidence for a person.

### Requirements
- OpenCV
- Dlib
- Imutils
- AppJar

### Screenshots

![Real examples](https://github.com/ErodotosTerpizis/Face-Recognition-Python-OpenCV-/Screnshot-real)
![Fake examples](https://github.com/ErodotosTerpizis/Face-Recognition-Python-OpenCV-/Screnshot-fake)
![GUI examples](https://github.com/ErodotosTerpizis/Face-Recognition-Python-OpenCV-/Screnshot-GUI)

