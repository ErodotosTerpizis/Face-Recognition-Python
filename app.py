from appJar import gui
import numpy as np
import cv2
import os
from PIL import Image

import face_dataset
import face_training
import face_recogniser_blink

import json


class MyApplication():

    # Build the GUI
    def Prepare(self, app):
        # Form GUI
        app.setFont(16)
        app.setSize(400,400)
        app.setStopFunction(self.BeforeExit)

        app.setSticky("nws")
        app.setExpand("both")
        app.setStretch("both")


        app.addLabel("title","Facial Recognision Security System",0,0,3)
        app.setSticky("ew")

        #CLIENT DETAILS LABEL
        app.startLabelFrame("Client Details",10,0,3)
        app.setSticky("ew")
        app.addLabel("mess","Please enter your name and ID",0,0,3)
    
        app.addLabel("IDLab", "ID:", 1, 0)
        app.addEntry("ID", 1, 2,2)
        app.addLabel("userLab", "Username:", 2, 0)
        app.addEntry("username", 2, 2,2)
        app.stopLabelFrame()

        #BUTTONS
        app.setSticky("s")
        app.addButton("Collect",self.Collect,15,0)
        app.addButton("Train",self.Train,15,1)
        app.addButton("Recognise",self.Recognise,15,2)
        app.addLabel("owner", "Erodotos Terpizis", 18, 0,3)


        return app
        
    # Build and Start your application
    def Start(self):
        # Creates a UI
        app = gui()

        self.namelist={}
        self.namelist["people"]=[]

        # Run the prebuild method that adds items to the UI
        app = self.Prepare(app)

        # Make the app class-accesible
        self.app = app
        
        # Start appJar
        app.go()

    
    # Callback execute before quitting your app
    def BeforeExit(self):
        return self.app.yesNoBox("Confirm Exit", "Are you sure you want to exit the application?")
    
    
    def Collect(self):
        username = self.app.getEntry("username")
        id =int(self.app.getEntry("ID"))

        #append the details to the namelist
        self.namelist['people'].append({
            'id': id,
            'username': username
        })

        #collector module
        face_dataset.collect(id)
        self.app.infoBox("Note"," Please note that for the system to recognise the newly added faces the train buttton must be pressed before you attempt to recognise a person")


    def Train(self):
        #write the details to the file
        with open('clients.txt', 'w') as outfile:
            json.dump(self.namelist, outfile)
        
        #training module
        faces_trained = face_training.train()
        self.app.infoBox("Training Complete","[INFO] {0} faces trained.".format(faces_trained))

    def Recognise(self):
        #recogniser/blink detection module
        face_recogniser_blink.recognise()
       


# Run the application
# `python app.py`
if __name__ == '__main__':
    # Create an instance of your application
    App = MyApplication()
    # Start your app !
    App.Start()



