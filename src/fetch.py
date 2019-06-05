#-*- coding: utf-8 -*-
from src.utils.request_handler import request
from src.utils.help_utils import green,blue,yellow,red
from src.utils.help_utils import skema,no_skema
from http.cookies import SimpleCookie

class _fetch(object):

      def __init__(self,target,proxy=None,cookie=None,timeout=10):
          self.target = target
          self.proxy = proxy
          self.cookie = cookie
          self.timeout = timeout
          self.res = request(proxy=self.proxy,cookie=self._set_cookie(),timeout=self.timeout)

      def _set_cookie(self):
          try:
              if self.cookie != None:
                 cc = SimpleCookie()
                 kue = cc.load()
                 coki_coki = {a:b.value for a,b in kue.items()}
                 return coki_coki
              else:
                 return None 
          except Exception:
              print(f'[{yellow("!")}] Cookie Format {red("Invalid")}')
              return None
              
      def _request_all(self):
#          try:
              _request = self.res.send(
                mtd='GET',
                url=self.target,
                verify=False,
                allow_redirects=True
              )
              return _request
#          except Exception as eek:
#              print(f'[{red("x")}] {eek}') 
              
      def _robot(self):        
          try:
              _request = self.res.send(
                mtd='GET',
                url=self.target + '/robots.txt',
                verify=False,
                allow_redirects=False
              )
              return _request
          except Exception as eek:
              print(f'[{red("x")}] {eek}')
              
      def _sitemap(self):  
          try:
              _request = self.res.send(
                mtd='GET',
                url=self.target + '/sitemap.xml',
                verify=False,
                allow_redirects=False
              )
              return _request
          except Exception as eek:
              print(f'[{red("x")}] {eek}')
      








              
