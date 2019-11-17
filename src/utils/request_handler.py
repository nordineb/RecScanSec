#-*- coding: utf-8 -*-
from requests import request as _request
from requests import Session
from urllib3.exceptions import NewConnectionError
from requests.exceptions import  ProxyError, TooManyRedirects, ConnectionError, ConnectTimeout, ReadTimeout
from src.utils.exceptions import RequestException
from src.utils.user_agent import useragent

class request(object):

      def __init__(self,proxy=None,cookie=None,timeout=10):
          self.proxy = {
            'http':proxy,
            'https':proxy
          }
          self.cookie = cookie
          self.timeout = timeout
          
      def send(self,mtd='GET',*args,**kwargs):
          try:
               return _request(
                method=mtd,
                headers={
                    'User-Agent':useragent(),
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept': '*/*',
                    'Connection': 'keep-alive'
                },
                timeout=self.timeout,
                cookies=self.cookie,
                proxies=self.proxy,
                *args,
                **kwargs
               )
          except ProxyError:
              raise RequestException('Error Connect To Proxies')
          except (ConnectTimeout,ReadTimeout):
              raise RequestException('Connection Timeout To Server')
          except NewConnectionError:
              raise RequestException("Address Can't be Resolved")             
          except ConnectionError:
              raise RequestException('Error Connecting To Host Check Your Internet Connection')
          except TooManyRedirects:
              raise RequestException('Too Many Redirects Error')              
          except UnicodeDecodeError:
              pass  
              
      def ses(self):
          ses = Session()
          ses.headers.update({'User-Agent': useragent(), 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'})
          ses.proxies.update(self.proxy)          
          return ses








        