import json
from newsapi import NewsApiClient

newd={2:"two",1:"one",3:"three",6:"six",4:"four"}

a=json.dumps(newd,sort_keys=True)

print(a)

odic={values:key for key, values in newd.items()}
print(odic)
