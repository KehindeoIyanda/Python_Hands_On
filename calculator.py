#x = int (input ("what is y? "))
#y = int (input ("what is x? "))

#print (x + y)


#x = float (input ("what is y? "))
#y = float (input ("what is x? "))

#z = round(y + x)

#print (f"{z:,}")


#x = float (input ("what is y? "))
#y = float (input ("what is x? "))

#z = (y / x)

#print (f"{z:.2f}")


def main() :
    x = int(input("what's x ?"))
    print("x squared is", square(x) )

def square(n) :
    #return n * n 
    return pow (n, 50)
    #return n ** 2

main()



