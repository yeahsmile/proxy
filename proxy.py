import urllib
import urllib2
import re

url = "http://cn-proxy.com/"
#抓取代理服务器的ip地址，端口号，位置
request = urllib2.Request(url)
content = urllib2.urlopen(request).read()
pattern = re.compile('<tr>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<div',re.S)
items = re.findall(pattern,content)
#print "ip地址列表为："
#用来存储可用代理服务器的列表
usable = []
#用来存储不可用代理服务器的列表
unusable = []
#检测代理服务器是否有效
print "检测中(需要2-5分钟)......"
for i in items:
    proxyHandler = urllib2.ProxyHandler({"http":'http://%s:%s' % (i[0],i[1])})
    opener = urllib2.build_opener(proxyHandler)
    urllib2.install_opener(opener)
    try:
        
        con = urllib2.urlopen('http://www.baidu.com',timeout=5).read()
        usable.append(i)
    except Exception,e:
        unusable.append(i)
        continue
    #print i[0],i[1],i[2].decode('utf-8')
print "可用的代理服务器%d个：" % len(usable)
for i in usable:
    print i[0],i[1],i[2].decode('utf-8')
print "-----------------------------------------"
print "不可用的代理服务器%d个：" % len(unusable)
for i in unusable:
    print i[0],i[1],i[2].decode('utf-8')
    
