import requests
import os

def save_pdf(url, root):
    state = -1
    path = root + '/' + url.split('/')[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url)
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
                state = 2
                print("successfully saved")
        else:
            state = 1
            print("file already exists")

    except:
        print("failure!")
        state = 0
        
    return state

if __name__ == "__main__":
    url = "http://jwbinfosys.zju.edu.cn/wbwj/关于2021级本科新生第一学年秋冬学期选课的通知.pdf"
    root = "./pdfs"
    print(save_pdf(url, root))
