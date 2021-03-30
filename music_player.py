import tkinter
import pygame
import time
import mutagen
import  json
#from selenium import webdriver
from lxml import html
etree = html.etree
import os
from tkinter import filedialog
import threading
from PIL import Image,ImageTk
from io import StringIO,BytesIO
import requests
from one import one_png
import  base64
# coding = utf-8
#from bs4 import BeautifulSoup        # 用于解析网页源代码的模块
from binascii import b2a_hex, a2b_hex
from jsonpath import jsonpath
from Crypto.Cipher import AES
import requests                        # 用于获取网页内容的模块
import base64
import json
import inspect
import ctypes
#import ast
pygame.mixer.init()
#folder = ''
list = []
ret = []
dics = []
num = 0
dicc = []
playshow = False
playl = False
mmm = 1
kuwoshow = True
wangyi = False
zz = []

def breadclick(): #添加文件
    global folder
    global list
    global ret
    global num
    global playl
    global zz
    global t1
    global set
    num = 0
    var2.set([])
    folder = ''
    ret = []
    zz = []
    t1 = threading.Thread(target=test)
    t1.setDaemon(True)
    t1.start()
    folder = tkinter.filedialog.askdirectory()
    set = str(set)
    print(set)
    set = eval(set)
    set['folder'] = folder
    #set = str(set)
    #set = json.loads(set)
    #print(set['folder'])
    set = json.dumps(str(set))
    with open('./setting.json', 'w') as fp:
        fp.write(set)
    set = eval(set)
    list = [folder + '/' + music for music in os.listdir(folder) \
            if music.endswith(('.mp3','.flac','.wav','.ape','ogg'))]
    if len(list) != 0:
        for i in list:
            ret.append(i.split('/')[-1])

        var2.set(ret)
        musicName.set('正在播放中...')
        buttonpause['state'] = 'normal'
        buttonstart['state'] = 'normal'
        addb['state'] = 'normal'
        reduceb['state'] = 'normal'
    else:
        return


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)

def isplay(): #播放
    global num
    global  list
    global playshow
    global playl
    global mmm
    global ret
    global jishu
    global zz
    global t1
    playl = False
    nnn = 0
    print(num)
    #num = int(lb.curselection()[0])
    var4.set(ret[num].split('.')[0])
    music = list[num]
    label2['state'] = 'normal'
    down['state'] = 'disabled'
    audio = mutagen.File(music)
    m = list[num].replace('.' + list[num].split('.')[-1],'.lrc')
    if  os.path.exists(m) == True:
        f = open(m,encoding='utf-8', errors='ignore')
        y = f.read()
        musicLrcList = y.splitlines()
        z = []
        zz = []
        for i in range(8):
            z.append('')
        for lrcLine in musicLrcList:

            try:

                lrcLineList = '   {: ^30}\n'.format(lrcLine.split("]")[1])
                #lrcLineList = lrcLine.split("]")[1]
                zz.append(lrcLine.split(']')[0][1:].replace(':','.').replace('[',''))
                z.append(lrcLineList)
                z.append('')
            except:
                pass


        var3.set(z)
        t1 = threading.Thread(target=ly)
        t1.setDaemon(True)
        t1.start()
    else:
        pass
    d = list[num].split(' - ')[-1].split('.')[0]
    c = list[num].split(' - ')[0].split('/')[-1]
    j = '{}/{} - {}.jpg'.format(folder,c,d)
    if os.path.exists(j) == True:

        jpg = Image.open(str(j))
        jpg = jpg.resize((100,100),Image.ANTIALIAS)
        j = ImageTk.PhotoImage(jpg)
        label2.config(image=j)
        label2.image= j
        frame1['highlightthickness'] = 0
    else:
        pass


    pygame.mixer.music.load(music)
    # p = Process(target=ly)
    # p.daemon = True  # 1、必须在p.start()之前
    # p.start()
    while playshow:
        if not  pygame.mixer.music.get_busy():
            print('nnn=' + str(nnn))
            if mmm == 0:
                while playl:
                    i = 1
            else:
                if nnn == 0:
                    pygame.mixer.music.play()
                    nnn = 1
                else:
                    pygame.mixer.music.stop()
                    var3.set([])
                    start_cancel.set('播放')
                    playshow = False


        else:
            time.sleep(0.1)
    t1 = threading.Thread(target=test)
    t1.setDaemon(True)
    t1.start()
    var3.set([])

    #time.sleep(audio.info.length)
    print('ok')
