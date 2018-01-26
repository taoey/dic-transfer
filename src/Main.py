import pymysql
import urllib.request
import json
import re
import time
from pymongo import MongoClient

#金山词霸的API的key
key = "B02371606E81A113AEB37D8DB0C5194E"
def getAllData(word):
    url = "http://dict-co.iciba.com/api/dictionary.php?w={}&key={}&type=json".format(word, key)
    response = urllib.request.urlopen(url).read().decode('utf8')
    getJson = json.loads(response)
    return getJson

def getMysqlWords():
    # 获取MySQL中的单词数据
    Mysqlwords=[]
    db = pymysql.connect("localhost", "root", "12345678", "dic")
    cursor = db.cursor()
    sql = "SELECT * FROM english LIMIT 69191,20000"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            word = row[0]
            Mysqlwords.append(word)
    except:
        print("Error: unable to fecth data")
    db.close()
    return Mysqlwords


def main():
    # ---------------获取MySQL中的单词数据-------------
    mysqlWords=getMysqlWords()
    #print(mysqlWords)
    # ---------------连接MongoDB数据库-------------
    client = MongoClient()
    db = client.Taoey
    #----------------请求金山词霸API,保存数据到MongoDB中--------------
    count=0
    fw = open("../log/log.txt", "a+",encoding="UTF-8")
    startTime=time.time()
    fw.write("---------------------------------------------------------"+"\n")
    for word in mysqlWords:
        wordData=getAllData(word)
        if "word_name" in wordData:
            db.endic.insert_one(wordData)
            fw.write("{}单词:{}插入成功".format(count,word) + "\n")

            print("{}单词:{}插入成功".format(count,word))
        count+=1
        if(count%150==0):
            time.sleep(5)
            fw.write("---------------------睡眠5秒-----------------------"+"\n")
            print("---------------------睡眠5秒-----------------------")
    endTime=time.time()
    fw.write("用时:{}".format(endTime-startTime) + "\n")
    print("用时:{}".format(endTime-startTime) + "\n")
    fw.close()





if __name__ == '__main__':
    main()