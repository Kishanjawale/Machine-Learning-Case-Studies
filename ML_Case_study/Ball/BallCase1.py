#imported Requiored Library
from sklearn import tree


#Loaded the Dataset
Fetures= [[35,"Rough"],[47,"Rough"],[90,"Smooth"],[48,"Rough"],[90,"Smooth"],[35,"Rough"],[92,"Smooth"],[35,"Rough"],[35,"Rough"],[35,"Rough"],[96,"Smooth"],[43,"Rough"],[110,"Smooth"],[35,"Rough"],[95,"Smooth"]]
Labels = ["Tennis","Tennis","Cricket","Tennis","Cricket","Tennis","Cricket","Tennis","Tennis","Tennis","Cricket","Tennis","Cricket","Tennis","Cricket"]


#Decided machine learning algorithm
obj= tree.DecisionTreeClassifier()

#Performed the training of model
obj = obj.fit(Fetures,Labels)


#Performed the testing
print(obj.predict([[97,"Smooth"]]))
