# coding : utf-8

import requests
from bs4 import BeautifulSoup


def get_content(url):
    headers = {"user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
    r = requests.get(url, headers=headers)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def get_shopname(html):

    shopname = html.find_all('a', class_='productShop-name')
    return shopname


def get_price(html):

    price = html.find_all('p', class_='productPrice')
    return price


def get_status(html):

    status = html.find_all('p', class_='productStatus')
    return status


def get_title(html):

    title = html.find_all('p', class_='productTitle')
    return title


def get_detail(content):
    con = []
    for i in content:
        con.append(i.get_text())
    return con


def print_all(title, shopname, price, status):
    length = len(title)
    for i in range(1, length):
        print('第%d个店铺信息:' % i)
        print(title[i], shopname[i], price[i], status[i])
        print('---------------------------')


def main():

    item = input('请输入想要搜索的宝贝：')
    url = 'https://list.tmall.com/search_product.htm?q={}'.format(item)
    soup = get_content(url)

    Shopname = get_detail(get_shopname(soup))

    Price = get_detail(get_price(soup))

    Status = get_detail(get_status(soup))

    Title = get_detail(get_title(soup))

    print_all(Title, Shopname, Price, Status)


if __name__ == '__main__':
    main()






