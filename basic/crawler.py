import urllib.request as req
import bs4
def web_crawler():
    import urllib.request as req
    from bs4 import BeautifulSoup

    url = "https://www.ptt.cc/bbs/Gossiping/index.html"
    payload = {
        'from': '/bbs/Gossiping/index.html',
        'yes': 'yes'
    }
    request = req.Request(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"})
    with req.urlopen(request) as response:
        data  = response.read().decode("utf-8")
    print (data)
    root = bs4.BeautifulSoup(data,"html.parser")
    title = root.find_all("div", class_ = "p")
    print(root.title.string)
if __name__ == "__main__":
    web_crawler()
