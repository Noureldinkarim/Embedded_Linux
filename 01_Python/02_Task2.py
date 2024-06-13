
vowels = {'a','e','i','o','u','A','E','I','O','U'}

def check_vowel(input):
    if input in vowels:
        return True
    else:
        return False

value = input("Enter a Character: ")
if(check_vowel(value)):
    print("Letter is a vowel")
else:
    print("Letter is not a vowel")


