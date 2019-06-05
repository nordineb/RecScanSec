#-*- coding: utf-8 -*-
import re

class waf_detect(object):

      @classmethod
      def cloudfront(cls,r):
          serv = 'CloudFront'
          if any(p in r.headers.keys() for p in ('Via','X-cache')) and any(serv.lower() in isi for isi in r.headers.values()):
             return True
          if r.headers.get('Server') == serv:
             return True
          return

      @classmethod
      def incapsula(cls,r):
          if 'X-Iinfo' in r.headers.keys() or r.headers.get('X-CDN') == 'Incapsula':
              return True
          return

      @classmethod
      def distil(cls,r):
          if r.headers.get('x-distil-cs'):
             return True
          return

      @classmethod
      def cloudflare(cls,r):
          if 'CF-RAY' in r.headers.keys() or r.headers.get('Server') == 'cloudflare' or r.headers.get('server') == 'cloudflare-nginx':
              return True
          return

      @classmethod
      def edgecast(cls,r):
          if 'Server' in r.headers.keys() and 'ECD' in r.headers['Server']:
             return True

      @classmethod
      def maxcdn(cls,r):
          if 'Server' in r.headers.keys() and 'NetDNA-cache' in r.headers['Server']:
              return True
          return

      @classmethod
      def sucuri(cls,r):
          if any((r.headers.get('Server') == 'Sucuri/Cloudproxy','X-Sucuri-ID' in r.headers.keys(),'X-Sucuri-Cache' in r.headers.keys(),'Access Denied - Sucuri Website Firewall' in r.text)):
             return True
          return

      @classmethod
      def reblaze(cls,r):
          if r.headers.get('Server') == 'Reblaze Secure Web Gateway' or r.cookies.get('rbzid'):
             return True
          return

      @classmethod
      def bigip(cls,r):
          if 'x-cnection' in r.headers.keys() or 'x-wa-info' in r.headers.keys():
             return True
          return
          
      @classmethod
      def anquanbao(cls,r):
          if 'x-powered-by-anquanbao' in r.headers.values():
             return True
          return
          
      @classmethod
      def baidu(cls,r):
          if 'yunjiasu-nginx' in r.headers.values() or 'fh1' in r.headers.values():
             return True
          return
          
      @classmethod
      def aescure(cls,r):
          if r.headers.get('aeSecure-code') is not None or 'aesecure_denied.png' in r.text:
             return True
          return
          
      @classmethod
      def dynamic(cls,r):
          if r.headers.get('X-403-Status-By') in ['dw-inj-check','dw_inj_check']:
             return True
          return
          
      @classmethod
      def binarysec(cls,r):
          if r.headers.get('server') == 'BinarySec' or r.headers.get('x-binarysec-via') is not None or r.headers.get('x-binarysec-nochace') is not None:
             return True
          return 
          
      @classmethod
      def block_dos(cls,r):
          if r.headers.get('server') == 'BlockDos.net':
             return True
          return
          
      @classmethod
      def cachewall(cls,r):
          if r.headers.get('Server') == 'Varnish' or r.headers.get('X-Varnish') is not None or r.headers.get('X-Chacewall-Action') is not None or r.headers.get('X-Chacewall-Reason') is not None:
             return True
          return
          
      @classmethod
      def china_cache(cls,r):
          if r.headers.get('Powered-By-ChinaCache') is not None:
             return True
          return
          
      @classmethod
      def ace_xml(cls,r):
          if r.headers.get('server') == 'ACE XML Gateway':
             return True
          return

      @classmethod
      def cloudbrick(cls,r):
          if r.headers.get('Server') == 'Approach Web Application Firewall':
             return True
          return

      @classmethod
      def defender(cls,r):
          if r.headers.get('X-dotDefender-denied') != None:
             return True
          return
          
      @classmethod
      def greywizard(cls,r):
          if r.headers.get('Server') == 'greywizard':
             return True
          return
          
      @classmethod    
      def datapower(cls,r):
          if r.headers.get('X-Backside-Transport') in ['OK','FAIL']:
             return True
          return

      @classmethod
      def jiasule(cls,r):
          if r.headers.get('Server') == 'Jiasule-WAF':
             return True
          return

      @classmethod
      def Akamai(cls,r):
          if r.headers.get('Server') == 'AkamaiGhost':
             return True
          return

      @classmethod
      def mission_control(cls,r):
          if r.headers.get('server') == 'Mission Control Application Shield':
             return True
          return

      @classmethod
      def mod_security(cls,r):
          if r.headers.get('Server') in ['mod_security','Mod_Security','NOYB']:
             return True
          return

      @classmethod
      def newdefend(cls,r):
          if r.headers.get('Server') == 'Newdefend':
             return True
          return

      @classmethod
      def nsfocus(cls,r):
          if r.headers.get('server') == 'NSFocus':
             return True
          return

      @classmethod
      def oneMessage(cls,r):
          if r.headers.get('X-Engine') == 'onMessage Shield':
             return True
          return
          
      @classmethod
      def profense(cls,r):
          if r.headers.get('Server') == 'profense':
             return True
          return

      @classmethod
      def radware(cls,r):
          if r.headers.get('X-SL-CompState') is not None:
             return True
             
      @classmethod
      def Asp(cls,r):
          if r.headers.get('X-ASPNET-Version') is not None:
             return True
          return
          
      @classmethod
      def safe3(cls,r):
          if r.headers.get('Server') == 'Safe3 Web Firewall':
             return True
          return
          
      @classmethod
      def safedog(cls,r):
          if r.headers.get('server') == 'Safedog':
             return True
          return

      @classmethod
      def secureentry(cls,r):
          if r.headers.get('Server') == 'Secure Entry Server':
             return True
          return

      @classmethod
      def sonicwall(cls,r):
          if r.headers.get('Server') == 'SonicWALL':
             return True
          return
          
      @classmethod
      def transIp(cls,r):
          if r.headers.get('X-TransIP-Backend') is not None:
             return True
          return

      @classmethod
      def urlmaster(cls,r):
          if r.headers.get('X-UrlMaster-Ex') is not None or r.headers.get('X-UrlMaster-Debug') is not None:
             return True
          return

      @classmethod
      def wallarm(cls,r):
          if r.headers.get('Server') == 'nginx-wallarm':
             return True
          return
          
      @classmethod
      def watchguard(cls,r):
          if r.headers.get('Server') == 'WatchGuard':
             return True
          return
          
      @classmethod
      def webseal(cls,r):
          if r.headers.get('Server') == 'WebSEAL':
             return True
          return

      @classmethod
      def wangzanbao(cls,r):
          if r.headers.get('X-Powered-By-360WZB') is not None:
             return True
          return

      @classmethod
      def xlabs(cls,r):
          if r.headers.get('X-cdn') == 'XLabs Security':
             return True
          return
          
      @classmethod
      def yundun(cls,r):
          if r.headers.get('Server') == 'YUNDUN' or r.headers.get('X-Chace') == 'YUNDUN':
             return True
          return
          
      @classmethod
      def zenedge(cls,r):
          if r.headers.get('Server') == 'ZENEDGE':
             return True
          return
          
      @classmethod
      def zscaler(cls,r):
          if r.headers.get('Server') == 'ZScaler':
             return True
          return          