def ly():
    global num
    global zz
    global mmm
    global nnn
    global playl
    global playshow
    music = list[num]
    audio = mutagen.File(music)
    # st = round(audio.info.length/50,1)
    #time.sleep(0.3)
    # for i in range(50):
    #     time.sleep(st)
    #     lb1.yview_moveto(i / 50)
    #     frame3.update()
    try:
        lb1.select_set(8)
    except:
        time.sleep(0.1)
    while playshow:
        if pygame.mixer.music.get_busy() == 1:
            for i in range(len(zz) - 1):
                frame3.update()
                timediff = float(zz[i + 1].split('.')[0])*60 + float(zz[i + 1].split('.')[1])*1+float('0.' + zz[i + 1].split('.')[2])- float(zz[i].split('.')[0])*60 - float(zz[i].split('.')[1])*1-float('0.' + zz[i].split('.')[2])
                #print(float(zz[0].split('.')[0]) * 60 + float(zz[0].split('.')[1]) * 1 + float('0.' + zz[0].split('.')[2]))
                if int(float(zz[0].split('.')[0])*60 + float(zz[0].split('.')[1])*1+float('0.' + zz[0].split('.')[2])) == 0:
                    print('第一行为0')
                    time.sleep(abs(round(float(timediff),1)))
                    lb1.yview_moveto(i/len(zz))
                    frame3.update()
                    if mmm == 0:
                        while playl:
                            i = 1
                    else:
                        #print(timediff)
                        lb1.select_clear(lb1.curselection())
                        lb1.select_set(10 + 2*i)
                else:
                    time.sleep(abs(round(float(timediff), 1)))
                    lb1.yview_moveto(i / len(zz))
                    frame3.update()
                    if mmm == 0:
                        while playl:
                            i = 1
                    else:
                        #print(timediff)
                        lb1.select_clear(lb1.curselection())
                        lb1.select_set(8 + 2 * i)
            while pygame.mixer.music.get_busy() == 1:
                time.sleep(0.1)
    print('ly ok')
def playing():
    global playshow
    global zz
    global t1
    if start_cancel.get() == '播放':
        playshow = True
        t = threading.Thread(target=isplay)
        t.setDaemon(True)
        t.start()
        start_cancel.set('取消')
    else:
        playshow = False
        pygame.mixer.music.stop()
        stop_thread(t1)
        zz = []
        var3.set([])
        start_cancel.set('播放')





def stops():
    global playl
    global mmm
    global nnn
    if pause_resume.get() == '暂停':
        mmm = 0
        pygame.mixer.music.pause()
        playl = True
        nnn = 10
        pause_resume.set('继续')
    else:
        playl = False
        mmm = 1
        pygame.mixer.music.unpause()
        pause_resume.set('暂停')
def control(sound): #音量
    t = threading.Thread(target=con,args=(sound,))
    t.setDaemon(True)
    t.start()
def con(sound):
    pygame.mixer.music.set_volume(float(sound))

def add(): #下一页
    global num
    global playshow
    global zz
    global t1
    playshow = False
    pygame.mixer.music.stop()
    stop_thread(t1)
    zz = []
    start_cancel.set('取消')
    var3.set([])
    time.sleep(0.1)
    if num != len(list) - 1:
        playshow = True
        num = num + 1
        #var3.set([])
        t = threading.Thread(target=isplay)
        t.setDaemon(True)
        t.start()
    else:
        playshow = True
        num = 0
        #var3.set([])
        t = threading.Thread(target=isplay)
        t.setDaemon(True)
        t.start()


