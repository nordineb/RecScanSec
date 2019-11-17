#-*- coding: utf-8 -*-
import logging
import os
import distutils.spawn
from colorlog import ColoredFormatter
from tldextract import extract as tld

# setup logger

def logger(name,outfile):
    format_ = ColoredFormatter(
            '[%(log_color)s%(levelname)s%(reset)s] %(message)s',
            log_colors={
                '#':'blue',
                '!':'yellow',
                '-':'red',
                'x':'red',
                '+':'green'
            }
        )
    logging.addLevelName(10,'#')
    logging.addLevelName(20,'!')
    logging.addLevelName(30,'-')
    logging.addLevelName(40,'x')
    logging.addLevelName(50,'+')
    file = logging.FileHandler(outfile)
    file.setFormatter(format_)
    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    handler.setFormatter(format_)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.addHandler(file)
    return logger


def makedir(namedir):
    try:
        os.makedirs(namedir)
    except FileExistsError:
        pass

def find_nmap():
    return distutils.spawn.find_executable("nmap")

# custom print with color
def green(string):
    return f'\033[92m{string}\033[0m'
    
def red(string):
    return f'\033[91m{string}\033[0m'

def yellow(string):
    return f'\033[93m{string}\033[0m'    

def blue(string):
    return f'\033[94m{string}\033[0m'

def no_skema(url):
    subdomain = tld(url).subdomain
    domain = tld(url).domain
    suffix = tld(url).suffix
    if subdomain == '':
       return f'{domain}.{suffix}'
    else:
       return f'{subdomain}.{domain}.{suffix}'

def skema(url):
    if url.startswith('http://') or url.startswith('https://'):return url
    else:
         if tld(url).subdomain == 'www': return f'https://www.{url}'
         else: return f'http://{url}'
         
def custom_write(out,s):
    with open(out,'w') as www:
         www.write(s)

h = '\033[92m'
m = '\033[91m'
b = '\033[94m'
p = '\033[0m'
a = '\033[1;30m'

ban = f'''                                             {a} __  (\\_{p}
__             __                {h} __{p}        {a} (_ \\ ( '>{p}
|__)  _  _  __ (_   _  _   _   __{h} (_   _  _{p} {a}   ) \\/_)={p}
| \\  (- (_     __) (_ (_| | )   {h}  __) (- (_{p}{a}    (_(_ )_{p}
     Reconaissance - Scanner - Security {b}1.0{p}

({a}by{p}): {h}407 Authentic Exploit{p}
({a}codename{p}): JaxBCD
'''         









        
