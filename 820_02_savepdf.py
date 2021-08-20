import requests
import os

url = "http://jwbinfosys.zju.edu.cn/wbwj/关于2021级本科新生第一学年秋冬学期选课的通知.pdf"
root = "./pdfs/"
path = root + url.split('/')[-1]

try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("successfully saved")
    else:
        print("file already exists")

except:
    print("failure!")
