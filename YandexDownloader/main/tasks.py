# -*- coding: utf-8 -*-

from celery import task
import lxml.html as html
import requests

import models

proxies = {
  'http': 'http://82.139.113.237:80',
  'https': 'http://103.43.47.66:3128',
}

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)'
                         ' AppleWebKit/537.36'
                         ' (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def get_links_from_page(keyword, page_number):
    '''
    Update db with YandexEntity
    Note! For avoid blocking IP from Yandex we can use list
    of proxies.
    :param keyword: Keyword for query
    :param page_number: number of page of response
    :return: no return. This method only update db
    '''
    response = requests.get(
        "http://yandex.ru/search/?text=%s&lr=194&p=%s" % (keyword,
                                                          page_number),
        headers=headers
        #proxies=proxies
    )
    content = response.content
    page = html.document_fromstring(content.decode('utf-8'))
    items = page.find_class('serp-item')
    for item in items:
        url = item.find_class(
            'link organic__url link link_cropped_no')[0].attrib['href']
        title = item.text_content()
        y = models.YandexEntity(page_number=page_number, url=url, title=title)
        y.save()


@task
def get_links(keyword):
    for i in range(3):
        get_links_from_page(keyword, i)
