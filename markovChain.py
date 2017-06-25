import random 

def markov(input, legnth):
    #input = input text
    #legnth = word legnth of output text
    #separate text into dict of words
    words = input.split()
    wordList = {i:[] for i in words} #make dict of lists
    
    pos = 0
    while pos < len(words) - 1: 
        wordList[words[pos]].append(words[pos+1]) #add to word's list of words that occur after
        pos += 1
        
    output = ""
    wordCount = 0
    currentWord = words[random.randint(0, len(words) - 1)]
    while wordCount <= legnth: #construct output string based on dict entries
        output = output + " %s" %currentWord #add to output 
        if not wordList[currentWord]:
            currentWord = words[random.randint(0, len(words) - 1)] #pick random word if this is the last word in data
        else:
            currentWord = wordList[currentWord][random.randint(0, len(wordList[currentWord])-1)] #if not, pick random word based on list
        wordCount += 1
        
    return output 
    
print "Enter text to be markov'd: "
data = raw_input(">> ")

print "Input number of output words: "
number = input(">> ")
    
print markov(data, number)
