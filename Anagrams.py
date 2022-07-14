# from operator import truediv


# def is_anagam(s1,s2):
#     if (sorted(s1)==sorted(s2)):
#         print(sorted(s1),sorted(s2))
#         return True
#     return False

# print (is_anagam("knee","keen"))

from dataclasses import replace


def is_anagram(s1,s2):
    for i in s1:
        for j in s2:
            if i==j:
                s1.replace(s2)