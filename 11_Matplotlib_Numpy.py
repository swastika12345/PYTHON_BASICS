#Matplotlib_Library

#Question-1
import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,3,6,4,9])
y=np.array([30,50,70,80,90])
plt.plot(x,y)
plt.show()

#Question-2
import matplotlib.pyplot as plt
import numpy as np
x=np.array([12,34,56,78,90])
y=np.array([1.5,3.6,4.5,7.8,9.0])
plt.plot(x,y,'o')
plt.show()

#Question-3
import matplotlib.pyplot as plt
import numpy as np
x=np.array([12,34,56,78,90])
y=np.array([1.5,3.6,4.5,7.8,9.0])
plt.plot(x,y,'*')
plt.show()

#Question-4
import matplotlib.pyplot as plt
import numpy as np
x=np.array([12,34,56,78,90])
y=np.array([1.5,3.6,4.5,7.8,9.0])
plt.plot(x,y,'s')
plt.show()

#Question-5
import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,2,6,8])
y=np.array([3,8,1,10])
plt.plot(x,y)
plt.show()

#Question-6
import matplotlib.pyplot as plt
import numpy as np
y=np.array([3,8,1,10])
plt.plot(y,marker='o',ms=20)

#Question-7
import matplotlib.pyplot as plt
import numpy as np
y=np.array([3,8,1,10])
plt.plot(y,'o:g',ms=20)
plt.show()

#Question-8
import matplotlib.pyplot as plt
import numpy as np
y=np.array([3,8,1,10])
plt.plot(y,'o-.c',ms=20)
#after o the interpretetion this will mark the line design
plt.show()


#Question-9
import matplotlib.pyplot as plt
import numpy as np
y=np.array([3,8,1,10])
plt.plot(y,marker='*',ms=20,mec='r')
#mec give the colour of symbol boundary
plt.show()

#Question-10
import matplotlib.pyplot as plt
import numpy as np
y=np.array([3,8,1,10])
plt.plot(y,marker='o',ms=20,mec='r',mfc='r')
#mfc=Color between the boundary
plt.show()

#Question-11
import matplotlib.pyplot as plt
import numpy as np
y=np.array([3,8,1,10])
plt.plot(y,linestyle='dotted',color='g')
plt.show()

#Question-12
import matplotlib.pyplot as plt
import numpy as np
y=np.array([3,8,1,10])
plt.plot(y,linestyle='dashed',color='r')
plt.show()

#Question-13
import matplotlib.pyplot as plt
import numpy as np
y=np.array([3,8,1,10])
plt.plot(y,linewidth='30',color='yellow')
plt.show()

#Question-14
import matplotlib.pyplot as plt
import numpy as np
x1=np.array([2,4,5,7])
y1=np.array([3,8,1,10])
x2=np.array([1.2,2.5,3.6,5.8,6.2])
y2=np.array([7.1,8.2,9.4,10.4,12.5])
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.xlabel("Pulse rate")
plt.ylabel("Time")
plt.title("Patient-Pulse Rate",color='yellow')
plt.grid()


#Question-15
import matplotlib.pyplot as plt
import numpy as np
x1=np.array([2,4,5,7])
y1=np.array([3,8,1,10])
x2=np.array([1.2,2.5,3.6,5.8,6.2])
y2=np.array([7.1,8.2,9.4,10.4,12.5])
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.xlabel("Pulse rate")
plt.ylabel("Time")
plt.title("Patient-Pulse Rate",color='yellow')
plt.grid(axis ='x')
plt.show()
plt.show()

#Question-16
import matplotlib.pyplot as plt
import numpy as np
x1=np.array([2,4,5,7])
y1=np.array([3,8,1,10])
x2=np.array([1.2,2.5,3.6,5.8,6.2])
y2=np.array([7.1,8.2,9.4,10.4,12.5])
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.xlabel("Pulse rate")
plt.ylabel("Time")
plt.title("Patient-Pulse Rate")
plt.grid(axis ='y')
plt.show()

#Question-17
import matplotlib.pyplot as plt
import numpy as np
x1=np.array([2,4,5,7])
y1=np.array([3,8,1,10])
x2=np.array([1.2,2.5,3.6,5.8,6.2])
y2=np.array([7.1,8.2,9.4,10.4,12.5])
plt.subplot(1,2,1)
plt.plot(x1,y1)
plt.subplot(1,2,2)
plt.plot(x2,y2)
plt.xlabel("Pulse rate")
plt.ylabel("Time")
plt.title("Patient-Pulse Rate")
plt.grid(axis ='y')
plt.show()

#Question-18
import matplotlib.pyplot as plt
import numpy as np
x1=np.array([0,1,2,3])
y1=np.array([3,8,1,10])
x2=np.array([0,1,2,3])
y2=np.array([10,20,30,40])
plt.subplot(1,2,1)
plt.plot(x1,y1)
plt.subplot(1,2,2)
plt.plot(x2,y2)
plt.show()