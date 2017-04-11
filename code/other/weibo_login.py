# -*- coding: utf-8 -*-
import urllib.request as request
import urllib.parse as parse
import string
import re
import os
import urllib.error as error
import urllib

def fetch(baseUrl):  
  
    # 第1步：模拟浏览器发送请求  
    response = urllib.request.urlopen(baseUrl)    
    data = response.read()
    data=data.decode('utf-8')    
  
    # 第2步：页面返回后，利用正则表达式提取想要的内容  
    nameList=[]  
    nameList = re.compile(r'】(.*?)<\/div>\n',re.DOTALL).findall(data)
  
    # 第3步：返回在页面上析取的“标题名”  
    return nameList

#######     执行    ########   
if __name__ =="__main__": 
    #要抓取的网页地址  
    url = "http://weibo.com/rmrb?refer_flag=0000015010_&from=feed&loc=nickname&is_all=1"
    #存放到名字列表中  
    NameList = fetch(url)  
  
    # 输出 NameList  
    Length = len(NameList)  
    for i in range(0, Length):  
        print ('%d ref is:%s' %(i+1, NameList[i]))
with open('E:/graduate_project/code/other/hehe.txt', 'a') as f:
	for i in range(0,Length):
		f.write("\n")
		f.write(NameList[i])