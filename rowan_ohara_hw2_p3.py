# This program will determine if a pattern exists in DNA sequences

# First, the user will input the pattern to search for
pattern = input("Enter pattern: ")

# This initializes the variables and ensures that after each time the loop wipes the memory 
# of the occurance rate variable, the rates can still be used
rate1 = ""
rate2 = ""
rate3 = ""
rate4 = ""
rate5 = ""

# Problem 1 and 2
for x in range(1,6):  # This loop repeats these steps 5 times
    DNAseq = input("Enter DNA sequence " + str(x) + ": ")  # The user inputs the DNA sequence
    length = len(DNAseq)  # Then this finds the length of the sequence
    count = 0
    if pattern in DNAseq:  # This looks for the pattern in the sequence
        print(pattern, "Exist")
    else:
        print(pattern, "Does not exist")  # It prints a statement based on whether or not it was present
    for c in DNAseq:  # Then, it looks at the characters in the sequence
        if c in pattern: # if the characters are also present in the pattern
            count += 1  # it counts the number of times it occurs in the sequence
    occuranceRate = count / length  # To find the occurance rate, it divides the count by the length of the sequence
    occuranceRate = round(occuranceRate, 4) # Rounds the occurance rate to four decimal places
    print("Occurance rate: ", occuranceRate)
    if (x == 1):  # This checks if it is the first sequence,
        rate1 = occuranceRate  # then save the occurance rate to the occurance of the first sequence
    if (x == 2):  # This repeats for each sequence
        rate2 = occuranceRate
    if (x == 3):
        rate3 = occuranceRate
    if (x == 4):
        rate4 = occuranceRate
    if (x == 5):
        rate5 = occuranceRate

# This portion compares the occurance rates by finding the average, minimum, and maximum
# Problem 3

print()

# Average
aveRate = (rate1 + rate2 + rate3 + rate4 + rate5) / 5  # This finds the average occurance rate
aveRate = round(aveRate, 4)
print("Average Occurance Rate:", aveRate)

# Minimum
do_quit1 = False  # This is a boolean marker, this will let tell the while loop to stop when it becomes True
while not do_quit1:
    if rate1 < rate2:  # This is a series of if statements that compares each rate to every other rate
        if rate1 < rate3:  # If it is lower it will continue through these statements
            if rate1 < rate4:
                if rate1 < rate5:
                    print("Minimum Occurance Rate:", rate1)  # and print it as the lowest
                    do_quit1 = True  # and then stop the loop
    if rate2 < rate1:  # If any one of the above if statements are false,
        if rate2 < rate3:  # it will start comparing the next rate to every other rate
            if rate2 < rate4:
                if rate2 < rate5:  # until it determines it is the lowest
                    print("Minimum Occurance Rate:", rate2)  # and prints it
                    do_quit1 = True  # and then stops the loop
    if rate3 < rate1:
        if rate3 < rate2:
            if rate3 < rate4:
                if rate3 < rate5:
                    print("Minimum Occurance Rate:", rate3)
                    do_quit1 = True
    if rate4 < rate1:
        if rate4 < rate2:
            if rate4 < rate3:
                if rate4 < rate5:
                    print("Minimum Occurance Rate:", rate4)
                    do_quit1 = True
    if rate5 < rate1:
        if rate5 < rate2:
            if rate5 < rate3:
                if rate5 < rate4:
                    print("Minimum Occurance Rate:", rate5)
                    do_quit1 = True

# Maximum
do_quit2 = False  # This works in the same way as the minimum portion
while not do_quit2:
    if rate1 > rate2:  # Excepts it compares each rate to find the highest
        if rate1 > rate3:  # The same logic applies
            if rate1 > rate4:
                if rate1 > rate5:
                    print("Maximum Occurance Rate:", rate1)
                    do_quit2 = True
    if rate2 > rate1:
        if rate2 > rate3:
            if rate2 > rate4:
                if rate2 > rate5:
                    print("Maximum Occurance Rate:", rate2)
                    do_quit2 = True
    if rate3 > rate1:
        if rate3 > rate2:
            if rate3 > rate4:
                if rate3 > rate5:
                    print("Maximum Occurance Rate:", rate3)
                    do_quit2 = True
    if rate4 > rate1:
        if rate4 > rate2:
            if rate4 > rate3:
                if rate4 > rate5:
                    print("Maximum Occurance Rate:", rate4)
                    do_quit2 = True
    if rate5 > rate1:
        if rate5 > rate2:
            if rate5 > rate3:
                if rate5 > rate4:
                    print("Maximum Occurance Rate:", rate5)
                    do_quit2 = True