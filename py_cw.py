# Arash's coursework template

# Jose Fernandes, H00324200
# F28PL Coursework 2, Python                         <--- sanity check


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
    (real1, img1) = c1
    (real2, img2) = c2
    real = real1 + real2
    imag = img1 + img2
    return (real, imag)


def cmult(c1,c2):
    (real1, img1) = c1
    (real2, img2) = c2
    real = (real1 * real2) - (img1 * img2)
    img = (real1 * img2) + (real2 + img1)
    return (real, img)

#####################################
# Question 1b

def tocomplex(x1, y1):
    img = y1 * 1j
    return (x1 + img)


def fromcomplex(c):
    real = int(c.real)
    img = int(c.imag)
    return (real, img)


# END ANSWER TO Question 1
################################################################################


################################################################################
# Question 2


"""
2a. Using def, write iterative functions seqaddi and seqmulti that implement pointwise
addition and multiplication of integer sequences.
For instance
 seqaddi([1,2,3],[-1,2,2])
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
    addList = []
    for i in range(len(l1)):
        val = l1[i] + l2[i]
        addList.append(val)
    return addList


def seqmulti(l1, l2):
    mulList = []
    for i in range(len(l1)):
        val = l1[i] + l2[i]
        mulList.append(val)
    return mulList



#####################################
# Question 2b


def seqaddr(l1, l2):
    if len(l1) > 0:
        temp =  [ l1.pop() + l2.pop() ]
        return seqaddr(l1, l2) + temp
    else:
        return []


def seqmultr(l1, l2):
    if len(l1) > 0:
        temp = [ l1.pop() * l2.pop() ]
        return seqmultr(l1, l2) + temp
    else:
        return []


#####################################
# Question 2c


def seqaddlc(l1,l2):
    return list(( x + y for x in l1 for y in l2 if l1.index(x) == l2.index(y)))


def seqmultlc(l1,l2):
    return list(( x * y for x in l1 for y in l2 if l1.index(x) == l2.index(y) ))


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
    if (m == [[]]) or (m == []): return True

    lengthRow = len(m[0])
    length = len(m)

    for i in range(1, length - 1):
        if lengthRow != len(m[i + 1]):
            return False
        lengthRow = len(m[i])

    return True



def matrixshape(m):
    lengthRow = len(m[0])
    lengthCollumn = len(m)
    return (lengthRow, lengthCollumn)



def matrixadd(m1,m2):
    newMatrix = []
    for i in range(0, len(m1)):
        seq = seqaddlc(m1[i], m2[i])
        newMatrix.append(seq)
    return newMatrix


def mul_sumLists(seq1, seq2):
    list = seqmultlc(seq1, seq2)
    total = 0
    for el in list:
        total = total + el
    return total

def transposingMatrix(m):
    transposedMatrix = []
    for i in range(0, len(m[0])):
        tempRow = []
        for j in range(0, len(m)):
            tempRow.append(m[j][i])
        transposedMatrix.append(tempRow)
    return transposedMatrix

def multSeqbyMatrix(seq, matrix):
    tempList = []
    matrix = transposingMatrix(matrix)
    for row in matrix:
        tempList.append(mul_sumLists(row, seq))
    return tempList

def matrixmult(m1,m2):
    finalMatrix = []
    for row in m1:
        tempSeq = multSeqbyMatrix(row, m2)
        finalMatrix.append(tempSeq)
    return finalMatrix



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



"""

Mutable vs Immutable types

In Python, the mutable type objects are items with static values, which never change. In this programming language, all items and values are inherited from the "object" so there are no "pure values". For that reason, some built-in types have their inner value an immutable form, to not break the formal logic and object-oriented programming principles. The basic programming types, "bool", "int" and "float", are completely static because it avoids horrible errors that break the laws of mathematics and logic since it has to no good purpose to do so. 
The "tuple", "string" and "frozenset" types are defined by the user but their values can not change after being created since these types do not have functions to mutate their inner value. However, these types might have functions that return other objects resultant from the original object, without changing any of its properties. This ensures the programmer that the values will remain intact throughout the python script interpretation.
The mutable types are objects that can have their inner value changed. this property is very useful for the procedural programming paradigm as the values in the memory location must the updated according to the intended procedure, instead of just continuously taking more memory to store new values resultant from existing ones. The mutable types include "list", "tuple", "set" and "dictionaries". Additionally, the "frozenset" is inherited from the "set" and it is used, for example, in "dictionaries" as "key" since this data structure associates an immutable "key" to a "value".

"""



"""

Integer vs float types

Integers, in the python programming language, represent numbers the whole number values. The representation of a number is accomplished by allocating the same amount of memory for every integer because for a computer's memory there is no distinction between "0" and the integer maximum value. The integer's memory architecture uses all the bits to store the whole number value, apart from the first bit which determines if the value is positive or negative. As a result of the integer's representation having a low precision of 1 since it is dealing with the whole numbers, the computer finite memory can store these values with relative ease. Additionally, python will display numbers in the form of a "string of numbers" if the number is bigger than the memory available, event thought the computer's limited memory is not capable of processing those huge values.
However, the memory representation of a float value is completely different since it deals with fractional numbers with variable precision. For this reason, the memory architecture for this type of numbers takes more space than an integer value with constant precision. As a result, to switch between integers and floats it is necessary to use built-in constructors to cast the new number values into the computer memory.

