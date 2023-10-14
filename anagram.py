#Write a function to check if two strings are anagrams of each other (contain the same characters in a different order

def are_anagram(str1,str2):
    return sorted(str1)==sorted(str2)

print(are_anagram("abcd","dabc"))