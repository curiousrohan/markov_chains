import random
import sys
from collections import OrderedDict
txt="the theremin is theirs, ok? yes, it is. this is a theremin." #Your sample text goes here.

order=3 #Tou can change the order of the ngram here
ngrams=[]
count=OrderedDict()
for i in range(0,len(txt)-order+1):
	gram=txt[i:i+order]
	ngrams.append(gram)
	if gram not in count:
		count.setdefault(gram,[])
	if gram in ngrams:
		#count[gram][0]+=1
		if i is not (len(txt)-order):
			count.setdefault(gram,[]).append(txt[i+order])

currentGram=txt[0:order]
for i in range(20):
	if(len(count[currentGram])) is 0:
		sys.exit(0)

	possibilities=random.choice(count[currentGram])
	newGram= currentGram+possibilities
	print(newGram,end='')
	currentGram=newGram[-order:]
