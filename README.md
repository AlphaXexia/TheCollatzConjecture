# The Collatz Conjecture

This is a graph of the Collatz conjecture which asserts that the total stopping time of every n is finite. It is also equivalent to saying that every n ≥ 2 has a finite stopping time. This definition yields smaller values for the stopping time and total stopping time without changing the overall dynamics of the process.

The way this is rationalized is that with every instance of n that is considered a Whole Odd Number is transformed with the equation *3n + 1* and on every instance of n that is Considered a Whole Even Number is transformed with the equation *n/2*. Thus creating a 4-2-1 loop which can be further seen in the example below.

![image](https://user-images.githubusercontent.com/54741558/136548661-77f2fc00-b702-483f-8ab7-e132f99760cf.png)

The reason as to why i've made this fun little project was because of how Mathematicians have considered it so infamous.

Note: This was easily made with [Matplotlib](https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/)
