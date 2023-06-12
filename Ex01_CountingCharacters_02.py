import collections , tabulate
text_without_spaces = input("Enter your text: ").replace(" ", "")
character_ferequency = list((collections.Counter(text_without_spaces)).items())
print(tabulate.tabulate(character_ferequency, headers =['Name','Frequency'] , tablefmt = 'grid'))