# Thise code Move the first letter of each word to the end of it, then add "ay" to the end of the word.




def pig_it(sentence):
   
    words = sentence.split()
 
    pig_latin_words = []
    for word in words:
        
        if word.isalpha():
          
            pig_latin_word = word[1:] + word[0] + 'ay'
        else:
           
            pig_latin_word = word
        pig_latin_words.append(pig_latin_word)
   
    return ' '.join(pig_latin_words)

user_input = input("enter your sentence --> ")
result = pig_it(user_input)

print(f"the result for {user_input} is ({result})")