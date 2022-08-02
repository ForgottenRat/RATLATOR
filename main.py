print("================================================================")
print("WELCUM TO RATLATOR")
sentence = input("Your sentence here:\n")
uppercase = input("do you want the output in uppercase?(y, n): ")   
print("================================================================")

# Words 
yes1 = 'yes'
new_yes1 = 'yesh'

discord1 = 'discord'
new_discord1 = 'dishcord'

must1 = 'must'
new_must1 = 'musht'

his1 = 'his'
new_his1 = 'hish'

the1 = 'the'
new_the1 = 'da'

no1 = 'no'
new_no1 = 'nei'

is1 = 'is'
new_is1 = 'ish'

brothers1 = 'brothers'
new_brothers1 = 'broddash'

brother1 = 'brother'
new_brother1 = 'brodda'

sisters1 = 'sisters'
new_sisters1 = 'sistashs'

poop1 = 'poop'
new_poop1 = 'caca'



for i in range(sentence.count(yes1)):
        sentence = sentence.replace(yes1, new_yes1, 1)  # replacing only one match

for i in range(sentence.count(discord1)):
        sentence = sentence.replace(discord1, new_discord1, 1)  # replacing only one match

for i in range(sentence.count(must1)):
        sentence = sentence.replace(must1, new_must1, 1)  # replacing only one match

for i in range(sentence.count(his1)):
        sentence = sentence.replace(his1, new_his1, 1)  # replacing only one match

for i in range(sentence.count(the1)):
        sentence = sentence.replace(the1, new_the1, 1)  # replacing only one match

for i in range(sentence.count(no1)):
        sentence = sentence.replace(no1, new_no1, 1)  # replacing only one match

for i in range(sentence.count(is1)):
        sentence = sentence.replace(is1, new_is1, 1)  # replacing only one match

for i in range(sentence.count(brothers1)):
        sentence = sentence.replace(brothers1, new_brothers1, 1)  # replacing only one match

for i in range(sentence.count(brother1)):
        sentence = sentence.replace(brother1, new_brother1, 1)  # replacing only one match

for i in range(sentence.count(sisters1)):
        sentence = sentence.replace(sisters1, new_sisters1, 1)  # replacing only one match

for i in range(sentence.count(poop1)):
        sentence = sentence.replace(poop1, new_poop1, 1)  # replacing only one match


if uppercase == "y":
    print(sentence.upper())

if uppercase == "n":
    print(sentence)

    