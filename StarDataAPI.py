#-------------------------------------StarDataAPI,py-------------------------------------#

'''
Importing Modules
-flask :- Flask, request, jsonify
-datamodifier (file) :- final_list,route_input
'''
from flask import Flask,request,jsonify
from datamodifier import final_list,route_input

less_list=[]
great_list=[]

app=Flask(__name__)
@app.route('/')
#Defining a function to recieve and idsplay the main data
def Getdata():

    #Returning the data in the form of a list of dictionaries
    return jsonify({
        "data":final_list,
        "success":"True"
    },200)

@app.route('/'+route_input)
#Defining a function to find the star on the basis of the request provided by the user
def FindStar():
    star_name=request.args.get('name')

    #Verifying the validity of the request provided by the users
    #Case-1
    if star_name==None:

        #Returning the error message , on the request being empty or a NoneType object
        return josnify({
            "error":"Empty Request",
            "success":"False"
            })
    #Case-2        
    else:
        #Using a try block to assess the valididty of the user's request
        #Try block
        try:
            star_data=next(value for value in final_list if value["Star Name"]==star_name)     
            
            #Returning the data in the form of a list of dictionaries 
            return jsonify({
                "data({})".format(route_input):star_data,
                "success":"True",
                "Message":"Thank you for using StarDataAPI.py"
            },200)  
        #Except block    
        except:

            #Returning the eror message, in reponse to the invalid request stipulated by the user
            return({
                "error":"Invalid Request",
                "success":"False"
            })     

#Verifying whether the variable "__name__" is equal tp "__main__"
#Case-1
if __name__ == '__main__':
    app.run()  

#-------------------------------------StarDataAPI.py-------------------------------------#     