"""



"""


Assignment = vs equality == vs identity

The assignment is the operation of allocating a value to a variable. In python, this operation is done with the single equality symbol "=". When assigning an object to another object, the assignment will allocate a "copy" the value of the object, instead of just referencing the same original object.
In python language, the objects are compared to determine if they have the same properties, using the equality operator "==". This operator has a boolean return type, which compares every single attribute and function of an object to determine if they are "equal". This does not mean that both variables point to the same object in memory but it means instead that these two objects share identical properties, attributes and functions.
In contrast to many conventional programming languages, python has an operator that checks if objects are references to the same value. That operator is the keyword "is". This operator simply compares the result of the function "id" that returns the numerical number which identifies every object in memory. In all, if both variables have the same "id" number means that they are the reference to the same object in memory. Testing if two variables point to the object is especially important to let the programmer careful when modifying them since it is unsafe to use variables that have second effects of the program.

"""



"""


The computational effects of a call to list on an element of range type, as in list(range(5**5**5))

The range function is a python native function that stores an object that generates a stream of integers. This function does not hold any values on memory but it holds a mathematical computation that streams a sequence of integer numbers.  This function is overloaded but generally, by default, the integer sequence has the minimum value of 0 and it is incremented by 1. The maximum integer is the value which has to be specified, at the least.
In contrast, the list constructor stores a sequence of polymorphic elements. It is usually used to store sequences of integers in the memory, without storing or referencing the mathematical computation which produced them.
In this example, the function range "5**5**5" will generate an integer stream from 0 to 298,023,223,876,953,125, incrementing successively by one, which means that it will generate a stream with 298,023,223,876,953,125 integers. This value is far too big for a regular computer processing power to perform. The result of this range function, the integer stream, is then stored into the memory using the list constructor which implies that a sequence of 298,023,223,876,953,125 integers will be stored in memory, what is also far too big for the regular computer's memory.

"""



"""


Slices, with examples. Including an explanation of the difference in execution between list(range(10**10)[10:10]) and list(range(10**10))[10:10]

In python, the slices have different results in lists and ranges. In lists, the slice operator returns a copy of the segment specified inside the squared brackets, that determine the initial and the last indexes for the integer sequence copy. 
In ranges, the slice operator determines where the stream should start from and when it should end. All the computation related to the rest of the stream will not be run, similarly to a "break" statement in a normal programming loop.
The first example shows a range function which will only run from the element integer 10 but it will also end at the same exact value. The range function will return an empty or null value which the list constructor will interpret as an empty list. This example only executes one operation in the range function and one operation in the list constructor, which is pretty cheap in processing power.
The second example is computing an integer stream from 0 to 10,000,000,000‬, one by one. This operation alone takes 10,000,000,000 operations what can be considered as a very costly operation. Furthermore, this sequence composed of 10,000,000,000‬ integer elements will then be stored in the computer memory what is very costly in terms of memory space. In this example, the slice operation is only called after the processing and the storage of this huge integer sequence to output an empty list, since the initial and the final indexes are the same. 


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
    dataType = type(dat)
    if dataType == int or dataType == float:
        return str(dat)
    elif dataType == complex:
        return str( int( dat.real ) ) + str("+") + str( int( dat.imag ) ) + str("j")


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
    if i == 0:
        return []
    else:
        return [ fenc( i - 1 ) , [ fenc( i - 1) ] ]




def fdec(l):
    if l == []:
        return 0
    else:
        el = l.pop()
        if el == []:
            return 0 + fdec(l)
        else:
            return 1 + fdec(l)


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
    cycle = ["code", "eat", "sleep"]
    counter = 1
    while True:
        index = counter % len(cycle)
        yield cycle[index]
        counter += 1


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
    if type(datum) == int:
        return [datum]
    elif datum == []:
        return []
    else:
        while type(datum[0]) == list:
            if datum[0] == []:
                return gendat(datum[1:])
            temp = datum[0].pop()
            if temp != []:
                datum.append(temp)
        return datum[0:1] + gendat(datum[1:])


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
    primes = [2]
    A = [True] * 5

    loop = 0

    while True:
        lastIndexPrimes = len(primes) - 1
        yield primes[lastIndexPrimes]

        for y in range(primes[lastIndexPrimes] + 1, len(A)):
            if A[y] == True:
                primes.append(y)
                lastIndexPrimes = len(primes) - 1
                newArrayLength = (primes[lastIndexPrimes] ** 2) + 1
                tempArray = [True] * ( newArrayLength - len(A))
                A += tempArray
                break

        for prime in primes:
            for i in range(primes[0], len(A) + 2, prime):
                A[i - 2] = False



# This is not an endless generator (like you're asked to programme) this will only get primes upto the passed input or 40000
def eratosthenesEXAMPLE(z=40000):
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
