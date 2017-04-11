import re,urllib2,urllib
import cookielib

def getopener(head):
    cj = cookielib.LWPCookieJar()
    cookie_support = urllib2.HTTPCookieProcessor(cj)
    header = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
    urllib2.install_opener(header)

    lit = []
    for key, value in head.items():
        tmp = (key, value)
        lit.append(tmp)
    header.addheaders = lit
    return header

url = 'https://passport.csdn.net/account/login'
quest = urllib2.Request(url)
page = urllib2.urlopen(quest).read()

pat = re.compile(r'name="lt" value="(.*)"[\s\S]*?name="execution" value="(.*)"[\s\S]*?name="_eventId" value="(.*?)"')
get = re.findall(pat, page)
lt = get[0][0]
exe = get[0][1]
submit = get[0][2]
print lt, exe, submit

id = '******@qq.com'
password = '*********'
postdict = {
    'username': id,
    'password': password,
    'lt': lt,
    'execution': exe,
    '_eventId':    submit
}
postdict = urllib.urlencode(postdict).encode()

head = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Origin':'https://passport.csdn.net',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/600.5.17 (KHTML, like Gecko) Version/8.0.5 Safari/600.5.17',
    'Content-Type':'application/x-www-form-urlencoded',
    'Referer':'https://passport.csdn.net/account/login?ref=toolbar'
}

opener = getopener(head)
login = opener.open(url, postdict).read()
yet = re.compile(r'该参数可以理解成每个需要登录的用户都有一个流水号')
flag = re.findall(yet, login)
print login
if len(flag) != 0:
    print 'fail'
else:
    print login