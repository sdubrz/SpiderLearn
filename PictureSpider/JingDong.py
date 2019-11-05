# 在京东上爬取图片

import re
import urllib.request as request
import urllib


def craw(url, page, save_path):
    """
    爬取京东笔记本电脑的图片和名称
    :param url: 网址
    :param page:
    :param save_path: 存储路径
    :return:
    """
    html1 = request.urlopen(url).read().decode('utf-8')
    pattern1 = '<div id="plist"((.|\n)+?)<div class="page clearfix">'
    goods = re.compile(pattern1).findall(html1)
    goods = goods[0]
    goods = goods[0]

    item_pattern = '<li class="gl-item">((.|\n)+?)</li>'
    compute_list = re.compile(item_pattern).findall(goods)

    index = 1
    for compute in compute_list:
        try:
            compute_str = compute[0]
            # 提取图片
            image_pattern = '<img width="220" height="220" data-img="1" src="//(.+?\.jpg)'
            image_url = re.compile(image_pattern).findall(compute_str)
            image_url = image_url[0]
            image_url = "http://" + image_url  # 图片网址

            # 提取商品名称
            name_div_pattern = '<div class="p-name">((.|\n)+?)</div>'
            name_div = re.compile(name_div_pattern).findall(compute_str)
            name_div = name_div[0]
            name_div_str = name_div[0]
            name_pattern = '<em>\n(.+?)</em>'
            name = re.compile(name_pattern).findall(name_div_str)
            name = name[0]

            image_path = save_path + "Page" + str(page) + "-" + str(index) + name + ".jpg"
            try:
                request.urlretrieve(image_url, filename=image_path)
            except urllib.error.URLError as e:
                if hasattr(e, "code"):
                    index += 1
                if hasattr(e, "reason"):
                    index += 1
        except Exception as e:
            continue

        index += 1


def craw0(url, page, save_path):
    """
    爬取京东上的笔记本电脑图片
    :param url:
    :param page:
    :param save_path: 保存路径
    :return:
    """
    html1 = request.urlopen(url).read()
    html1 = str(html1)
    # print(url)
    # print(html1)
    # pattern1 = '<div id="plist"(.+?)<div class="page clearfix">'
    pattern1 = '<div id="plist".+?<div class="page clearfix">'
    goods = re.compile(pattern1).findall(html1)
    goods = goods[0]

    item_pattern = '<li class="gl-item">.+?</li>'
    compute_list = re.compile(item_pattern).findall(goods)

    index = 1
    for compute in compute_list:
        # 提取图片
        try:
            image_pattern = '<img width="220" height="220" data-img="1" src="//(.+?\.jpg)'
            image_url = re.compile(image_pattern).findall(compute)
            image_url = image_url[0]
            image_url = "http://" + image_url  # 图片网址
            image_path = save_path + "Page" + str(page) + "-" + str(index) + ".jpg"

            try:
                request.urlretrieve(image_url, filename=image_path)
            except urllib.error.URLError as e:
                if hasattr(e, "code"):
                    index += 1
                if hasattr(e, "reason"):
                    index += 1
        except Exception as e:
            continue

        index += 1


def run0():
    url = "https://list.jd.com/list.html?cat=670,671,672&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main"
    save_path = "E:\\Project\\Spider\\JDcomputes\\"

    for i in range(1, 966):
        url = "https://list.jd.com/list.html?cat=670,671,672&page=" + str(i)
        url = url + "&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main"
        craw0(url, i, save_path)
        if i % 50 == 0:
            print(i)


def run():
    url = "https://list.jd.com/list.html?cat=670,671,672&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main"
    save_path = "E:\\Project\\Spider\\JDcomputes\\"

    for i in range(1, 962):
        url = "https://list.jd.com/list.html?cat=670,671,672&page=" + str(i)
        url = url + "&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main"
        craw(url, i, save_path)
        if i % 50 == 0:
            print(i)


if __name__ == '__main__':
    run()
