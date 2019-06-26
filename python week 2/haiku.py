from random import randint

haiku = []
five_syllable = [
"The cup is most empty",
"the mockingbird sings"
]
seven_syllable = [
"when the world will show you empty"
"You will see the beauty and"

]
first_index = random.randint(0, len(five_syllable)-1)
first_line = five_syllable[first_index]
haiku.append(first_line)

second_index = random.randint(0, len(seven_syllable)-1)
second_line = seven_syllable[first_index]
haiku.append(second_line)

third_index = first_index
while third_line == first_index:
    third_index = random.randint(0, len(five_syllable)-1)
third_line = five_syllable[third_index]
haiku.append(third_line)

for i in range(0,3):
    print(haiku[i])
