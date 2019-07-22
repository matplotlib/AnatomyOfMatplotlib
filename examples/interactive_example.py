#This example is inspired from my severe usage of MATLAB overlay plotting where I plot on a figure and based on its distribution/look I do some operation in backend like moving the image to another directory etc
import numpy as np
import matplotlib.pyplot as plt

def main():
    plt.ion() #Turining interactive mode on
    fig,ax = plt.subplots()
    for i in range(3):
        x=np.random.randn(100) #plotting points
        ax.plot(x)
        ax.set_xlabel('Index')
        ax.set_ylabel('Value')
        y=input("Shall we do internal operation on this?")
        if (y=='y'): # input y if we want to do operation in backend
            print("Yes performing operation")
        ax.cla() #Clearning axes here else it will overlap on previous plot. This is required sometimes based on your req


main()
