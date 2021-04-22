# KMottershead Peak Picking DL Model

This repository holds the webservice and deep learning model (Model E) created as part of the research paper Deep Learning in Mass Spectrometry Analysis by K Mottershead and T Miller (link).

The model is stored as a .h5 file: PeakPicking Model/MobileNetPTModel.h5

The licensing of this repository can be found in the LICENSE file.

This web service can be run locally, where test files (.png) can be uploaded and tested against the model. The will be assigned a probability of Peak, No Peak, and Further Investigation (FI). This README.md file describes how you can set this to run locally. 

# Pre-Requisits
(All instructions are given for a Windows machine, linux and Mac has not been tested with this webservice and instruction may vary slightly) 
1. python must be installed locally (https://www.python.org/downloads/) (python verison 3.8 was used in the creation of this Model and Web Service)
2. pip must be installed and upgraded (normally comes packaged as part of python, upgrade cmd line is below)

			pip install --upgrade pip
			
3. Tensorflow (and thus Keras) must be installed locally (cmd line below)

			pip install tensorflow

4. Flask must also be installed locally (cmd line below)

	pip install Flask
	