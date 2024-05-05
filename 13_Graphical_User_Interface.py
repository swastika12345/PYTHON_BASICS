#Graphical User Interface


#Question 1
import matplotlib.pyplot as plt
x=[2,5,7,9,12,45,65,78,9,2,22,31,6]
y=[1,12,4,6,8,54,44,89,23,41,36,33,40]
plt.scatter(x,y)
plt.show()

#Question 2
import matplotlib.pyplot as plt
x=[4,2,1]
y=[1,3,2]
plt.plot(x,y,label='line 1')
plt.xlabel('x-axis')
plt.xlabel('y-axis')
plt.show()

#Question 3
import matplotlib.pyplot as plt
import numpy as np
a = np.array([12,23,32,34,45,46,54,33,36,78,89,90])
fig, ax = plt.subplots(figsize =(5, 2))
ax.hist(a, bins = [0, 20, 40, 60,80, 100])
plt.show()

#Question 4
import matplotlib.pyplot as plt
import numpy as np
y=np.array([12,28,20,25,5])
mylabels=["Maths","English","Geography","Science","History"]
plt.pie(y,labels=mylabels,shadow=True)
plt.show()

#Question-5
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]
plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.show() 