# 正则表达式测试
import re


def run():
    pattern = '\n'
    string = """hello
     world"""
    result = re.search(pattern, string)
    print(result)


if __name__ == '__main__':
    run()
