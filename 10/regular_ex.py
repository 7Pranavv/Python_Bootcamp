import re 
text = "The rain in the Spain."

match= re.search("Spain", text)
matches=re.findall("the",text,re.IGNORECASE)

new_text = re.sub("Spain", "France", text)
print(new_text)

if match:
    print("Match found:")
    print("Start index:", match.start())
    print("End index:", match.end()) 
print(matches)