def reduce(): #上一页
    global num
    global playshow
    global zz
    global t1
    playshow = False
    pygame.mixer.music.stop()
    stop_thread(t1)
    zz = []
    start_cancel.set('取消')
    var3.set([])
    time.sleep(0.1)
    if num != 0:
        playshow = True
        num = num - 1
        #var3.set([])
        t = threading.Thread(target=isplay)
        t.setDaemon(True)
        t.start()

    else:
        playshow = True
        num = len(list) - 1
        #var3.set([])
        t = threading.Thread(target=isplay)
        t.setDaemon(True)
        t.start()
def downloadyi(f):
    global downadd
    name = f['songname']
    singer = f['songer']
    id = f['songid']
    g = '{} - {}'.format(name,singer)
    url = 'http://music.163.com/song/media/outer/url?id=' + f['songid'] +'.mp3'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400'
    }
    response = requests.get(url=url, headers=headers).content
    with open(downadd + '/' + g +'.mp3','wb') as fp:
        fp.write(response)
    urll = 'http://music.163.com/api/song/lyric?id=' + str(id) + '&lv=1&kv=1&tv=-1'
    response = requests.get(url=urll, headers=headers)
    lrccc = response.json()['lrc']['lyric']
    with open(downadd + '/' + g + '.lrc','w', encoding='utf-8') as fp:
        fp.write(lrccc)
    urlll = 'https://music.163.com/song?id=' + str(id)
    texts = requests.get(url=urlll,headers=headers).text
    trees = etree.HTML(texts)
    u = trees.xpath('//img[@class="j-img"]/@src')[0]
    uu = requests.get(url=u,headers=headers).content
    with open(downadd + '/' + g + '.jpg', 'wb') as fp:
        fp.write(uu)
    down['state'] = 'disabled'
def test():
    while True:
        time.sleep(0.5)
t1 = threading.Thread(target=test)
t1.setDaemon(True)
t1.start()
def click(self): #点击播放
    global num
    global folder
    global dics
    global ret
    global playshow
    global zz
    global t1
    playshow = False
    pygame.mixer.music.stop()
    stop_thread(t1)
    zz = []
    start_cancel.set('取消')
    var3.set([])
    time.sleep(0.1)
    t1 = threading.Thread(target=test)
    t1.setDaemon(True)
    t1.start()

    if folder != '':
        playshow = True
        pygame.mixer.music.stop()
        num = int(lb.curselection()[0])
        var4.set(ret[num].split('.')[0])
        t = threading.Thread(target=isplay)
        t.setDaemon(True)
        t.start()
        start_cancel.set('取消')
    else:
        down['state'] = 'normal'
        num = int(lb.curselection()[0])
        e = dicc[num]
        name = e['songname']
        singer = e['songer']
        id = e['songid']
        dd = '{} - {}'.format(name, singer)
        var4.set(str(dd))
def downloads():
    global num
    global dicc
    global wangyi
    global kuwoshow
    e = dicc[num]
    changes()
    if kuwoshow == True:
    #t = threading.Thread(target=download,args=(e,))
        t = threading.Thread(target=downloadwo,args=(e,))
        t.setDaemon(True)
        t.start()
    if wangyi == True:
        t = threading.Thread(target=downloadyi, args=(e,))
        t.setDaemon(True)
        t.start()
