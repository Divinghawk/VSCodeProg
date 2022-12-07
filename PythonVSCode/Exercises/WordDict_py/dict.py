programmingwordsdict =  {
    "print" : "print is print",
    "strings" : "string is text",
    "variable" : "a container for a text or number",
    "comments" : "is a describing text or note for something",
    "if" : "is a statement for possibilities",
}

for a in range(len(programmingwordsdict)):
    print(([key for key in programmingwordsdict.keys()][a], [value for value in programmingwordsdict.values()] [a]))
print(" ")

programmingwordsdict.update({"else": "if statement reference"})
programmingwordsdict.update({"elif": "if statement reference"})   
programmingwordsdict.update({"container" : "for words and numbers"})
programmingwordsdict.update({"methods" : "compact programming"})
programmingwordsdict.update({"dictionaries" : "list of keys and values"})

for a in range(len(programmingwordsdict)):
    print(([key for key in programmingwordsdict.keys()][a] + ": " + [value for value in programmingwordsdict.values()][a]))