import requests
import json

token_url = ''
payload = {'':'','':''}
header = {'Content-Type':'application/json'}
res = requests.post(token_url,json=payload,headers=header)
token = res.json("token")
#取响应中的cookie
res.cookies

#获取token后和下一个接口做关联 token一般在响应体中返回 通过账号密码得到
header = {'X-AUTH-TOKEN':token}
add_url = ''
payload = {'':''}
res = requests.post(add_url,json=payload,headers=header)

"""
文件上传接口 
Content-Type:multipart/form-data(文件表单格式)
请求消息体：jpg/png/gif
请求头：cookie:token=通过获取token的接口获取
密码需要加密 md5('zr'+ 密码 +'hg')
"""
import hashlib#算法库
#创建对象 按照上面的格式进行迦密 然后以16进制的形式进行输出 此处的b不可省略
psw = hashlib.md5(b'zr111111hg').hexdigest()
print(psw)
#payload参数中有加密参数
token_url = ""
# 密码需要md5加密
payload = {'mobile':'18516418695','password':psw}
#token放在cookie中进行传递
cookie = {'token':token}
#文件上传中的payload 文件名字 文件对象
fileload = {'file':('logo.png',open(r'文件绝对路径','rb'),'jpg/png/gif')}
res = requests(token_url,files=fileload,cookies=cookie)


