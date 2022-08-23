# !/usr/bin/python3
# author: @aisabellafontes

def start():
    run = True
    while run:
        user_word = input("Enter string to test for palindrome or 'exit' ")
        word = str(user_word).strip().lower()        
        if word == 'exit':
            run = False
            break
        
        newstr = ""
        for x in word:
            if x.isalnum():
                newstr += x

        print("Palindrome test: ", is_palindrome(newstr))

    print("Bye!")

def is_palindrome(word):
    word_reverse = str(word[::-1])
    return word_reverse == word    

start()
