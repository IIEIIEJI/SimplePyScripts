#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


def img_to_base64_html(file_name__or__bytes__or__file_object):
    arg = file_name__or__bytes__or__file_object

    if type(arg) == str:
        with open(arg, mode='rb') as f:
            img_bytes = f.read()

    elif type(arg) == bytes:
        img_bytes = arg

    else:
        img_bytes = arg.read()

    import io
    bytes_io = io.BytesIO(img_bytes)

    from PIL import Image
    img = Image.open(bytes_io)

    import base64
    img_base64 = base64.b64encode(img_bytes).decode('utf-8')
    # print(img_base64)

    return 'data:image/{};base64,'.format(img.format.lower()) + img_base64


if __name__ == '__main__':
    file_name = 'img.jpg'
    img_base64 = img_to_base64_html(file_name)
    print('[len {}]: {}...'.format(len(img_base64), img_base64[:50]))

    with open(file_name + '_base64.txt', mode='w', encoding='utf-8') as f:
        f.write(img_base64)
