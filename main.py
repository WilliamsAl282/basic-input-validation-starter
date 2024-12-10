# Alex and Shay 
# 12/10/2024
# Validating String Input (Tiered Assignment)

# Are you and your partner working on Level 1, Level 2 or Level 3 today?
# Working on Level 3


input = input("Please enter a string: \n")

if input.isalpha() == True and len(input) in range(6,11):
    print(f"Valid input:{input} ")

else:
    print("Input must be alphabetic and have between 6 to 10 characters long")


