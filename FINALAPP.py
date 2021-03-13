# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 20:37:21 2021

@author: User
"""


from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()
app = Flask(__name__)
model = pickle.load(open('D:/APP PROJECT/random_forest_regression_model (1).pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template("index.html")


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Crop_Red=0
    if request.method == 'POST':
        Temperature = int(request.form["Temperature"])
       
        Crop_Tomato=request.form['Crop_Tomato']
        if(Crop_Tomato==' Crop_Tomato'):
                Crop_Tomato=1
                Crop_Chilli=0
                Crop_Potato=0
        elif(Crop_Tomato==' Crop_Chilli'):
                Crop_Tomato=0
                Crop_Chilli=1
                Crop_Potato=0
                
        else:  
               Crop_Tomato=0
               Crop_Chilli=0
               Crop_Potato=1
            
                
       
        Soil_Red=request.form['Soil_Red']
        if(Soil_Red=='Red'):
            Soil_Red=1
            Soil_Black=0
            Soil_Alluvial=0
            
        elif(Soil_Red=='Black'):
            Soil_Red=0
            Soil_Black=1
            Soil_Alluvial=0
          
              
        else:
            Soil_Red=0
            Soil_Black=0
            Soil_Alluvial=1
            
         	  
        Soil_Texture_Loamy=request.form['Soil_Texture_Loamy']   
       
        if( Soil_Texture_Loamy=='Loamy'):
          
            Soil_Texture_Loamy=1
            Soil_Texture_Sandy=0
            Soil_Texture_Clayey=0
            
        elif(Soil_Texture_Loamy=='Sandy'):
            Soil_Texture_Loamy=0
            Soil_Texture_Sandy=1
            Soil_Texture_Clayey=0
              
        else:
            Soil_Texture_Loamy=0
            Soil_Texture_Sandy=0
            Soil_Texture_Clayey=1
            
              
         
        Soil_Colour_Red=request.form['Soil_Red']
        if(Soil_Colour_Red=='Red'):
            Soil_Colour_Red=1
            Soil_Colour_Black=0
            Soil_Colour_Brown=0
            
        elif(Soil_Colour_Red=='Black'):
            Soil_Colour_Red=0
            Soil_Colour_Black=1
            Soil_Colour_Brown=0
          
              
        else:
            Soil_Colour_Red=0
            Soil_Colour_Black=0
            Soil_Colour_Brown=1
            
            
            
            
        Drainage_High=request.form['Drainage_High']    
        if(Drainage_High=='High'):
            
                Drainage_High=1
                Drainage_Medium=0
                Drainage_Low=0
        elif(Drainage_High=='Medium'):
                Drainage_High=0
                Drainage_Medium=1
                Drainage_Low=0
                
        else:  
                Drainage_High=0
                Drainage_Medium=0
                Drainage_Low=1
                
                
       # Water_holding_capacity_Low=request.form['Water_holding_capacity_Low']
        
        #if(Water_holding_capacity_Low=="Low"):
                Water_holding_capacity_High=0
                Water_holding_capacity_Medium=0
                Water_holding_capacity_Low=1
                
               
        #elif(Water_holding_capacity_Low=="High"):
                Water_holding_capacity_High=1
                Water_holding_capacity_Medium=0
                Water_holding_capacity_Low=0
                
                
       # else:
                Water_holding_capacity_Low=0
                Water_holding_capacity_High=0
                Water_holding_capacity_Medium=1
                
                
                
                
        Sunlight_hgh=request.form['Sunlight_hgh'] 
        
        if(Sunlight_hgh=="hgh"):
               Sunlight_hgh=1
               Sunlight_low=0
               Sunlight_nor=0
               
               
        elif(Sunlight_hgh=="low"):
               Sunlight_hgh=0
               Sunlight_low=1
               Sunlight_nor=0 
               
               
        else:  
               Sunlight_hgh=0
               Sunlight_low=0
               Sunlight_nor=1
               
        prediction=model.predict([[Temperature, Crop_Potato, Crop_Tomato, Soil_Black, Soil_Red,
       Soil_Texture_Loamy, Soil_Colour_Brown,
       Soil_Colour_Red, Drainage_Low, Drainage_Medium,
       Drainage_Medium ,# Water_holding_capacity_Low,
       #Water_holding_capacity_Medium, Water_holding_capacity_Medium ,
       Sunlight_hgh, Sunlight_low, Sunlight_nor,]])
       
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot grow this crop")
        else:
            return render_template('index.html',prediction_text="the yield of crop is  {}".format(output))
    else:
        return render_template('index.html')
    
    
    
     

      
if __name__== "__main__":
    app.run(debug=True)