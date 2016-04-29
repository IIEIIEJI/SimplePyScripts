#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


import sys
import logging
logging.basicConfig(
    level=logging.DEBUG,
    stream=sys.stdout,
    format='[%(asctime)s] %(filename)s[LINE:%(lineno)d] %(levelname)-8s %(message)s'
)

username = '<username>'
password = '<password>'
smtp_server = '<smtp_server>'
from_email = '<from_email>'


def get_last_lunch_menu():
    """
    Функция получает последнее письмо от указанного емейла
    и сохраняет из него приложенный файл.

    """

    logging.debug('Check last email.')

    import imaplib
    connect = imaplib.IMAP4(smtp_server)
    connect.login(username, password)
    connect.select()

    logging.debug('Search emails from %s.', from_email)

    typ, msgnums = connect.search(None, 'HEADER From', from_email)
    last_id = msgnums[0].split()[-1]
    typ, data = connect.fetch(last_id, '(RFC822)')

    import email
    msg = email.message_from_bytes(data[0][1])

    connect.close()
    connect.logout()

    return msg


if __name__ == '__main__':
    msg = get_last_lunch_menu()
    print(msg)