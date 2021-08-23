# KMottershead Peak Picking DL Model

This repository holds the webservice and deep learning model (Model E) created as part of the research paper Deep Learning in Mass Spectrometry Analysis by K Mottershead and T Miller (link).

The model is stored as a .h5 file: PeakPicking Model/MobileNetPTModel.h5

The licensing of this repository can be found in the LICENSE file.

This web service can be run locally, where test files (.png) can be uploaded and tested against the model. The will be assigned a probability of Peak, No Peak, and Further Investigation (FI). This README.md file describes how you can set this to run locally. 

# Prerequisites
(All instructions are given for a Windows machine, linux and Mac has not been tested with this webservice and instruction may vary slightly) 
1. python must be installed locally (https://www.python.org/downloads/) (python verison 3.8 was used in the creation of this Model and Web Service)
2. pip must be installed and upgraded (normally comes packaged as part of python, upgrade cmd line is below)

		pip install --upgrade pip
			
3. Tensorflow (and thus Keras) must be installed locally (cmd line below)

		pip install tensorflow

4. Flask must also be installed locally (cmd line below)

		pip install Flask
		
# Downloading the Repo
1. Download or Clone this repository locally to your C:/ drive 
2. Then copy the h5 file located in **king/PeakPicking Model/MobileNetPTModel.h5** and paste it into a new folder in your C Drive called models (eg. **C://models/MobileNetPTModel.h5**)


# Starting the flask App
1. Locate to to the folder in the repo containing the predict_app.py in cmd line

		cd C:\PeakPickingRepo\PeakPicking Model
		
2. Set the FLASK_APP variable to be the predict_app.py file

		set FLASK_APP=predict_app.py
		
3. Run the flask app ( a --host parameter here can be used to give others access to this web service but is not needed)

		flask run
		
4. look for the following lines to appear in the cmd line log. If these appear the flask app is running successfully. 

		* Loading Keras Model...
		* Model Loaded!
		* Running on http://[localhost]:5000/ (Press CTRL+C to quit)
		
# Using the Web Service

1. To view the front end go to http://[localhost]:5000/static/predict.html
2. Use the Choose file button to upload a .png ROI (ROI examples can be found in the Examples folder in this repo)
4. wait for the image to load and all predictions to be set to 0
3. Click the 'Predict' Button and wait for the Predictions to load 

