import time
import os
import requests
import json
from aido.config import *
from aido.recorder import Recorder
import random
import urllib.request
import base64

# 获取百度API调用的认证，实时生成，因为有时间限制
def getToken():
    # token认证的url
    api_url = "https://openapi.baidu.com/oauth/2.0/token?" \
                     "grant_type=client_credentials&client_id=%s&client_secret=%s"
    token_url = api_url % (BaiDu_API_Key_GetVoi, BaiDu_Secret_Key_GetVoi)
    r_str = urllib.request.urlopen(token_url).read()
    token_data = json.loads(r_str)
    token_str = token_data['access_token']
    return token_str

class ChatBot(object):
    def __init__(self):
        self.name = "AIDO"
        if not os.path.exists("voices"):
            os.makedirs("voices")
        self.voice_url = r'voices/voice_ss.mp3'
        self.recorder = Recorder()

    def get_data(self,text):
    # 请求思知机器人API所需要的一些信息
        data = {
            "appid": "96e172cabcf3b21089395c484b65668e",
            "userid": "BluqL2PT",
            "spoken": text,
        }
        return data

    def get_response(self,text,voice_flag=False):
        if not voice_flag:
            data = self.get_data(text)
        else:
            self.recording()
            text = self.voice2text()
            data = self.get_data(text)
        url = 'https://api.ownthink.com/bot'
        response = requests.post(url=url, data=data, headers=headers)
        response.encoding = 'utf-8'
        result = response.json()
        answer = result['data']['info']['text']
        answer = answer.replace('小思','小海')
        return answer

    def text2voice(self,answer):
        # 获取access_token
        token = getToken()
        get_url = baidu_api_url2 % (urllib.parse.quote(answer), "test", token)
        voice_data = urllib.request.urlopen(get_url).read()
        # 本地Mp3语音文件保存位置
        name = random.randrange(1, 99999)
        global voice_url
        voice_url = r'voice_tsn' + str(name) + '.mp3'
        voice_fp = open(voice_url, 'wb+')
        voice_fp.write(voice_data)
        voice_fp.close()
        return

    def recording(self):
        self.recorder.recording(self.voice_url)

    def voice2text(self):
        # 获取access_token
        token = getToken()
        data = {}
        data['format'] = 'wav'
        data['rate'] = 16000
        data['channel'] = 1
        data['cuid'] = str(random.randrange(123456, 999999))
        data['token'] = token
        wav_fp = open(self.voice_url, 'rb')
        voice_data = wav_fp.read()
        data['len'] = len(voice_data)
        data['speech'] = base64.b64encode(voice_data).decode('utf-8')
        post_data = json.dumps(data)
        # 语音识别的api url
        upvoice_url = 'http://vop.baidu.com/server_api'
        r_data = urllib.request.urlopen(upvoice_url, data=bytes(post_data, encoding="utf-8")).read()
        print(json.loads(r_data))
        err = json.loads(r_data)['err_no']
        if err == 0:
            return json.loads(r_data)['result'][0]
        else:
            return json.loads(r_data)['err_msg']

# # 播放Mp3文件
# def play_mp3():
#     # 接受服务器的消息
#     pygame.mixer.init()
#     pygame.mixer.music.load(voice_url)
#     pygame.mixer.music.play()
#     while pygame.mixer.music.get_busy():
#         time.sleep(1)
#     pygame.mixer.music.stop()
#     pygame.mixer.quit()


# # 删除声音文件
# def remove_voice():
#     path = r"voices"
#     for i in os.listdir(path):
#         path_file = os.path.join(path, i)
#         try:
#             os.remove(path_file)
#         except:
#             continue

# # 百度讲文本转为声音文件保存在本地 tts地址，无需token实时认证
# def baidu_api(answer):
#     api_url = '{11}?idx={0}&tex={1}&cuid={2}&cod={3}&lan={4}&ctp={5}&pdt={6}&spd={7}&per={8}&vol={9}&pit={10}'\
#         .format(baidu_api_set["idx"], answer, baidu_api_set["cuid"], baidu_api_set["cod"], baidu_api_set["lan"],
#                 baidu_api_set["ctp"], baidu_api_set["pdt"], baidu_api_set["spd"], baidu_api_set["per"],
#                 baidu_api_set["vol"], baidu_api_set["pit"], baidu_api_url)
#     res = requests.get(api_url, headers=headers2)
#     # 本地Mp3语音文件保存位置
#     iname = random.randrange(1, 99999)
#     global voice_url
#     voice_url = r'voice_say/voice_tts' + str(iname) + '.mp3'
#     with open(voice_url, 'wb') as f:
#         f.write(res.content)