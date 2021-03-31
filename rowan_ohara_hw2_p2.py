# This program will determine if a pattern exists in DNA sequences

# First, the user will input the pattern to search for
pattern = input("Enter pattern: ")

# DNA sequence 1
DNAseq1 = input("Enter DNA sequence 1: ")  # The user inputs the first DNA sequence
length1 = len(DNAseq1)  # Then this finds the length of the sequence
count1 = 0
if pattern in DNAseq1:  # This looks for the pattern in the sequence
    print(pattern, "Exist")
else:
    print(pattern, "Does not exist")  # It prints a statement based on whether or not it was present
for c in DNAseq1:  # Then, it looks at the characters in the sequence
    if c in pattern: # if the characters are also present in the pattern
        count1 += 1  # it counts the number of times it occurs in the sequence
rate1 = count1 / length1  # To find the occurance rate, it divides the count by the length of the sequence
rate1 = round(rate1, 4) # Rounds the occurance rate to four decimal places
print("Occurance rate: ", rate1)

# The user inputs the DNA sequence 2
DNAseq2 = input("Enter DNA sequence 2: ")  # Then it just goes through the same steps as with the first sequence
length2 = len(DNAseq2)
count2 = 0
if pattern in DNAseq2:
    print(pattern, "Exist")
else:
    print(pattern, "Does not exist")
for c in DNAseq2:
    if c in pattern:
        count2 += 1
rate2 = count2 / length2
rate2 = round(rate2, 4)
print("Occurance rate: ", rate2)

# The user inputs the DNA sequence 3
DNAseq3 = input("Enter DNA sequence 3: ")
length3 = len(DNAseq3)
count3 = 0
if pattern in DNAseq3:
    print(pattern, "Exist")
else:
    print(pattern, "Does not exist")
for c in DNAseq3:
    if c in pattern:
        count3 += 1
rate3 = count3 / length3
rate3 = round(rate3, 4)
print("Occurance rate: ", rate3)

# The user inputs the DNA sequence 4
DNAseq4 = input("Enter DNA sequence 4: ")
length4 = len(DNAseq4)
count4 = 0
if pattern in DNAseq4:
    print(pattern, "Exist")
else:
    print(pattern, "Does not exist")
for c in DNAseq4:
    if c in pattern:
        count4 += 1
rate4 = count4 / length4
rate4 = round(rate4, 4)
print("Occurance rate: ", rate4)

# The user inputs the DNA sequence 5
DNAseq5 = input("Enter DNA sequence 5: ")
length5 = len(DNAseq5)
count5 = 0
if pattern in DNAseq5:
    print(pattern, "Exist")
else:
    print(pattern, "Does not exist")
for c in DNAseq5:
    if c in pattern:
        count5 += 1
rate5 = count5 / length5
rate5 = round(rate5, 4)
print("Occurance rate: ", rate5)