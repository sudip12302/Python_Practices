''' write a function that takes a word as input and counts the number of vowels
present in the word.'''
def count_vowels(word):
    vowels = 'aeiouAEIOU'
    vowels_count = 0
    const_count = 0
    for chrac in word:
        if chrac in vowels:
            vowels_count += 1
        else:
            const_count += 1

    return vowels_count, const_count
word = input("Enter a word: ")
vowels_count, const_count = count_vowels(word)
print(f"Number of vowels: {vowels_count}")
print(f"Number of constants: {const_count}")

