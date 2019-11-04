import urllib.request as request
import urllib


path = "E:\\Project\\Spider\\test\\"  # 华硕
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"


def test():
    """尝试下载一个网页"""
    file = request.urlopen("https://blog.csdn.net/john_bian/article/details/74502323")
    data = file.read()
    f_handle = open(path+"blog2.html", "wb")
    f_handle.write(data)
    f_handle.close()
    # print("存储网页成功")


def test2():
    """
    伪装成浏览器
    :return:
    """
    url = "https://blog.csdn.net/john_bian/article/details/74502323"
    header = ("User-Agent", user_agent)
    opener = request.build_opener()
    opener.addheaders = [header]
    data = opener.open(url).read()
    f_handle = open(path + "blog_article.html", "wb")
    f_handle.write(data)
    f_handle.close()
    # print("存储网页成功")


def test3():
    """
    测试使用代理服务器进行爬取
    :return:
    """
    print("开始爬取")
    proxy_addr = "113.120.35.96:9999"
    url = "https://blog.csdn.net/john_bian/article/details/74502323"
    proxy = request.ProxyHandler({'http': proxy_addr})
    opener = urllib.request.build_opener(proxy, request.HTTPHandler)
    request.install_opener(opener)
    data = request.urlopen(url).read()
    print(data)

    f_handle = open(path + "blog_article2.html", "wb")
    f_handle.write(data)
    f_handle.close()
    print("存储网页成功")
    print(len(data))


if __name__ == '__main__':
    print('这里')
    test3()
