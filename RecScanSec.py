#-*- coding: utf-8 -*-
import sys
if sys.version[0] == '2':
   print('\n[x] Not Supported For Python 2 please use python 3\n')
   exit()
   
try:
     import requests
     import tldextract
     import bs4
     import colorlog
     import click
     import asyncio
except Exception:
     print('\n ! pip3 install -r requirements.txt "for install requirements"\n')
     exit()

from src.lib.fingerprint import (
    finger,
    ssl_info,
    ptr_record
)
from src.lib.disclosure import disclosure
from src.lib.host_mapper import host_mapper
from src.lib.crawler import (
    Crawling,
    html_form
)
from src.lib.fuzzer import Fuzz
from src.utils.help_utils import (
    skema,
    no_skema,
    green,
    red,
    blue,
    yellow,
    ban,
    makedir,
    find_nmap,    
)
from src.fetch import _fetch
from datetime import datetime as d
from time import sleep
import urllib3
import os
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

@click.command()
@click.version_option('1.0')
@click.argument('target')
@click.option('--timeout',help='Seconds to wait before timeout connections ',default=None,show_default=True,type=int)
@click.option('--proxy',default=None,help='if Use a proxy ex: 0.0.0.0:8888'
                             'if with auth 0.0.0.0:8888@user:password')
@click.option('--cookies',default=None,help='if use cookie comma separated cookies to add the request'
                               'ex: PHPSESS:123,kontol=True')
@click.option('--no-url-fuzzing',is_flag=True,help='do not fuzz url')                               
@click.option('--update',is_flag=True,help='Check For Update')


def main(target,timeout,proxy,cookies,no_url_fuzzing,update):
    wd_path = os.getcwd() + '/src/utils/wordlist'
    if update == True:
       print('[{}] Checking For Update'.format(yellow('!')))
       os.system('git pull')
       exit()
    _request = _fetch(target,proxy=proxy,cookie=cookies,timeout=timeout)
    makedir(os.getcwd() + '/output/' + no_skema(target))
    try:
        print(ban)
        r1 = _request._request_all()
        print('[{}] Starting @ {}'.format(green('!'),green(d.now().strftime("%H-%M-%S /%Y-%m-%d/"))))
        print('[{}] Scanning Target: {}'.format(blue('#'),red(target)))
        print('[{}] Status: {}'.format(blue('#'),'\033[1;30m' + str(r1.status_code) + '\033[0m'))        
        print('[{}] Checking Headers Security '.format(green(d.now().strftime("%H-%M-%S"))))                        
        sleep(5)        
        _finger = finger(r1,target)
        _finger.security_headers()
        print('[{}] Try To Detecting WAF '.format(green(d.now().strftime("%H-%M-%S"))))
        sleep(5)
        _finger.detect()
        print('[{}] Searching Location Info'.format(green(d.now().strftime("%H-%M-%S"))))
        sleep(5)        
        _finger.location()
        if find_nmap is not None:
           print('[{}] Scanning Port Open'.format(green(d.now().strftime("%H-%M-%S"))))
           _finger.port_scan()
        print('[{}] Domain PTR Recording'.format(green(d.now().strftime("%H-%M-%S"))))
        sleep(5)
        ptr_record(target)._run()
        print('[{}] Getting SSL Information'.format(green(d.now().strftime("%H-%M-%S"))))
        ssl_info(target).get_ssl()
        print('[{}] Disclosing Information on {}'.format(green(d.now().strftime("%H-%M-%S")),red(target)))    
        sleep(5)        
        disc = disclosure(r1.text,target)
        disc.email()
        disc.phone()
        disc.credit_card()
        disc.social_security_number()
        r2 = _request._robot()
        r3 = _request._sitemap()
        disc.robot(r2)
        disc.sitemap(r3)
        print('[{}] Mapping Host Information on: {}'.format(green(d.now().strftime("%H-%M-%S")),no_skema(target)))
        sleep(5)        
        hm = host_mapper(target)
        hm.DNS()
        sleep(3)
        hm.MX()
        sleep(3)
        hm.TXT()
        sleep(3)
        hm.subdomain()
        sleep(3)
        hm.subdomain_info()
        sleep(3)
        print('[{}] Crawling Url on: {}'.format(green(d.now().strftime("%H-%M-%S")),red(target)))
        sleep(5) 
        crawl = Crawling(r1.text,target)
        crawl.js_parse_link()
        sleep(3)
        crawl._internal_dynamic()
        sleep(3)
        crawl._external_link()
        sleep(3)
        print('[{}] Crawling From robots.txt'.format(green(d.now().strftime("%H-%M-%S"))))
        sleep(3)        
        crawl.robot_url_crawl(r2)
        print('[{}] Crawling From Sitemap.xml'.format(green(d.now().strftime("%H-%M-%S"))))
        sleep(3)        
        crawl.sitemap_url_crawl(r3)
        frm = html_form(r1.text,target)
        print('[{}] Analyzing HTML Form Input'.format(green(d.now().strftime("%H-%M-%S"))))
        sleep(3)        
        frm.analis()
        if no_url_fuzzing == False:
           print('[{}] Starting Url FUZZ'.format(green(d.now().strftime("%H-%M-%S"))))
           print('[{}] Please Wait'.format(yellow('!')))
           fuz = [Fuzz(target,wd_path + '/fuzzlist.fuzz'),Fuzz(target,wd_path + '/dir_sensitive.fuzz')]
           fuz[0].main()
           fuz[1].main()
           print('[{}] Done at {}'.format(yellow('!'),green(d.now().strftime("%H-%M-%S"))))
        print('[{}] All Scanning Done At {}'.format(green('!'),green(d.now().strftime("%H-%M-%S /%Y-%m-%d/"))))
    except Exception as e:
        print(red(e))    
    except (KeyboardInterrupt):
        exit()                          
        
if __name__ == '__main__':
   main()        
        
                
         
         
         










       
    