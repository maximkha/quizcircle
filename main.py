from textblob import TextBlob

import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

KEEPTAGS = ['NN', 'NNP', 'IN', 'NNS', 'JJ', 'CD']

#order from more complex to least
STARTS = ['how many ', 'name the ', 'what is ', 'what ', "during "]

POPULARITY = False # don't adjust for number of refernces, just the sum

#text = 'how many wonders of the ancient world are there'
#text = 'Name the Paris museum that houses the famous Greek marble statue entitled Victory of Samothrace'
#text = 'During this conflict, the territorial governor Charles Bent was scalped in the Taos Revolt.'
#text = 'A poem written in this language that contrasts a creature who knows one big thing with an animal'
#text = 'This city was ruled by the Council of 104, which sent Hamilcar to conquer Sicily in 310 BC. '
text = input("Q> ")

text = text.lower()

#remove the starts

for start in STARTS:
    if text[:len(start)] == start:
        print("Found start '" + start[:-1] + "'")
        text = text[len(start):]
        break

blob = TextBlob(text)

print("Extracting keywords")
words = []
for word, tag in blob.pos_tags:
    #print(word + ", " + tag)
    if tag in KEEPTAGS:
        words.append(word)

query = str.join(" ",words)
print("Query: " + query) 

#exit()

import wikipedia
print("Searching for wikipedia results")
results = wikipedia.search(query)
#print(results)

#pick the best answer
#threshold = 1/3 # the answer must have less than 50% in common with the question

queryWords = TextBlob(query).words
#print(queryWords)

print("Scoring wikipedia results")

resultAndScore = []
for i in range(len(results)):
    print(str(i + 1) + "/" + str(len(results)))
    result = results[i]
    wikiLinks = None
    try:
        wikipage = wikipedia.page(result)
        wikiLinks = wikipage.links
        #wikiContent = TextBlob(wikipage.content).words #wikipage.content
    except:
        print("Couldn't process '" + result + "'")
        continue
    #print()
    #exit()
    relatedTopics = [TextBlob(related.lower()).words for related in wikiLinks]
    queryWordSet = set(blob.words)
    total = 1 if POPULARITY else len(relatedTopics)
    score = sum([len(set(relatedTopic).intersection(queryWordSet)) for relatedTopic in relatedTopics]) / total
    #contentTotal = 1 if POPULARITY else len(wikiContent)
    #score += len(set(wikiContent).intersection(queryWordSet)) / contentTotal

    resultAndScore.append((result, score))

resultAndScore = sorted(resultAndScore, key=lambda x: x[1], reverse=True)
table = []
table.append(["Score", "Result"])
for result, score in resultAndScore:
    table.append([score, result])

from terminaltables import AsciiTable
termTable = AsciiTable(table)
print(termTable.table)