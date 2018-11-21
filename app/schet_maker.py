# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import requests
import time
import numpy as np
from app.data import *


def body_schet_inserter(contragent, dogovor, nomenclatura, summa, date, nds, nomen_comment):
    global body
    date_ = date.split('-')[2] + '-' + date.split('-')[1] + '-' + date.split('-')[0]

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

    body = body.split('<d:Date>')[0] + \
           '<d:Date>' + date_ + 'T00:00:00</d:Date>' + \
           body.split('<d:Date>')[1].split('</d:Date>')[1]
    if 'Нет' in nds:
        body = body.split('<d:СуммаВключаетНДС>')[0] + \
               '<d:СуммаВключаетНДС>' + 'false' + '</d:СуммаВключаетНДС>' + \
               body.split('<d:СуммаВключаетНДС>')[1].split('</d:СуммаВключаетНДС>')[1]
    else:
        pass
    body = body.split('<d:Содержание>')[0] + \
           '<d:Содержание>' + nomen_comment + '</d:Содержание>' + \
           body.split('<d:Содержание>')[1].split('</d:Содержание>')[1]
    return body


def timeout():
    for i in range(3):
        time.sleep(np.random.choice(list(range(1, 3))))

def contragenti_extractor_1C(address):
    try:
        response = requests.get(address)
        content = response.content
        tree = ET.ElementTree(ET.fromstring(content))
    except:
        timeout()
        response = requests.get(address)
        content = response.content
        tree = ET.ElementTree(ET.fromstring(content))
    companies = {}
    x = ''
    for n, elem in enumerate(tree.iter()):
        if 'Ref_Key' in str(elem.tag) or 'Description' in str(elem.tag):
            if len(elem.text.split('-')) >= 5:
                try:
                    companies[elem.text]
                    x = elem.text
                except:
                    companies.update({elem.text: ''})
                    x = elem.text
            else:
                companies.update({x: elem.text})
    return companies

def get_contragents_dogovors():
    address = addresses_1c['main_address'] + addresses_1c['contra_dogovors']
    try:
        response = requests.get(address)
        content = response.content
        tree = ET.ElementTree(ET.fromstring(content))
    except:
        timeout()
        response = requests.get(address)
        content = response.content
        tree = ET.ElementTree(ET.fromstring(content))
    companies_docs = {}
    for n, elem in enumerate(tree.iter()):
        if 'Ref_Key' in str(elem.tag):
            try:
                companies_docs[elem.text]
                x = elem.text
            except:
                companies_docs.update({elem.text: []})
                x = elem.text
        elif 'Owner_Key' in str(elem.tag):
            companies_docs[x].append(elem.text)
        elif 'Description' in str(elem.tag):
            companies_docs[x].append(elem.text)
    return companies_docs


def get_specific_contragent(contragent):
    companies = contragenti_extractor_1C(addresses_1c['main_address'] + addresses_1c['contragenti'])
    for k, v in companies.items():
        if contragent in str(v):
            contragent_id = k
    return contragent_id

def get_contragent_dogs(contragent_id, we_know_dog_exactly=False):
    dogs = []
    contragents_dogovors = get_contragents_dogovors()
    if we_know_dog_exactly:
        for k, v in contragents_dogovors.items():
            if we_know_dog_exactly in v[1] and v[0] == contragent_id:
                return k
    else:
        for k, v in contragents_dogovors.items():
            if v[0] == contragent_id:
                dogs.append(v[1])
        return dogs

def nomenclatur_extractor_1C():
    address = addresses_1c['main_address'] + addresses_1c['nomenclaturs']
    try:
        response = requests.get(address)
        content = response.content
        tree = ET.ElementTree(ET.fromstring(content))
    except:
        timeout()
        response = requests.get(address)
        content = response.content
        tree = ET.ElementTree(ET.fromstring(content))
    nomenclaturs = {}
    x = ''
    for n, elem in enumerate(tree.iter()):
        if 'Ref_Key' in str(elem.tag) or 'Description' in str(elem.tag):
            if len(elem.text.split('-')) >= 5:
                try:
                    nomenclaturs[elem.text]
                    x = elem.text
                except:
                    nomenclaturs.update({elem.text: ''})
                    x = elem.text
            else:
                nomenclaturs.update({x: elem.text})
    return nomenclaturs

def get_specific_nomenclatura(nomenclatura_name):
    nomenclaturs = nomenclatur_extractor_1C()
    for k, v in nomenclaturs.items():
        if nomenclatura_name == str(v):
            nomenclatura_id = k
    return nomenclatura_id


def response_sender_checker(body, address):
    response = requests.post(address, data=body.encode(), headers=headers)
    response = response.content.decode()
    import json
    with open('_.json', 'w') as f:
        json.dump({'1': response}, f)
    key = response.split('<d:Ref_Key>')[1].split('</d:Ref_Key>')[0]
    if len(key.split('-')) == 5:
        return response



def schet_maker(data):
    flag = data['flag']
    if flag == 'get':
        contragent_name = data['contragent']
        contragent_id = get_specific_contragent(contragent_name)

        date = data['date']
        dogovor = data['dogovor']
        dog_id = get_contragent_dogs(contragent_id, we_know_dog_exactly=dogovor)

        nds = data['nds']
        nomen = data['nomen']
        nomenclatura_id = get_specific_nomenclatura(nomen)

        nomen_comment = data['nomen_comment']
        summa = data['summa']
        body = body_schet_inserter(contragent_id, dog_id, nomenclatura_id, summa, date, nds, nomen_comment)
        import json
        with open('_2.json', 'w') as ff:
            json.dump({'1':body}, ff)
        response = response_sender_checker(body, address)
        if response:
            return response.split('<d:Number>')[1].split('</d:Number>')[0]
    return False
