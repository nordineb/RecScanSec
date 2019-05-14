#-*- coding: utf-8 -*-
from .utils.request_handler import request_handler as request
from .utils.ngelog import logger,skema,no_skema
from bs4 import BeautifulSoup as bs
import re

class subdomain_enumeration(object):

      def __init__(self,domain):
          self.domain = domain
          self.req = request().sessi()
          self.text = self.request().text

      @property
      def soup(self):
          sop = bs(self.text,'html.parser').findAll('table')
          return sop

      def dns(self):
          teks = self.soup[0].text
          hasil = re.sub(r'([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3})','- ',teks)
          return hasil

      def mx(self):
          teks = self.soup[1].text
          hasil = re.sub(r'([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3})','- ',teks)
          return hasil
          
      def txt(self):
          teks = self.soup[2].text
          return teks
          
      def subInfo(self):
          teks = self.soup[3].text
          hasil = re.sub(r'([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3})','- ',teks)
          return hasil

      def subdomain(self):
          sub = re.findall(r'http://(.*?)"',self.text)
          return sub

      def request(self):
          get_token = self.req.get('https://dnsdumpster.com')
          better_cookie = get_token.cookies.get_dict()
          r = self.req.post(
            'https://dnsdumpster.com',
            cookies=better_cookie,
            headers={'Referer':'https://dnsdumpster.com'},
            data={
                'csrfmiddlewaretoken':better_cookie['csrftoken'],
                'targetip':no_skema(self.domain)
            }
          )
          return r

           

