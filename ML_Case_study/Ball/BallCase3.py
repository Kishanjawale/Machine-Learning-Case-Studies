#imported Requiored Library
from sklearn import tree

def Ball_Predictor(Weight,Surface):

    #Ecoding the Dataaset 
    #Features                       #Labels
       #Rough  1                       #Tennis 2
       #Smooth 0                       #Cricket 1        
    
    #Loaded the Dataset
    Fetures= [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[10,0],[35,1],[95,0]]
    Labels = [2,2,1,2,1,2,1,2,2,2,1,2,1,2,1]

    #Decided machine learning algorithm
    obj= tree.DecisionTreeClassifier()           #DecisionTreeClassifier() is the name of algorithm

    #Performed the training of model
    obj = obj.fit(Fetures,Labels)

    #Performed the testing 
    Output=(obj.predict([[Weight,Surface]]))
    return Output

def main():    
    print("____________Ball Predictor Case Study By Kishan Jawale____________")
    print("___________________________________________________________________")

    #Taking Input (Weight and Surface type) 
    print("Please Enter The weight of Your Object in Grams:")
    Weight=int(input())

    print("Please Enter The type of Surface of Your Object (Rough /Smooth):")
    Surface= input()

    if Surface.lower() == "smooth":
        Surface = 0
    if Surface.lower() == "rough":
        Surface=1
    else:
        print("Invalid Type of Surface")
        exit()
    
    Ret=Ball_Predictor(Weight,Surface)
    
    if Ret==2:
        print("Predicted Ball is Tennis")
    if Ret==1:
        print("Predicted Ball is Cricket")

if __name__=="__main__":
    main()