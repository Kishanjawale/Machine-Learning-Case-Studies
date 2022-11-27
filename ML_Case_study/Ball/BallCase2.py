#imported Requiored Library
from sklearn import tree


#Features
#Rough  1
#Smooth 0


#Labels
#Tennis 2
#Cricket 1

#   
#Loaded the Dataset
Fetures= [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[10,0],[35,1],[95,0]]
Labels = [2,2,1,2,1,2,1,2,2,2,1,2,1,2,1]


#Decided machine learning algorithm
obj= tree.DecisionTreeClassifier()

#Performed the training of model
obj = obj.fit(Fetures,Labels)



#Performed the testing 
Output=(obj.predict([[90,0]]))

if (Output==2):
    print("Tennis")
if (Output==1):
    print("Cricket")