mot =input("Entrer le mot ")
mot_inverse=mot[::-1]
if mot == mot_inverse :
    print("Ce mot est un palindrome")
else :
    print("Malheureusement c'est pas un palindrome")