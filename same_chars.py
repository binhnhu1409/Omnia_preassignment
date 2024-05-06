"""
File: same_chars.py
-------------------
Omnia assignment: Write a function named same_chars, which takes one string and two integers as arguments.
The integers refer to indexes within the string.
The function should return True if the two characters at the indexes specified are the same.
Otherwise the function returns False.
"""

def same_chars():
    # State the purpose of this program
    print("This program compare 2 specified characters in a word.")

    # Ask input from users
    user_string = input("Enter a word:")
    index1 = int(input("Enter an index refer to a character within the string:"))
    index2 = int(input("Enter another index refer a character you want to compare with the previous one:"))

    # Print out output
    print(f"Your input: same_chars({user_string}, {index1}, {index2})")
    # check if the index that user input is valid
    if index1 < 0 or index2 < 0 or index1 > len(user_string) or index2 > len(user_string):
        print("The index you entered is not valid.")
        return False
    else:
        # check if 2 characters at those specified indexes are the same
        if user_string[index1] == user_string[index2]:
            print("True! There are two identical characters at the given indices.")
            return True
        else:
            print("False! The two characters are not identical.")
            return False

# The following lines is to call the same_chars() function
if __name__ == '__main__':
    same_chars()