mot = input("Entrer un mot pour savoir s'il est un palindrome: ")

if(str(mot) == str(mot)[::-1]):
    print("TRUE, le mot est un palindrome")
else:
    print("FALSE, le mot n'est pas un palindrome")