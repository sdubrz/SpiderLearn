# 在京东上爬取图片

import re
import urllib.request as request


def craw(url, page):

    html1 = request.urlopen(url).read().decode('utf-8')
    html1 = str(html1)
    # print(url)
    # print(html1)
    # pattern1 = '<div id="plist"(.+?)<div class="page clearfix">'
    pattern1 = '<div id="plist"((.|\n)+?)<div class="page clearfix">'
    goods = re.compile(pattern1).findall(html1)
    goods = goods[0]
    goods = goods[0]
    # print(goods)

    item_pattern = '<li class="gl-item">(.|\n)*</li>'
    compute_list = re.compile(item_pattern).findall(goods)
    # compute_list = compute_list0.search(goods).group()
    print(len(compute_list))

    index = 1
    for compute in compute_list:
        # print(compute)
        # 提取图片
        image_pattern = '<img width="220" height="220" data-img="1" src="//.+?\.jpg)'
        image_url = re.compile(image_pattern).findall(compute)
        print(image_url)
        image_url = image_url[0]
        image_url = "http://" + image_url  # 图片网址
        # print(image_url)

        # 提取价格
        # price_div_pattern = '<div class="p-price">(.+?)</strong>'
        # price_div_pattern2 = '<i>.+?<i>'
        # price_div = re.compile(price_div_pattern).findall(compute)
        # print(price_div)
        # price_div2 = re.compile(price_div_pattern2).findall(compute)
        # print(price_div2)

        # 提取商品名称
        name_div_pattern = '<div class="p-name">(.+?)</div>'
        name_div = re.compile(name_div_pattern).findall(compute)
        name_div = name_div[0]
        # name_div.encode('UTF-8')
        print(name_div)

        index += 1
        break


def run():
    url = "https://list.jd.com/list.html?cat=670,671,672&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main"
    craw(url, 1)


if __name__ == '__main__':
    run()
