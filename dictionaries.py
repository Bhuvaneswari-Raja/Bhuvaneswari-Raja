
reference = {'pseudonym1': 'Thomas', 'pseudonym2': 'Alastair'}

for x in reference:
    print(x,":",reference[x])


Suits = ["\u2663", "\u2665", 
         "\u2666", "\u2660"] 
for x in range(len(Suits)):
    print(Suits[x])



word = "Ace of \u2660"
#list_my = word.split()
print(word.split()[2])
#print(list_my)
#print(" ".join(list_my))