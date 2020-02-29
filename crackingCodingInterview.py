# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)

# "Mr John Smith ", 13

def URLify(url):
    if url[0] == " ":
        url = url[1:]
    if url[len(url) - 1] == " ":
        url = url[:-1]
    url = url.replace(" ", "%20")
    return url



# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# 1.5
# 1.6
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco eta", etc.)
# Hints: #106, #121, #134, #136 

def checkIfPermIsPalindrome(string):
    string_dict = {}
    isEven = False
    has_center = False
    for item in string:
        if item in string_dict:
            string_dict[item] += 1
        else:
            string_dict[item] = 1
    isEven = not len(string)%2
    for item in string_dict:
        if (string_dict[item]%2 == 1):
            if isEven:
                return False
            if has_center:
                return False
            has_center = True
    print("has permutation of a palindrome")
    return True

checkIfPermIsPalindrome("abcceerr")



# There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away. 