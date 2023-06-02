text = input("Enter your text: ")

text_without_space = text.replace(' ','')

character_frequency = {}

for character in text_without_space:
    if character in character_frequency:
        character_frequency[character] += 1
    else:
        character_frequency[character] = 1
                  
print("+" + 8 * "-" + "+" + 13* "-" + "+" + "\n| Name \t |   Frequency |\n" + "+" + 8 * "=" + "+" + 13 * "=" + "+")  

for character, frequency in character_frequency.items():
       print ("| {}      |           {} |".format(character,character_frequency[character]),"\n+" + 8 * "-" + 13 * "-" +"+")