#coding=utf-8
import json
import re
from pymongo import MongoClient


data="{'symbols': [{'ph_other': '', 'ph_am_mp3': 'http://res.iciba.com/resource/amp3/1/0/c4/7d/c47d187067c6cf953245f128b5fde62a.mp3', 'ph_am': 'wɜrd', 'ph_en_mp3': 'http://res.iciba.com/resource/amp3/0/0/c4/7d/c47d187067c6cf953245f128b5fde62a.mp3', 'parts': [{'part': 'n.', 'means': ['单词', '话语', '诺言', '消息']}, {'part': 'vt.', 'means': ['措辞，用词', '用言语表达']}, {'part': 'vi.', 'means': ['讲话']}], 'ph_en': 'wɜ:d', 'ph_tts_mp3': 'http://res-tts.iciba.com/c/4/7/c47d187067c6cf953245f128b5fde62a.mp3'}], 'items': [''], 'word_name': 'word', 'exchange': {'word_past': ['worded'], 'word_est': '', 'word_ing': ['wording'], 'word_done': ['worded'], 'word_third': ['words'], 'word_pl': ['words'], 'word_er': ''}, 'is_CRI': 1}"

#连接数据库
data=re.sub('\'','\"',data)
data = json.loads(data)
client=MongoClient()
db=client.Taoey
db.endic.insert_one(data)











