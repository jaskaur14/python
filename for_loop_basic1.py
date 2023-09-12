# Basic
for i in range(0, 151):
    print(i)

# Multiples of 5
for i in range(5,1001,5):
    # range given from first two numbers, multiple given in last (every 5 numbers)
    print(i)

# Counting the Dojo Way
for i in range(0, 101):
    if i % 10 == 0:
        print ("Coding Dojo")
    elif i % 5 == 0:
        print ("Coding")
    else:
        print(i)
        # numbers divisble by 10 print coding dojo, divisble by 5 print coding

# Whoa That Sucker's Huge
sum = 0
for i in range (1, 500001, 2):
    sum += i
print(sum)
# every 2 numbers

# Countdown by Fours
for i in range (2018, 0, -4):
    print(i)
    # counting down by 4, given by -4

# Flexible Counter
lowNum = 2
highNum = 9
multi = 3
for i in range (lowNum, highNum + 1):
    if i % multi == 0:
        print(i)
        # takes preset variables into consideration while doing the math for this problem
        