def downloadwo(f):
    global downadd
    name = f['songname']
    singer = f['songer']
    id = f['songid']
    print(name,id,singer,f['jpg'])
    g = '{} - {}'.format(name, singer)
    url = 'http://www.kuwo.cn/url?format=mp3&rid='+ str(id).split('_')[1] + '&response=url&type=convert_url3&br=320kmp3&from=web&t=1614768006814&httpsStatus=1&reqId=d1e9e2f1-7c0c-11eb-9d26-e94e333a5f3d'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400'
    }
    response0 = requests.get(url=url, headers=headers).json()
    response1 = requests.get(url=response0['url'],headers=headers).content
    with open(downadd + '/' + g + '.mp3', 'wb') as fp:
        fp.write(response1)
    url = 'http://m.kuwo.cn/newh5/singles/songinfoandlrc?musicId='+ str(id).split('_')[1] + '&httpsStatus=1&reqId=8d072ac0-7be0-11eb-9329-05448107428f'
    response = requests.get(url=url, headers=headers).json()['data']['lrclist']
    for i in range(len(response)):
        b = response[i]['lineLyric']
        t = response[i]['time']
        if float(t) >= 60.00:
            d = float(t) // 60
            t = str(round(float(t) % 60, 2)).replace('.', ':')
            nowtime = '0{}:{}'.format(int(d), t)
        else:
            t = t.replace('.', ':')

            nowtime = '00:{}'.format(t)
        # print(nowtime)
        if len(nowtime.split(':')[1]) < 2:
            # print(len(nowtime.split(':')[1]))
            nowtime = nowtime.split(':')[0] + ':' + '0' + nowtime.split(':')[1] + ':' + nowtime.split(':')[2]
        nowlyric = '[' + nowtime + ']' + b
        with open(downadd+ '/' + g + '.lrc', 'a', encoding='utf-8') as fp:
            fp.write('{}\n'.format(nowlyric))
    if f['jpg'] != '':
        uu = requests.get(url=f['jpg'], headers=headers).content
        with open(downadd +'/'+ g + '.jpg', 'wb') as fp:
            fp.write(uu)
    else:
        pass
    down['state'] = 'disabled'

def get_params(forth_param, first_param):  # 获取params 参数的函数
    iv = "0102030405060708"
    first_key = forth_param
    second_key = 16 * 'F'
    h_encText = AES_encrypt(first_param, first_key, iv)
    h_encText = AES_encrypt(h_encText, second_key, iv)
    return h_encText


def get_encSecKey():
    encSecKey = "257348aecb5e556c066de214e531faadd1c55d814f9be95fd06d6bff9f4c7a41f831f6394d5a3fd2e3881736d94a02ca919d952872e7d0a50ebfa1769a7a62d512f5f1ca21aec60bc3819a9c3ffca5eca9a0dba6d6f7249b06f5965ecfff3695b54e1c28f3f624750ed39e7de08fc8493242e26dbc4484a01c76f739e135637c"
    return encSecKey


def AES_encrypt(text, key, iv):
    text = text.encode('utf-8')
    pad = 16 - len(text) % 16
    text = text + ( pad * chr(pad)).encode('utf-8')  # 需要转成二进制，且可以被16整除
    key = key.encode('utf-8')
    iv = iv.encode('utf-8')
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    encrypt_text = encryptor.encrypt(text)  # .encode('utf-8')
    encrypt_text = base64.b64encode(encrypt_text)
    return encrypt_text.decode('utf-8')


def get_json(url, params, encSecKey):
    data = {
        "params": params,
        "encSecKey": encSecKey
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400'
    }
    response = requests.post(url, headers=headers, data=data)
    return response.content


def handle_json(ressult_str):
    global ressult_b
    """通过request返回的json结果，对结果进行处理"""
    ressult_str = ressult_b.decode('utf-8')  # 结果转码为str类型
    json_text = json.loads(ressult_str)  # 加载为json格式
    i = 0
    L = []
    for i in range(len(jsonpath(json_text, '$..songs[*].id'))):  # 根据id获取列表条数
        D = {'num': 'null', 'name': 'null', 'id': 'null', 'singer':'null', 'song_sheet':'null'}  # 初始化字典
        D['num'] = i
        D['name'] = '/'.join(jsonpath(json_text, "$..songs["+str(i)+"].name"))  # 获取名称
        D['id'] = str(jsonpath(json_text, "$..songs["+str(i)+"].id")[0])  # 获取ID且获取第一个ID值并转化为str类型
        D['singer'] = '/'.join(jsonpath(json_text, "$..songs["+str(i)+"].ar[*].name"))  # 获取歌手列表
        al_list = jsonpath(json_text, "$..songs["+str(i)+"].al.name")  # 获取专辑列表
        al = '/'.join(al_list)  # 将获取的专辑列表合并
        D['song_sheet'] = "《" + al + "》"
        L.append(D)
    return L




