import urllib.request
import json

#金山词霸的API的key
key = "B02371606E81A113AEB37D8DB0C5194E"
def getAllData(word):
    url = "http://dict-co.iciba.com/api/dictionary.php?w={}&key={}&type=json".format(word, key)
    response = urllib.request.urlopen(url).read().decode('utf8')
    getJson = json.loads(response)
    return getJson




if __name__ == '__main__':
    result=getAllData("e")
    if "word_name" in result:
        print("Y")
    else:
        print("N")


#如果单词可以在词霸中查询到,则会返回word_name属性,否则不返回,可以利用这一特性来判断单词的有无