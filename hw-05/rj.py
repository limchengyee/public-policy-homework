# Begin by making a dictionary of all of the characters in the play.
# Then count their spoken lines. Who has the most lines in the play?
# How many lines do they have?
uniq1 = '<b>'
uniq2 = '</b>'

name = []
dct = {}
with open('rj.html','r') as f:
    for line in f:
        if 'NAME=speech' in line:
            split = line[line.find(uniq1)+len(uniq1):line.find(uniq2)].strip()
            name.append(split)
for i in name:
    if i not in dct:
        dct[i] = 1
    else:
        dct[i] += 1

solution = max(dct, key=lambda i: dct[i])
print(solution)

#import text file
#separate text into words
#filter only the speech lines
# count number of times new words appear