def yi():
    global dics
    global dicc
    global ressult_b
    search_name =  word = entry.get()
    headers = {
        'Cookie': 'appver=1.5.0.75771;',
        'Referer': 'http://music.163.com/'
    }
    first_param = r'{"hlpretag":"<span class=\"s-fc7\">","hlposttag":"</span>","s":"' + search_name + r'","type":"1","offset":"0","total":"true","limit":"30","csrf_token":""}'
    second_param = "010001"
    third_param = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
    forth_param = "0CoJUm6Qyw8W8jud"
    url = "https://music.163.com/weapi/cloudsearch/get/web?csrf_token="
    params = get_params(forth_param,first_param)
    encSeckey = get_encSecKey()
    ressult_b = get_json(url, params, encSeckey)
    ressult_str = ressult_b.decode('utf-8')  # 结果转码为str类型
    json_text = json.loads(ressult_str)
    i = 0
    L = []
    for i in range(len(jsonpath(json_text, '$..songs[*].id'))):
        locals()['dic' + str(i)] = {}
        a = locals()['dic' + str(i)]
        try:
            a['songname'] = '/'.join(jsonpath(json_text, "$..songs["+str(i)+"].name"))  # 获取名称
            a['songer'] = '/'.join(jsonpath(json_text, "$..songs["+str(i)+"].ar[*].name"))
            a['songid'] = str(jsonpath(json_text, "$..songs["+str(i)+"].id")[0])

            b = '{}  {}'.format(a['songname'],a['songer'])
            dics.append(b)
            dicc.append(a)
        except:
            pass
    var2.set(dics)
# def yis():
#     global dics
#     global dicc
#     headers = {'User-Agent':
#                    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3830.400'
#                }
#     word = entry.get()
#     url = 'https://music.163.com/#/search/m/?s=' + str(word) + '&type=1'
#     option = webdriver.ChromeOptions()
#     option.add_argument('headless')
#     bro = webdriver.Chrome(executable_path='./chromedriver.exe', options=option)
#
#     bro.get(url)
#     bro.switch_to_frame('g_iframe')
#     tree = etree.HTML(bro.page_source)
#     songer = tree.xpath('.//div[@id="m-search"]//div[@class="srchsongst"]/div//div[@class="td w1"]//a/text()')[0:]
#     songid = tree.xpath('.//div[@id="m-search"]//div[@class="srchsongst"]/div//div[@class="hd"]/a/@data-res-id')[0:]
#     songname = tree.xpath('.//div[@id="m-search"]//div[@class="srchsongst"]/div//div[@class="td w0"]//b/@title')[0:]
#     for i in range(len(songname)):
#         locals()['dic' + str(i)] = {}
#         a = locals()['dic' + str(i)]
#         print(i)
#         try:
#             a['songname'] = songname[i]
#             a['songer'] = songer[i]
#             a['songid'] = songid[i]
#
#             b = '{}  {}'.format(a['songname'],a['songer'])
#             dics.append(b)
#             dicc.append(a)
#         except:
#             pass
#     bro.quit()
#     var2.set(dics)

def wo():
    global dics
    global dicc
    word = entry.get()
    url = 'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key='+ str(word) +'&pn=1&rn=30&httpsStatus=1&reqId=82930e40-7bd8-11eb-81e5-5f72d2c3997c'
    headers = {
        'Referer': 'http://www.kuwo.cn/search/list?',
        'Cookie': 'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1614745495; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1614745495; _ga=GA1.2.1632744997.1614745496; _gid=GA1.2.135366005.1614745496; _gat=1; kw_token=JSOMCXTIQ09',
        'csrf': 'JSOMCXTIQ09',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400'
    }
    response = requests.get(url=url, headers=headers).json()['data']['list']
    for i in range(len(response)):
        locals()['dic' + str(i)] = {}
        a = locals()['dic' + str(i)]
        a['songname'] = response[i]['name']
        a['songer'] = response[i]['artist']
        a['songid'] = response[i]['musicrid']
        try:
            a['jpg'] = response[i]['pic']
        except:
            a['jpg'] = ''
        b = '{}  {}'.format(a['songname'], a['songer'])
        dics.append(b)
        dicc.append(a)
    var2.set(dics)

