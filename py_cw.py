# Arash's coursework template

# My Name here, My UserID, My Regno (why not)  <--- so we know who you are
# F28PL Coursework PY1                         <--- sanity check


# You may assume variables, procedures, and functions defined in earlier questions
# in your answers to later questions, though you should add comments in code explaining
# this if any clarification might help read your code.


################################################################################
# Question 1   <--- Yes, so we know what question you think you're answering


"""
The complex numbers are explained here (and elsewhere):
 http://www.mathsisfun.com/algebra/complex-number-multiply.html
Represent a complex integer as a pair of integers, so (4,5) represents 4+5i (or 4+5j, depending on the complex numbers
notation you use).
1a. Using def, define functions cadd and cmult representing complex integer addition and
multiplication.
For instance,
 cadd((1,0),(0,1))
should compute
 (1,1).
1b. Python has its own native implementation of complex numbers. Write translation functions
tocomplex and fromcomplex that map the pair (x1,y1) to the complex number x1+(y1)j and vice 
versa. You may use the python methods real and imag without comment, but not complex 
(use j directly instead).
"""
#  <--- always have the question under your nose

#####################################
# Question 1a


def cadd(c1, c2):
    pass


def cmult(c1,c2):
    pass


#####################################
# Question 1b

def tocomplex(x1, y1):
    pass


def fromcomplex(c):
    pass


# END ANSWER TO Question 1
################################################################################


################################################################################
# Question 2


"""
2a. Using def, write iterative functions seqaddi and seqmulti that implement pointwise
addition and multiplication of integer sequences.
For instance
 seqaddi([1,2,3],[~1,2,2])
should compute
 [0,4,5]
You need not write error-handling code to handle the cases that sequences have different
lengths.
2b. Do as for 2a, but make your functions recursive (like OCaml).
Call them seqaddr and seqmultr.
2c. Do it again. This time use list comprehensions instead of iteration or recursion.
"""

#####################################
# Question 2a


def seqaddi(l1, l2):
    pass


def seqmulti(l1, l2):
    pass


#####################################
# Question 2b


def seqaddr(l1, l2):
    pass


def seqmultr(l1, l2):
    pass


#####################################
# Question 2c


def seqaddlc(l1,l2):
    pass


def seqmultlc(l1,l2):
    pass




# END ANSWER TO Question 2
################################################################################

################################################################################
# Question 3

"""
Write functions
● ismatrix
This should input a list of list of integers (henceforth an intmatrix) and test whether a list
of lists of integers represents a matrix (so the length of each row should be equal).
● matrixshape
This should input an intmatrix and return the size of the matrix, which is the number of rows and the number of columns 
(traditionally the number of rows is given first, but if you have done it the other way around that’s fine; 
just make sure to clearly explain your code). 

● matrixadd
Matrix addition, which is simply pointwise addition.
● matrixmult
Similarly for matrix multiplication.
You do not need to write error-handling code, e.g. for the cases that inputs do not represent
matrices or represent matrixes of the wrong shapes; so for instance your matrixshape may 
assume that the argument has successfully passed the test ismatrix.
Your answer can use iteration, recursion, list comprehension, or anonymous functions. You
should not appeal to any libraries, e.g. for matrix processing.  Don't use zip.
"""


def ismatrix(m):
    pass


def matrixshape(m):
    pass


def matrixadd(m1,m2):
    pass


def matrixmult(m1,m2):
    pass

# END ANSWER TO Question 3
################################################################################


###############################################################################
# Question 4


"""
Write an essay on Python data representation. Be clear, to-the-point, and concise. Convince
your marker that you understand:
● Mutable vs immutable types. Give at least two examples of each, with explanation.
● Integer vs float types.
● Assignment = vs equality == vs identity is.
● The computational effects of a call to list on an element of range type, as in
list(range(5**5**5)).
● Slices, with examples. Including an explanation of the difference in execution between
 list(range(10**10)[10:10]) and
 list(range(10**10))[10:10]
Include short code-fragments where appropriate (as I do when lecturing) to illustrate your
observations.
"""




# END ANSWER TO Question 4
################################################################################


###############################################################################
# Question 5
print()
print('Question 5')

"""
Write a general encoding function encdat that will input an integer, float, complex number, or
string, and return it as a string.

So
• encdat(-5) should return '-5'
• encdat(5.0) should return '5.0'
• encdat(5+5j) should return '5+5j' (not '(5+5j)'; see hint below).
• encdat('5') should return '5'


"""


def encdat(dat):
    pass

# END ANSWER TO Question 5
################################################################################


###############################################################################
# Question 6


"""
An encoding f of numbers in lists is as follows:
• f(0) = [] (0 maps to the empty list)
• f(n+1) = [f(n),[f(n)]] (n+1 maps to the list that contains f(n) and singleton f(n))
Implement encode and decode functions in Python, that map correctly between nonnegative
integers and this representation. Call them fenc and fdec.
"""


def fenc(i):
    pass


def fdec(l):
    pass


# END ANSWER TO Question 6
################################################################################


###############################################################################
# Question 7


"""
Implement a generator cycleoflife such that if we assign
 x = cycleoflife()
then repeated calls to
 next(x)
return the values
 eat
 sleep
 code
 eat
 sleep
 code
 ...
in an endless cycle. If you can’t manage an endless cycle, do a program that runs for 1000
cycles then stops.
Note that this question is not asking you to program an endless loop that prints these values.
In effect, I am asking you to implement what is called a stream (infinite list)
 x = [eat, sleep, code, eat, sleep, code, ...].
This does not mean the whole infinite datastructure is in memory at any time (which is 
impossible for a machine with finite memory), but for any finite but unbounded number of calls 
to next your generator behaves as if it were the infinite datastructure illustrated above.
"""


def cycleoflife():
    pass



# END ANSWER TO Question 7
################################################################################


#################################################################################
# Question 8

"""
Call a *datum* something that is either an integer, or a list of data (datums).

Write a flatten function gendat that converts a datum to a list of integers.

So
- gendat(5) should return [5]
- gendat([])should return []
- gendat([5,[5,[]],[],[5]]) should return [5,5,5]

Do not use str.  You may find it useful to consider isinstance or the following code fragment
   type(5) == type([]) 
"""


def gendat(datum):
    pass


# END ANSWER TO Question 8
################################################################################


##########################################################
# Question 9

"""
Implement the Sieve of Eratosthenes
 https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
as a Python generator eratosthenes such that if we assign
 x = eratosthenes()
then repeated calls to
 next(x)
return the primes, starting from 2.
"""

def eratosthenes():
    pass



# This is not an endless generator (like you're asked to programme) this will only get primes upto the passed input or 40000
def eratosthenes(z=40000):
    # create an array of true values the size of z
    A = [True] * z
    # iterate over each value to z squared
    for x in range(2, int(z ** 0.5)):
        # if A[x] has a true value
        if A[x]:
            # iterate over a range starting from x*2 ending at z in jumps of x
            for z in range(x * 2, z, x):
                # set anything in the range to false
                A[z] = False
    # iterate over the array
    for y in range(2, len(A)):
        # if a value is true that index is a prime number
        if A[y]:
            # yield the current iterator location as it is a prime
            yield y




# END ANSWER TO Question 9
################################################################################
