sentence = "Curso em Vídeo Python"

print(sentence)
# The len function returns the total number of characters in a string 
print(len(sentence)) # 21
print(sentence[9]) # V
# Read characters from the end using negative indices
print(sentence[-15]) # e
# String Slicing
print(sentence[9:13]) # Víde
print(sentence[13:]) # o Python
print(sentence[:13]) # Curso em Víde
print(sentence[1:15:2]) # us mVdo
# Reverse string
print(sentence[::-1]) # nohtyP oedíV me osruC
# Updating a String
print(sentence.replace("Python", "Android")) # Curso em Vídeo Android
# upper() method converts all characters to uppercase
print(sentence.upper()) # CURSO EM VÍDEO PYTHON
# lower() method converts all characters to lowercase
print(sentence.lower()) # curso em vídeo python
# strip() removes leading and trailing whitespace from the string
s = "   Gfg   "
print(s.strip()) # Gfg
print(s.rstrip()) #    Gfg
print(s.lstrip()) # Gfg   
# We can repeat a string multiple times using * operator
t = "Hey "
print(t * 3) # Hey Hey Hey 
# count returns the number of times a specified substring appears within that string
print(sentence.count("o")) # 3
print(sentence.count("o", 0, 13)) # 1
# The find() method finds the first occurrence of the specified value
print(sentence.find("deo")) # 11
print(sentence.find("Android")) # -1
# in keyword checks if a particular substring is present in a string
print("Curso"in(sentence)) # True
# Upper case the first letter in this sentence
print(sentence.capitalize()) # Curso em vídeo python
# Make the first letter in each word upper case
print(sentence.title()) # Curso Em Vídeo Python
# Split a string into a list where each word is a list item
print(sentence.split()) # ['Curso', 'em', 'Vídeo', 'Python']
# Join all items in a tuple into a string, using a hash character as separator
print("-".join(sentence)) # C-u-r-s-o- -e-m- -V-í-d-e-o- -P-y-t-h-o-n
# Strings are iterable; you can loop through characters one by one.
""" for i in sentence:
  print(i) """
