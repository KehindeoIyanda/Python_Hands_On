# Ask the for the users name
name = input ("what's your name? " ).strip().title()

# Remove white space str ( Removes extra space during input) and Capitalize username
#name = name.strip().title()

# Splite user name into first and last name

first, last = name.split(" ")

#print (f"hello, {first}")


# Say hello to user
print (f"Hello, {last}")

