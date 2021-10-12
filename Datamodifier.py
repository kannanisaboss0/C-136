#-------------------------------------Datamodifier.py-------------------------------------# 

"""
Importing Modules:
-pandas (pd)
-time (tm)
-selenium
"""

import pandas as pd
import time as tm
from selenium import webdriver


print("Welcome to datamodifier.py")
print("We provide API services for a particular dataset of stars and their attributes, which will be conducted in another file:StarDataAPI.py")

api_input=input("Know about APIs? (I know or I don't know)")

#Assessing the user's knowledge about APIs and conducting necessary actions
#Case-1
if(api_input=="I Don't Know" or api_input=="i don't know" or api_input=="I don't know" or api_input=="I don't Know" or api_input=="I Don't know" or api_input=="I Dont Know" or api_input=="i dont know" or api_input=="I dont know" or api_input=="I dont Know" or api_input=="I Dont know"):
    print("An API, or Application Programming Interface is method of communicating data between two applications.")
    tm.sleep(2.3)
    print("APIs are usually used for extracting data that changes frequently or for rendering services diificult through direct programming.")
    tm.sleep(3.7)
    print("The method by which an API communicates with an application vary heavily.")
    tm.sleep(2.3)
    print("APIs are increasingly assuming an important role in the digital world.")
    tm.sleep(1.2)
    print("They are found in almost all web applications, wth even some renowned corporations providing API services, which usualy are paid.")
    tm.sleep(3.4)
    print("To know more, visit 'https://www.cleo.com/blog/knowledge-base-what-is-an-api")

    #Verifying whether the user e=wants to open the link in Chrome or not
    open_input=input("Open link in Chrome?(Yes or No)")
    if(open_input=="Yes" or open_input=="yes" or open_input=="YES" or open_input=="yEs" or open_input=="yeS" or open_input=="Y" or open_input=="y"):
        open_browser=webdriver.Chrome("/Users/kannan/Coding/Projects/chromedriver projects")
        open_browser.get("https://www.cleo.com/blog/knowledge-base-what-is-an-api")


#Reading data from the dataset
df=pd.read_csv("data.csv")

names=df["Names"].tolist()
mass=df["Mass"].tolist()
radius=df["Radius"].tolist()
distance=df["Distance"].tolist()
gravity=df["Gravity"].tolist()

final_list=[]

#Running a for loop over the data in order to store the data appropriately in a list of dictionaries
for i in range(len(df)):
    temp_dict={}
    temp_dict={"Star Name":names[i],
    "Mass":mass[i],
    "Gravity":gravity[i],
    "Distance":distance[i],
    "Radius":radius[i]
    }
    final_list.append(temp_dict)

route_input=input("Please enter the name of the route desired to create:")


#-------------------------------------Datamodifier.py-------------------------------------# 