import asyncio
import time
import aiohttp
import lxml
import xml.etree.ElementTree as et
import pandas as pd
from datetime import date, timedelta
import makefiles 
def getdata(format):
    cur = date(2023, 2, 10)
    yesterday = date.today() - timedelta(days=1)
    delta = timedelta(days=1)
    dates = []
    while cur <= yesterday:
        dates.append(cur.strftime(format))
        cur += delta
    return dates

async def source1(dates):
    res=[]
    async with aiohttp.ClientSession() as session:
        for i in dates:
          async with session.get(f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={i}') as response:
              result=await response.text()
              root=et.fromstring(result)
              for i in root.findall('Valute'):
                  if i.findtext('CharCode')=='USD':
                      res.append(float(i.findtext('Value').replace(',','.')))
    return res


async def source2(dates):
      result=[]
      async with aiohttp.ClientSession() as session:
        for i in dates:
            async with session.get(f'https://api.currencyapi.com/v3/historical?apikey=kYDvVe6IfM59XNuNHUDu5V9xa3FIPGCTlNq4Eary&currencies=RUB&date={i}') as response:
              a= await response.json()
              result.append(a['data']['RUB']['value'])
             
      return result

async def main():
    dates1=getdata('%d/%m/%Y')
    dates2=getdata('%Y-%m-%d')
    t1=asyncio.create_task(source1(dates1))
    t2=asyncio.create_task(source2(dates2))
    res1=await t1
    res2=await t2
    ndf=makefiles.make_data_frame(res1,res2,dates1)
    ndf.to_csv('result_of_script.csv',index=False)
    data=pd.read_csv('result_of_script.csv')
    print(data)
asyncio.get_event_loop().run_until_complete(main())
