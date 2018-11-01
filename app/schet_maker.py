import requests
import xml.etree.ElementTree as ET
from app.data import *


def body_schet_inserter(contragent, dogovor, nomenclatura, summa):
    global body

    body = body = body.split('<d:Контрагент_Key>')[0] + \
                  '<d:Контрагент_Key>' + contragent + '</d:Контрагент_Key>' + \
                  body.split('<d:Контрагент_Key>')[1].split('</d:Контрагент_Key>')[1]

    body = body = body.split('<d:ДоговорКонтрагента_Key>')[0] + \
                  '<d:ДоговорКонтрагента_Key>' + dogovor + '</d:ДоговорКонтрагента_Key>' + \
                  body.split('<d:ДоговорКонтрагента_Key>')[1].split('</d:ДоговорКонтрагента_Key>')[1]

    body = body.split('<d:Номенклатура_Key>')[0] + \
                 '<d:Номенклатура_Key>' + nomenclatura + '</d:Номенклатура_Key>' + \
                 body.split('<d:Номенклатура_Key>')[1].split('</d:Номенклатура_Key>')[1]


    body = body.split('<d:Цена>')[0] + \
           '<d:Цена>' + summa + '</d:Цена>' + \
           body.split('<d:Цена>')[1].split('</d:Цена>')[1]
    body = body.split('<d:Сумма>')[0] + \
           '<d:Сумма>' + summa + '</d:Сумма>' + \
           body.split('<d:Сумма>')[1].split('</d:Сумма>')[1]


    # АдресДоставки
    ### Clear Комментарий
    return body.encode('utf-8')


def schet_maker(data):
    dogovor = None
    nomenclatura = None
    summa = None
    body = body_schet_inserter(contragent, dogovor, nomenclatura)