def sousuo():
    global num
    global folder
    global dics
    global dicc
    global wangyi
    global kuwoshow
    global zz
    global t1
    pygame.mixer.music.stop()
    stop_thread(t1)
    zz = []
    start_cancel.set('播放')
    t1 = threading.Thread(target=test)
    t1.setDaemon(True)
    t1.start()
    num = 0
    folder = ''
    var2.set([])
    var3.set([])
    dics = []
    dicc = []
    down['state'] = 'normal'
    label2['state'] = 'disabled'
    if kuwoshow == True:
        t = threading.Thread(target=wo)
        t.setDaemon(True)
        t.start()
    if wangyi == True:
        t = threading.Thread(target=yi)
        t.setDaemon(True)
        t.start()

def r2():
    global wangyi
    global kuwoshow
    kuwoshow = True
    wangyi = False
def r1():
    global wangyi
    global kuwoshow
    kuwoshow = False
    wangyi = True

def changes():
    global downadd
    global set
    if downadd == '':
        downadd = tkinter.filedialog.askdirectory()
        var5.set(downadd)
        #set = json.loads(set)
        set['downadd'] = downadd
        set = json.dumps(set)
        with open('./setting.json', 'w') as fp:
            fp.write(set)
        #set = json.loads(set)
    else:

        pass
root = tkinter.Tk()
root.title('音乐播放器')
w = int((root.winfo_screenwidth() - 600)/2)
h = int((root.winfo_screenheight() - 500)/2)
root.geometry("600x500+%d+%d" % (w,h)) #长和宽
root.resizable(False,False)



tmp = open('one.png', 'wb')        #创建临时的文件
tmp.write(base64.b64decode(one_png))    ##把这个one图片解码出来，写入文件中去。
tmp.close()

photo = ImageTk.PhotoImage(Image.open('one.png'))
label1 = tkinter.Label(root, image=photo)  # 图片标签
label1.pack(fill=tkinter.BOTH)

os.remove('one.png')
buttonread = tkinter.Button(root,text='添加',command=breadclick)#添加按钮
buttonread.place(x=30,y=25,width=30,height=20)

start_cancel = tkinter.StringVar(root,value='播放')
buttonstart = tkinter.Button(root,textvariable=start_cancel,command=playing)#播放按钮
buttonstart.place(x=75,y=25,width=30,height=20)
buttonstart['state'] = 'disabled'

pause_resume = tkinter.StringVar(root,value='暂停')
buttonpause = tkinter.Button(root,textvariable=pause_resume,command=stops)#暂停按钮
buttonpause.place(x=75,y=55,width=30,height=20)
buttonpause['state'] = 'disabled'

musicName = tkinter.StringVar(root,value='暂时没有播放音乐...')
labelName = tkinter.Label(root,textvariable=musicName)#音乐状态
labelName.place(x=25,y=150,width=120,height=20)
sound = tkinter.StringVar(root,value=0.3)
s = tkinter.Scale(root,label='音量',from_=0,to=1,orient=tkinter.HORIZONTAL,length=100,resolution=0.02,\
                  sliderlength=10,width=10,sliderrelief='ridge',borderwidth=1,\
                  foreground='black',font='宋体 10',\
                  highlightbackground='blue',command=control,variable=sound)
s.place(x=10,y=80,width=120)
addb = tkinter.Button(root,text='+',command=add) #下一页
addb.place(x=120,y=30,width=15,height=14)
addb['state'] = 'disabled'

reduceb = tkinter.Button(root,text='-',command=reduce) #上一页
reduceb.place(x=120,y=57,width=15,height=14)
reduceb['state'] = 'disabled'

frame1 = tkinter.Frame(root,highlightthickness=1,relief='sunken',highlightbackground='yellow') #图片框架
frame1.place(x=150,y=25,width=100,height=100)

label2 = tkinter.Label(frame1)  # 图片标签
label2.pack(fill=tkinter.BOTH, expand='no')

frame2 = tkinter.Frame(root) #列表框架
frame2.place(x=20, y=150, width=120, height=200)


