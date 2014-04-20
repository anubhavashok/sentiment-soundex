import fuzzy
soundex = fuzzy.Soundex(4)
f = open('positive')
pos = f.read()
pos = pos.split('\n')
pos_soundex = []
for word in pos:
	pos_soundex.append(soundex(word))

f = open('negative')
neg = f.read()
neg = neg.split('\n')
neg = neg[len(neg) - len(pos):]
neg_soundex = []
for word in neg:
	neg_soundex.append(soundex(word))

diff_array = []

cont = True
i = 0
while cont:
	
	end = i + len(pos)
	if end >= len(neg):
		end = len(neg)
	cur_neg = neg[i:end]
	cur_neg_soundex = neg_soundex[i:end]
	neg_count = 0
	for word in pos_soundex:
		if word in cur_neg_soundex:
			neg_count += 1
	
	pos_count = 0
	for word in cur_neg_soundex:
		if word in pos_soundex:
			pos_count += 1
	print(pos_count)
	print(neg_count)
	diff = pos_count - neg_count
	diff_array.append(diff)
	i += len(pos)
	if i >= len(neg):
		cont = False
