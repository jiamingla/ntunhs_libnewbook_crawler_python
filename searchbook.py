import json
import string
booklist_read = []
i=0
with open('newbooks.json', 'r', encoding='utf-8') as f:
    booklist_read = json.load(f)

string = '成為自己'
for l1 in booklist_read:
    if (l1[1].lower().find(string.lower()) >=0 ):
        print(l1[1])