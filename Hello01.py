# define a function
def main():
    def hello (to="world"):
        print ("Hello,",to )

    hello()

    # call the function
    name = input("what's your name? ")
    hello (name)

    #print (name)

main()