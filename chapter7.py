#1
#A.
#A definite loop is when a certain condition is supposed to be taken place a set amount of times.A indefinite loop however is a loop when the certain amount of iterations is unknown and is run indefinitely until it is reached.

#B.
#A for loop is used when the number of times it needs to repeat is known. While a While loop is when the loop is run until the a condition is met and while a case is present. When the number of iterations is unknown.
#C.
#A interactive loop is one that involves input from an external place such as a user and uses its input as a part of the loop. And continues to use the input in its data. A sentinel loop is one that continues to proccess until a end goal is met. With data that is usually unchanged from within.
#D.
#Mentioned prior a sentinel loop is one where it uses a set data repeatedly until a goal is met. A end of file loop is one where a computer OS has no more data to be read and thus ends the loop.



#2
#A.
#P             Q                not P and Q
#T            T                   F          
#T            F                   T
#F            T                   T
#F            F                   T


#
#B.
#TTF
#TFF
#FTT
#FFF


#C.
#TTF
#TFT
#FTT
#FFT

#D.
#TTTT
#TTFT
#TFTT
#TFFF
#FTTT
#FTFF
#FFTT
#FFFF

#E.
#TTTT
#TTFT
#TFTF
#TFFF
#FTTF
#FTFF
#FFTF
#FFFF


#3
#A.

n = int(input("enter a number to find the sum of all the counting numbers until desired number:"))

sum = 0
i = 1

while i <= n:
    sum += i
    i += 1


#C.

total = 0

while true:
    num = int(input("enter a number: "))
    if num == 999:
        break
    total += num

print(" The sum is: " total)

    



#4.
nterms = int(input("how many terms?: "))
n1 = 0
n2 = 1
count = 0

if nterms <= 0:
    print("please enter a positive int")
elif nterms == 1:
    print("Fib sequence upto",nterms,";")
    print(n1)
else:
    print("fib sequence: ")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1







#5
        

# get starting value from user n
n = int(input("Enter integer starting value: "))

# set sequence to syr(n)
sequence = syr(n)

# print sequence
print(sequence)

def syr(x):
    
    # initialize result list
    result = [x]

    # while x does not equal 1
    while x != 1.0:

        # if x is even
        if x % 2 == 0.0:

            # divide x by two
            x = x / 2

            # append x to result
            result.append(int(x))

        # if x is odd
        else:

            # 3x + 1
            x = 3 * x + 1

            # append to result
            result.append(int(x))

return result







