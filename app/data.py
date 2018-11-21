# coding=utf-8
headers = {'Accept': 'application/atom+xml,application/xml',
           'Accept-Charset': 'UTF-8',
           'Content-Type': 'application/atom+xml',
           'DataServiceVersion': '3.0;NetFx',
           'MaxDataServiceVersion': '3.0;NetFx',
           'User-Agent': '1C-Enterprise'}

addresses_1c = {
    'main_address': 'https://login:pass@terminal.scloud.ru/base/odata/standard.odata/',
    'contragenti': 'Catalog_Контрагенты',
    'schet_factura': 'Document_СчетФактураПолученный',
    'act_creation': 'Document_ПоступлениеТоваровУслуг',
    'schet_pokupatelu': 'Document_СчетНаОплатуПокупателю',
    'contra_dogovors': 'Catalog_ДоговорыКонтрагентов',
    'nomenclaturs': 'Catalog_Номенклатура'
}
address = 'https://login:pass@terminal.scloud.ru/base/odata/standard.odata/Document_СчетНаОплатуПокупателю'

body = """<entry><category term="StandardODATA.Document_СчетНаОплатуПокупателю" scheme="http://schemas.microsoft.com/ado/2007/08/dataservices/scheme"/><title type="text"/><author/><summary/><content type="application/xml"><m:properties xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata"><d:DataVersion>AAAM7AAAAAA=</d:DataVersion><d:DeletionMark>false</d:DeletionMark><d:Date>2018-1--24T12:59:23</d:Date><d:Posted>true</d:Posted><d:Организация_Key>cbb38ee1-01c0-11e8-80c4-0cc47ab29cf7</d:Организация_Key><d:Склад_Key>0d861b95-a705-11e5-ba67-3085a93ddca2</d:Склад_Key><d:ПодразделениеОрганизации_Key>00000000-0000-0000-0000-000000000000</d:ПодразделениеОрганизации_Key><d:Контрагент_Key>e5e0707f-01cc-11e8-8d25-00155d461204</d:Контрагент_Key><d:ДоговорКонтрагента_Key>24a2fa71-1b1b-11e8-b9db-00155d462400</d:ДоговорКонтрагента_Key><d:ОрганизацияПолучатель_Key>cbb38ee1-01c0-11e8-80c4-0cc47ab29cf7</d:ОрганизацияПолучатель_Key><d:СтруктурнаяЕдиница_Key>aca7885c-01cc-11e8-8d25-00155d461204</d:СтруктурнаяЕдиница_Key><d:Комментарий>АВТО-договор</d:Комментарий><d:ВалютаДокумента_Key>e29ec0ec-a704-11e5-ba67-3085a93ddca2</d:ВалютаДокумента_Key><d:КратностьВзаиморасчетов>1</d:КратностьВзаиморасчетов><d:СуммаСкидки>0</d:СуммаСкидки><d:КурсВзаиморасчетов>1</d:КурсВзаиморасчетов><d:СуммаВключаетНДС>true</d:СуммаВключаетНДС><d:СуммаДокумента>2500</d:СуммаДокумента><d:ТипЦен_Key>00000000-0000-0000-0000-000000000000</d:ТипЦен_Key><d:УдалитьУчитыватьНДС>false</d:УдалитьУчитыватьНДС><d:УдалитьСтатусОплаты/><d:ГлавныйБухгалтер_Key>00000000-0000-0000-0000-000000000000</d:ГлавныйБухгалтер_Key><d:УдалитьЗаРуководителяПоПриказу/><d:УдалитьЗаГлавногоБухгалтераПоПриказу/><d:ДокументБезНДС>true</d:ДокументБезНДС><d:ДополнительныеУсловия_Key>fb132429-a704-11e5-ba67-3085a93ddca2</d:ДополнительныеУсловия_Key><d:ЗаГлавногоБухгалтераНаОсновании_Key>00000000-0000-0000-0000-000000000000</d:ЗаГлавногоБухгалтераНаОсновании_Key><d:ЗаРуководителяНаОсновании_Key>00000000-0000-0000-0000-000000000000</d:ЗаРуководителяНаОсновании_Key><d:Товары m:type="Collection(StandardODATA.Document_СчетНаОплатуПокупателю_Товары_RowType)"><d:element m:type="StandardODATA.Document_СчетНаОплатуПокупателю_Товары_RowType"><d:LineNumber>1</d:LineNumber><d:Номенклатура_Key>cd5b7e2f-0453-11e8-a837-00155d461301</d:Номенклатура_Key><d:Содержание>Размещение рекламных материалов на проекте Яндекс.Директ</d:Содержание><d:Количество>1</d:Количество><d:Цена>2500</d:Цена><d:Сумма>2500</d:Сумма><d:ПроцентСкидки>0</d:ПроцентСкидки><d:СуммаСкидки>0</d:СуммаСкидки><d:СтавкаНДС>БезНДС</d:СтавкаНДС><d:СуммаНДС>0</d:СуммаНДС></d:element></d:Товары><d:ВозвратнаяТара m:type="Collection(StandardODATA.Document_СчетНаОплатуПокупателю_ВозвратнаяТара_RowType)"/><d:УдалитьУслуги m:type="Collection(StandardODATA.Document_СчетНаОплатуПокупателю_УдалитьУслуги_RowType)"/></m:properties></content></entry>"""
