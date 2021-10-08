#Collatz conjecture mk. 5
import matplotlib.pyplot as plt

i = int(input("Give me a Rational Number: "))
# x = []
x = [1]
y = variable_outputs = [i]
ctr = 1
if(i>0) :
    #made for an input when it is equal to 1
    while(i==1):
        if((i%2)==0):
            i//=2
            ctr+=1
            x.append(ctr)
        elif((i%2)==1):
            i=(3*i)+1
            ctr+=1
            x.append(ctr)
        #This will show the 4-2-1 loop immediately
        variable_outputs.append(i)
    
    #made for an input when it is not equal to 1
    while(i != 1):
        if((i%2)==0):
            i//=2
            ctr+=1
            x.append(ctr)
        elif((i%2)==1):
            i=(3*i)+1
            ctr+=1
            x.append(ctr)
        variable_outputs.append(i)
    
    # plotting the points
    plt.plot(x, y)

    # naming the x axis
    plt.xlabel('Number of Variables\nx - axis ')
    # naming the y axis
    plt.ylabel('Minimum to Maximum Range of Variables\ny - axis')

    # giving a title to my graph
    plt.title('Collatz Conjecture')

    # function to show the plot
    plt.show()
            
    print("Number of Variables: "+str(x[-1]))
    
    print("List of Variables: "+str(variable_outputs))
    
else:
    #for any input that is not a Positve Whole Number
    print(str(i)+" is not a Rational Number.")
