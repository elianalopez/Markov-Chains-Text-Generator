import numpy as np
#import speak

text= open('./inauguraladdress.txt').read()
#print(text)

corpus = text.split()

# Display the corpus
#print(corpus)

#Make pairs to keys
def make_pairs(corpus):
    for i in range(len(corpus) - 1):
        yield (corpus[i], corpus[i + 1])

pairs = make_pairs(corpus)

word_dict = {}


for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]

# randomly pick the first word
first_word = np.random.choice(corpus)

# Pick the first word as a capitalized word so that the picked word is not taken from in between a sentence
while first_word.islower():
    first_word = np.random.choice(corpus)

# Start the chain from the picked word
chain = [first_word]

# Initialize the number of stimulated words
n_words = 25

for i in range(n_words):
    chain.append(np.random.choice(word_dict[chain[-1]]))

#Join returns the chain as a string
def txt():
    print(' '.join(chain) + '.')
txt()

def text():
    return(' '.join(chain)+ '.')



#Turn text into file
output = text()
file = open("output.txt","w")#append mode
file.write(output)
file.close()