sb = tkinter.Scrollbar(frame2) #垂直滑动条
sb.pack(side=tkinter.RIGHT,fill=tkinter.Y)

sc = tkinter.Scrollbar(frame2,orient='horizontal',width=10) #水平滑动条
sc.pack(side=tkinter.BOTTOM,fill=tkinter.X)

var2 = tkinter.StringVar()
lb = tkinter.Listbox(frame2, listvariable=var2,yscrollcommand=sb.set,xscrollcommand=sc.set) #列表
lb.bind(func=click,sequence='<Double-Button-1>')
lb.pack(side=tkinter.LEFT,fill=tkinter.BOTH,expand=True)

sb.config(command=lb.yview)
sc.config(command=lb.xview)

entry = tkinter.Entry(root) #输入框
entry.place(x=10,y=400,width=100,height=20)

search = tkinter.Button(root,text='->',font='5',command=sousuo) #搜索按钮
search.place(x=120,y=400,width=20,height=20)

down = tkinter.Button(root,text='下载',font='黑体 10',command=downloads) #下载按钮
down.place(x=500,y=63,width=30,height=20)

frame3 = tkinter.Frame(root)            #歌词框架
frame3.place(x=150,y=150,width=380,height=270)

sb1 = tkinter.Scrollbar(frame3) #垂直滑动条
sb1.pack(side=tkinter.RIGHT,fill=tkinter.Y)

var3 = tkinter.StringVar()
lb1 = tkinter.Listbox(frame3,listvariable=var3,yscrollcommand=sb1.set,font='黑体 12',selectforeground='green',selectmode='browse',selectbackground='white')  #歌词
lb1.pack(side=tkinter.LEFT,fill=tkinter.BOTH,expand=True)

sb1.config(command=lb1.yview)

var4 = tkinter.StringVar(root)
label4 = tkinter.Label(root, textvariable=var4)  # 下载音乐
label4.place(x=360, y=63, width=120, height=20)
v = tkinter.IntVar()
R1 = tkinter.Radiobutton(root,text='网易云',bg='white',variable=v,value=1,command=r1)#接口按钮
R1.place(x=10,y=370,width=55,height=20)

R2 = tkinter.Radiobutton(root,text='酷我',bg='white',variable=v,value=2,command=r2)#接口按钮
R2.place(x=75,y=370,width=55,height=20)
R2.select()

change = tkinter.Button(root,text='^',command=changes)#添加按钮
change.place(x=120,y=430,width=20,height=20)

var5 = tkinter.StringVar(root)
label5 = tkinter.Label(root, textvariable=var5)  # 下载音乐
label5.place(x=10, y=430, width=100, height=20)
def jiazai():
    global set
    global downadd
    global folder
    global list
    global ret
    global num
    global playl
    global zz
    global t1
    try:
        with open('./setting.json') as fp:
            set = json.load(fp)
        set = eval(set)
        folder = set['folder']
        downadd = set['downadd']
        var5.set(downadd)
        num = 0
        var2.set([])
        # folder = ''
        ret = []
        zz = []
        t1 = threading.Thread(target=test)
        t1.setDaemon(True)
        t1.start()
        # folder = tkinter.filedialog.askdirectory()
        list = [folder + '/' + music for music in os.listdir(folder) \
                if music.endswith(('.mp3', '.flac', '.wav', '.ape', 'ogg'))]
        if len(list) != 0:
            for i in list:
                ret.append(i.split('/')[-1])

            var2.set(ret)
            musicName.set('正在播放中...')
            buttonpause['state'] = 'normal'
            buttonstart['state'] = 'normal'
            addb['state'] = 'normal'
            reduceb['state'] = 'normal'
        else:
            pass


    except:
        set = json.dumps("{'folder':'','downadd':''}")
        with open('./setting.json','w') as fp:
            fp.write(set)
        with open('./setting.json') as fp:
            set = json.load(fp)
            set = eval(set)
        folder = set['folder']
        downadd = set['downadd']
        var5.set(downadd)


t = threading.Thread(target=jiazai)
t.setDaemon(True)
t.start()



root.mainloop()
