#-*-coding:utf-8-*-
import requests
import json
from collections import OrderedDict
from bs4 import BeautifulSoup

class corona(object):

    def __init__(self):
        super(corona, self).__init__()

    
    def _get_movement(self):
        
        _res = requests.get('http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=12&ncvContSeq=&contSeq=&board_id=&gubun=')
        _corona_html = _res.text
        _soup = BeautifulSoup(_corona_html, 'html.parser')
        _resource = _soup.select('tbody > tr')
        _resource_title = _soup.select('strong.tit')
        _json_info = OrderedDict()
        _corona_title = []
        index = 0
        
        for i in _resource_title:
            _corona_title.append(i.text)

        for i in _resource:
            _json_info[index] = {'address':i.select('td')[-3].text, 'date': i.select('td')[-2].text}
            index = index + 1

      
        with open('corona_movement.json', 'w', encoding='utf-8') as file:
            json.dump(_json_info, file, ensure_ascii = False, indent = '\t')

        print('가져온 정보:',_corona_title)
        
            
        
       

        
        



