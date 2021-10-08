#Collatz conjecture mk. 5
import matplotlib.pyplot as plt

i = int(input("Give me a Rational Number: ")) #pass the errors
# x = []
x = [1]
y = variable_outputs = [i]
ctr = 1
if(i>0) :
    while(i==1):
        if((i%2)==0):
            i//=2
            ctr+=1
            x.append(ctr)
        elif((i%2)==1):
            i=(3*i)+1
            ctr+=1
            x.append(ctr)
        variable_outputs.append(i)
        
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
        
    print(x)
    
    print("THE COLLATZ CONJECTURE")
    print(variable_outputs)
    
    # plotting the points
    plt.plot(x, y)

    # naming the x axis
    plt.xlabel('x - axis')
    # naming the y axis
    plt.ylabel('y - axis')

    # giving a title to my graph
    plt.title('My first graph!')

    # function to show the plot
    plt.show()
    
else:
    print(str(i)+" is not a Rational Number.")
    
