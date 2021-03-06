#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


"""
Download tags with description and save in file as JSON.

"""


import requests
from bs4 import BeautifulSoup
import time

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0"
}

tags = dict()

for page in range(1, 106):
    print(page)

    try:
        rs = requests.get('http://ru.stackoverflow.com/tags?page={}&tab=popular'.format(page), headers=headers)

        root = BeautifulSoup(rs.content, 'lxml')
        for tag in [a.text.strip() for a in root.select('.tag-cell > a')]:
            url_info = 'http://ru.stackoverflow.com/tags/{}/info'.format(tag)

            rs = requests.get(url_info, headers=headers)
            root = BeautifulSoup(rs.content, 'lxml')

            # TODO: Ignore tags without description
            if root.select_one('.post-text'):
                tags[tag] = {
                    'url_info': url_info,

                    # TODO: scrap only need text
                    'description': root.select_one('.post-text').text.strip(),
                }

            time.sleep(2)

    except Exception as e:
        import traceback
        print("ERROR: {}\n\n{}".format(e, traceback.format_exc()))

        break

import json
json.dump(tags, open('tags.json', 'w', encoding='utf-8'), ensure_ascii=False)
