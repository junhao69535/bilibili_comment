# -*- coding=utf-8 -*-
import urllib.request
import urllib.parse
import http.cookiejar
import urllib.error
import json
import time

def auto_comment(oid,message,cookie):    
    headers={
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': cookie,
        'Host': 'api.bilibili.com',
        'Origin': 'https://www.bilibili.com',
        'Referer': 'https://www.bilibili.com/video/av'+oid+'/?spm_id_from=333.334.home_popularize.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
        }
    url='https://api.bilibili.com/x/v2/reply/add'
    comment={
        'oid':oid,
        'type':'1',
        'message':message,
        'plat':'1',
        'jsonp':'jsonp',
        'csrf':'6e3a4a77eb11ba85d2321764935b7bb0'
        }
    postdata=urllib.parse.urlencode(comment).encode('utf-8')
    cj=http.cookiejar.CookieJar()
    opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    urllib.request.install_opener(opener)
    try:
        request=urllib.request.Request(url,headers=headers,data=postdata)
        response=opener.open(request)
    except urllib.error.URLError as e:
        if hasattr(e,'code'):
            print(e.code)
        if hasattr(e,'reason'):
            print(e.reason)
    
def get_new_video(uid):
    url='https://space.bilibili.com/ajax/member/getSubmitVideos?mid='+uid+'&page=1&pagesize=25'
    headers={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Host': 'space.bilibili.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    }
    try:
        request=urllib.request.Request(url,headers=headers)
        response=urllib.request.urlopen(request)
    except urllib.error.URLError as e:
        if hasattr(e,'code'):
            print(e.code)
        if hasattr(e,'reason'):
            print(e.reason)
    data=response.read()
    videodata=json.loads(data)
    av_number=videodata['data']['vlist'][0]['aid']
    first_video_time=videodata['data']['vlist'][0]['created']
    return (av_number,first_video_time)

cookie=input('请输入cookie:  ')
uid=input('请输入up空间的uid: ')
comment=input('请输入评论:  ')
nowtime=time.time()
while True:
    info=get_new_video(uid)
    if(info[1]>nowtime):
        auto_comment(str(info[0]),comment,cookie)
        break
    #每隔三分钟试一下
    time.sleep(360)
        
