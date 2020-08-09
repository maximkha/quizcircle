# QuizCircle

Quizcircle is a one day project to see if I could design a non-ML system to answer quiz bowl questions using only basic NLP and wikipedia. 



#### Process

First I use TextBlob to extract POS (part of speech) tags for each word. Next, I collected an list of parts of speech, mostly nouns, that I thought would represent the content of the sentence. Then, the program queries the wikipedia api and collects the article titles. Finally, the articles are scored by links and counting the similarity between the page links and query.



#### Results

The system can answer basic questions like: 

```
Q: how many wonders of the ancient world are there
A: Seven Wonders of the Ancient World

Q: Name the Paris museum that houses the famous Greek marble statue entitled Victory of Samothrace
A: Louvre

Q: During this conflict, the territorial governor Charles Bent was scalped in the Taos Revolt
A: Mexican–American War

Q: A poem written in this language that contrasts a creature who knows one big thing with an animal
A: Out of the Silent Planet (WRONG)
Correct: Greek Language (Was not present on the ranking)

Q: This city was ruled by the Council of 104, which sent Hamilcar to conquer Sicily in 310 BC. 
A: Punic Wars (WRONG)
Correct: Ancient Carthage (This was ranked as the 2nd best answer)
```

However, this approach has a two huge issues when answering questions:

1. It can only answer Wikipedia article names. 
2. The algorithm doesn't understand the actuall query.

Since the algorithm doesn't understand the relational meaning of the query it only returns topics similar to the query. This is evident in the last question, the Punic Wars and Ancient Carthage are related but the question specifically asked about the city not the war.



#### Future Work

I belive the best next step for this kind of Q&A system is to use Machine Learning. 

I have two implementation ideas:

1. A pair of algorithms. The first would be the 'rough search' algorithm. It's purpose is to search through the raw text of Wikipedia, a downloaded verison, and to return the relavent page. This could possibly be a plain keyword search or machine learning based algorithm. The second algorithm would be the interpretation network. It would take in a page and the question and would provide an answer.
2. Somehow train an transformer to output SPARKQL query language and return the result. The tricky part of this algorithm is how to train it, since there is no dataset which maps natural language to Wikipedia SPARKQL queries. It's possible to use a reinforcement learning system and having it learn to write SPARKQL having the network directly output SPARKQL would most likely be very inneffecient, becuase SPARKQL is a complex query language and isn't very human-freindly because of how it represents entities.
