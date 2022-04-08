import requests
import xmltodict
import json
import datetime




def currency_rates(CharCode):
  
  """currency_rates(CharCode) --> date and time, currency rate"""
  
  b = None
  req = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
  date = datetime.datetime.now()
  date_str_type = date.strftime("%d/%m/%Y %H:%M:%S")

  
  dict = xmltodict.parse(req.content)
  cour = json.loads(json.dumps(dict))

  
  for a in cour['ValCurs']['Valute']:
    if a['CharCode'] == CharCode:
      b = a['Value']
      
      
  return date_str_type, b