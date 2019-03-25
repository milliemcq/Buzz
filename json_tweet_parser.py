import json
import re
from pymongo import MongoClient


#NEED TO CREATE database here
MONGO_HOST= 'mongodb://localhost/musicaltweetdb'

client = MongoClient()

#shameless copy paste from json/decoder.py
FLAGS = re.VERBOSE | re.MULTILINE | re.DOTALL
WHITESPACE = re.compile(r'[ \t\n\r]*', FLAGS)

class ConcatJSONDecoder(json.JSONDecoder):
    def decode(self, s, _w=WHITESPACE.match):
        s_len = len(s)

        objs = []
        end = 0
        while end != s_len:
            obj, end = self.raw_decode(s, idx=_w(s, end).end())
            end = _w(s, end).end()
            objs.append(obj)

        print(objs)
        return objs

data_list = json.load(open('Buzz_Data_Final.txt'), cls=ConcatJSONDecoder)



info_list = []
for item in data_list:
 print("CREATED AT")
 print(item['created_at'])
 print()
 print("TEXT")
 print(item['text'])
 print()
 print(item['place'])
 print()
 print("USERT")
 print(item['user'])
 print()
 print("ENTITIES")
 print(item["entities"])