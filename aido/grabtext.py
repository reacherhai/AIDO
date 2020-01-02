# coding=utf-8
import re
from datetime import datetime
from aido.cn2num import chinese_to_arabic

def grabdate(text):
    text = text.strip()
    match = re.search(r'\d{4}年\d{1,2}月\d{1,2}日', text)
    if(not match):
        return ""
    #print(match.group())
    string = text #match.group()
    str1 = string.split("年")
    year = str1[0]
    str2 = str1[1].split("月")
    month = str2[0]
    day = str2[1].split("日")[0]
    final = year + "-" + month + "-" + day
    date = datetime.strptime(final, '%Y-%m-%d').date()
    return date

# text = "2020年2月10日上午十点去健身"
#print(grabdate(text))

def grabPriority(text):
    text = text.strip()
    index = text.find("优先级")
    if(index != -1):
        priority = int(text[index + 3])
        return priority
    else:
        return 0

def grabtext(text):
    text = text.strip()
    if(not grabdate(text)):
        return text
    else:
        return text.split("日")[1]

def grabdel(text):
    text = text.strip()
    match = re.search(r'删除',text)
    if(not match):
        return ""
    else:
        index = text.find("删除")+2
        substring = text[index:]
        substring = chinese_to_arabic(substring)
        return str(substring)
def getdel(text):
    text = text.strip()
    string = "todo done "
    if(grabdel(text)):
        string += grabdel(text)
    return string


def getcommand(text):
    text = text.strip()
    string = "todo add \""+grabtext(text)+"\""
    if(grabdate(text)):
        string += " --deadline "+ str(grabdate(text))
    if(grabPriority(text)):
        string += " --p " + str(grabPriority(text))
    return string

#todo add "fix the door" --deadline 2020-02-29