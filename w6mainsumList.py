x3=list()
for i in range(0,1001):
    if i%4==0 and i%5!=0:
        x3.append(i)
print x3

sum=0
for i in range(0,len(x3)):
    sum+=x3[i]
print sum



"""
JSY 201410028
20160411
"""

def sumList(list):
    sum=0
    for i in range(0,len(x3)):
        sum+=x3[i]
    return sum
    
sumList(x3)


def lab6():
    x=[1,2,3]
    mysum=sumList(x3)
    print mysum

def main():
    lab6()