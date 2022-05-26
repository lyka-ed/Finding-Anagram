# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = str(word)
    anagram = str(anagram)

    # made use of the sorted().
    return (sorted(word) == sorted(anagram))

ana_1 = find_anagram("marine", "remain")
print(ana_1)

ana_2 = (find_anagram("parrot", "remain"))
print(ana_2)


