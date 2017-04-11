# -*- coding: utf-8 -*-
"""
Created on Wed Mar 09 22:13:47 2016

@author: Blithe
"""

import time
import urllib
import urllib2
import cookielib
import rsa
import binascii
import base64
import re

class SinaLogin:
    def __init__(self, username, password):
        self.u = username
        self.p = password
        
    def Login(self):
        self.bindCookie()
        result = self.preLogin()
        info = self.getPreLoginInfo(result)
        np = self.doEncode(info)
        cookie = self.getLoginCookie(info, np)
        return self.submitLogin(cookie)

    def bindCookie(self):
        cookiejar = cookielib.LWPCookieJar()
        cookie_sup = urllib2.HTTPCookieProcessor(cookiejar)
        opener = urllib2.build_opener(cookie_sup, urllib2.HTTPHandler)
        urllib2.install_opener(opener)
    
    """
    做一次预登录，得到包含服务器时间、随机码等信息的返回结果
    """    
    def preLogin(self):
        url = "http://login.sina.com.cn/sso/prelogin.php"
        payload = {
            "entry":"weibo",
            "callback":"sinaSSOController.preloginCallBack",
            "su":"",
            "rsakt":"mod",
            "client":"ssologin.js(v1.4.11)",
            "_":time.time()
        }
        payload = urllib.urlencode(payload)
        req = urllib2.urlopen(url, data=payload)
        return req.read()
    
    """
    从预登录返回的结果中提取出服务器时间、随机码等信息
    """
    def getPreLoginInfo(self, result):
        hm = {}
        result = result[result.find('{') + 1 : result.find('}')]
        r = result.split(',')
        temp = ''
        for i in range(len(r)):
            temp = r[i].split(":")
            for j in range(2):
                if '\"' in temp[j]:
                    temp[j] = temp[j][1 : len(temp[j]) - 1]
            hm[temp[0]] = temp[1]
        return hm
    
    """
    加密用户名和密码
    """
    def doEncode(self, hm):
        np = []
        uNameTemp = urllib.quote(self.u)
        uNameEncoded = base64.encodestring(uNameTemp)[:-1]
        np.append(uNameEncoded)
        
        rsaPubkey = int(hm['pubkey'], 16)
        #创建公钥
        key = rsa.PublicKey(rsaPubkey, 65537)
        #拼接明文js加密文件中得到
        message = str(hm['servertime']) + '\t' + str(hm['nonce']) + '\n' + str(self.p)
        #加密
        passwd = rsa.encrypt(message, key)
        #将加密信息转换为16进制
        passwd = binascii.b2a_hex(passwd)
        np.append(passwd)
        return np
    
    """
    进行二次登陆得到重定向的页面信息
    """
    def getLoginCookie(self, hm, np):
        url = "http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.11)"
        postHeader = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0"
        }
        postData = {
            "entry": "weibo",
            "gateway" : "1",
            "from" : "",
            "savestate" : "7",
            "userticket" : "1",
            "ssosimplelogin" : "1",
            "vsnf" : "1",
            "vsnval" : "",
            "su" : np[0],
            "service" : "miniblog",
            "servertime" : hm['servertime'],
            "nonce" : hm['nonce'],
            "pwencode" : "rsa2",
            "sp" : np[1],
            "encoding" : "UTF-8",
            "prelt" : "115",
            "rsakv" : hm['rsakv'],
            "url" : "http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack",
            "returntype" : "META"
        }
        postData = urllib.urlencode(postData)
        req = urllib2.Request(url, postData, postHeader)
        r = urllib2.urlopen(req)
        return r.read()
    
    """
    解析重定向中的登陆URL，并实现最后的登陆。如登陆成功，可以得到该用户的用户ID
    和Cookie
    """
    def submitLogin(self, cookie):
        p = re.compile('location\.replace\([\'"](.*?)[\'"]\)')
        loginUrl = p.search(cookie).group(1)
        try:
            urllib2.urlopen(loginUrl)
        except:
            return False
            
        return True
        
if __name__ == "__main__":
    url = "http://weibo.com/rmrb?refer_flag=0000015010_&from=feed&loc=nickname&is_all=1"
    sinaLogin = SinaLogin('evilfc@163.com', 'fclove1818')
    if sinaLogin.Login() == True:
        print "Login success!"
        htmlContent = urllib2.urlopen(url).read()
        print htmlContent
    else:
        print "Login failed!"