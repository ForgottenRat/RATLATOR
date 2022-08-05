import pyperclip #For copy

print("================================================================")
print("WELCUM TO RATLATOR                               By ForgottenRat")
sentence = input("YOUR SENTENCE HERE:\n")
print("================================================================")

# Words defines word to words
the = 'the'
new_the = 'da'

no = 'no'
new_no = 'nei'

brothers = 'brothers'
new_brothers = 'broddash'

brother = 'brother'
new_brother = 'brodda'

sisters = 'sisters'
new_sisters = 'sistashs'

poop = 'poop'
new_poop = 'caca'

mother = 'mother'
new_mother = 'modda'

father = 'father'
new_father = 'fodda'

you = 'you'
new_you = 'thou'

master = 'master'
new_master = 'masta'

s = 's'
new_s = 'sh'

#Replaces words in the sentence
sentence = sentence.replace(the, new_the)
sentence = sentence.replace(no, new_no)
sentence = sentence.replace(brothers, new_brothers)
sentence = sentence.replace(brother, new_brother)
sentence = sentence.replace(sisters, new_sisters)
sentence = sentence.replace(poop, new_poop)
sentence = sentence.replace(mother, new_mother)
sentence = sentence.replace(father, new_father)
sentence = sentence.replace(you, new_you)
sentence = sentence.replace(master, new_master)
sentence = sentence.replace(s, new_s)

#Prints and copies output
sentence = sentence.upper()
print(sentence)
print("================================================================")
pyperclip.copy(sentence)
print("!!!COPIED TO CLIPBOARD!!!")
print("ANY SHITGESTIONS? DM ForgottenRat#7375 ")

