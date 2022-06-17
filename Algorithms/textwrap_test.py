import textwrap

sentence = 'their cow went to the house without knowledge'

wrapped = textwrap.wrap(sentence, 4)


final = ""
for wrap in wrapped:
    final += wrap + "\n"

print(final)