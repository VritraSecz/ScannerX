## Created By Alex Butler (https://github.com/MrHacker-X/)
## Don't be a copy cat create your own

import os 
import time
import sys

tumo = """
Usages: scanx <domain>
Example: scanx example.com
"""

## Getting input from argument

if(len(sys.argv) !=2):
  print(tumo)
  exit()

else:
  sitex = sys.argv[1]

#print(sitex)
#exit()

## Banner

banner = """\033[1;97m   ____                       \033[1;91m    _  __
 \033[1;97m / __/______  ___  ___  ___ ____\033[1;91m| |/_/
 \033[1;97m_\ \/ __/ _ `/ _ \/ _ \/ -_) __/\033[1;91m> < 
\033[1;97m/___/\__/\_,_/_//_/_//_/\__/_/\033[1;91m /_/|_| 
\033[1;91m<------[\033[1;41m\033[1;97mCreated By MrHacker-X\033[0m\033[1;91m]------>
"""

## main menu

menu = """\033[1;91m[##]\033[1;97m Select any option:

\033[1;91m[01] \033[1;97mShow Category
\033[1;91m[02] \033[1;97mRun All Scan
\033[1;91m[03] \033[1;97mFollow US
\033[1;91m[04] \033[1;97mAbout
\033[1;91m[05] \033[1;97mUpdate It
\033[1;91m[06] \033[1;97mUninstall It
\033[1;91m[00] \033[1;97mQuit

\033[1;97m[\033[1;91m??\033[1;97m] option\033[1;91m>> \033[1;97m"""

# List of scanning type

liscan = """\033[1;91m[##]\033[1;97m Select any option:

\033[1;91m[01] \033[1;97m Subdomain Enumaration
\033[1;91m[02] \033[1;97m Port, DNS, Whois
\033[1;91m[03] \033[1;97m Header Built With
\033[1;91m[04] \033[1;97m TLS/SSL Certificates
\033[1;91m[05] \033[1;97m Analyze
\033[1;91m[06] \033[1;97m Wayback Machine
\033[1;91m[07] \033[1;97m Search Engines
\033[1;91m[08] \033[1;97m Google Dorks
\033[1;91m[09] \033[1;97m Github Dorks P1
\033[1;91m[10] \033[1;97m Github Dorks P2
\033[1;91m[95] \033[1;97m Back
\033[1;91m[00] \033[1;97m Quit

\033[1;97m[\033[1;91m??\033[1;97m] option\033[1;91m>> \033[1;97m"""

# My social media profiles

soc = """\033[1;91m[*] \033[1;97mSelect any options

\033[1;91m[01] \033[1;97mInstagram
\033[1;91m[02] \033[1;97mFacebook
\033[1;91m[03] \033[1;97mGithub
\033[1;91m[04] \033[1;97mYouTube
\033[1;91m[05] \033[1;97mTelegram
\033[1;91m[95] \033[1;97mBack
\033[1;91m[00] \033[1;97mQuit

\033[1;97m[\033[1;91m??\033[1;97m]\033[1;91m option>> \033[1;97m"""

## About section

about = """
\033[1;91m[*]\033[1;97m Author: \033[1;91mAlex Butler (\033[1;97mMrHacker-X\033[1;91m)

\033[1;97m[*]\033[1;91m Introduction:
\033[1;91m==> \033[1;97mScannerX is a linux kernal based tool for linux and Termux(Android) user. This tool is written in python3. This tool contain 10 different type of scanning and We've used total more than 11 websites for better scanning. We've also included virustotal scanning here so you can see if link is malicious or not. If you're using this tool then You're able to scan port, subdomain, dns and many more things. 

\033[1;97m[*] \033[1;91mFeatures:

\033[1;91m>>\033[1;97m Subdomain Scanning
\033[1;91m>>\033[1;97m Port scanning
\033[1;91m>>\033[1;97m Whois scanning
\033[1;91m>>\033[1;97m DNS Scanning
\033[1;91m>>\033[1;97m Header Scanning
\033[1;91m>>\033[1;97m Analyze
\033[1;91m>>\033[1;97m TLS Scanning
\033[1;91m>>\033[1;97m SSL Scanning
\033[1;91m>>\033[1;97m Wayback Machine
\033[1;91m>>\033[1;97m Google Dorking
\033[1;91m>>\033[1;97m Github Dorking

\033[1;91m>>\033[1;97m Easy To Use
\033[1;91m>>\033[1;97m Lite Weight
\033[1;91m>>\033[1;97m User Friendly

\033[1;97m[*] \033[1;91mOur Social Media:

\033[1;91m>\033[1;97m YouTube   : \033[1;91m@\033[1;97m Sololex
\033[1;91m>\033[1;97m Facebook  : \033[1;91m@\033[1;97m hackerxmr
\033[1;91m>\033[1;97m Github    : \033[1;91m@\033[1;97m MrHacker-X
\033[1;91m>\033[1;97m Instagram : \033[1;91m@\033[1;97m 0hacker_x0
\033[1;91m>\033[1;97m Telegram  : \033[1;91m@\033[1;97m mrhackersx
"""

## Categorized function
# first wave subdomain enumaration
def dnsenum():
  os.system("xdg-open https://www.virustotal.com/gui/domain/" + sitex + "/relations 2> /dev/null")
  os.system("xdg-open https://crt.sh/?q=%25." + sitex + " 2> /dev/null")
  os.system("xdg-open https://riddler.io/search?q=pld:" + sitex + " 2> /dev/null")
  os.system("xdg-open https://riddler.io/search?q=host:" + sitex + " 2> /dev/null")
  os.system("xdg-open https://riddler.io/search?q=keyword%3A" + sitex + "&view_type=data_table 2> /dev/null")
  os.system("xdg-open https://findsubdomains.com/subdomains-of/souqana.com 2> /dev/null")
  os.system("xdg-open https://dnstable.com/domain/" + sitex + " 2> /dev/null")
  os.system("xdg-open https://securitytrails.com/list/apex_domain/" + sitex + " 2> /dev/null")
  os.system("xdg-open https://certspotter.com/api/v0/certs?domain=" + sitex + " 2> /dev/null")
  os.system("xdg-open https://www.google.ca/search?q=site:*." + sitex + " 2> /dev/null")
  os.system("xdg-open https://www.google.ca/search?q=site:*.*." + sitex + " 2> /dev/null")


 # 2nd wave Ports/DNS/WHOis
def portis():
  os.system("xdg-open https://viewdns.info/portscan/?host=" + sitex + " 2> /dev/null")
  os.system("xdg-open https://viewdns.info/dnsreport/?domain=" + sitex + " 2> /dev/null")
  os.system("xdg-open http://viewdns.info/reversewhois/?q=" + sitex + " 2> /dev/null")
  os.system("xdg-open https://viewdns.info/whois/?domain=" + sitex + " 2> /dev/null")
  os.system("xdg-open https://dnslytics.com/domain/" + sitex + " 2> /dev/null")

 # 3rd wave header built with
def header():
  os.system("xdg-open https://www.threatcrowd.org/domain.php?domain=" + sitex + " 2> /dev/null")
  os.system("xdg-open https://securityheaders.com/?q=" + sitex + "&followRedirects=on 2> /dev/null")
  os.system("xdg-open https://viewdns.info/httpheaders/?domain=" + sitex + " 2> /dev/null")
  os.system("xdg-open https://builtwith.com/" + sitex + " 2> /dev/null")

 # 4th wave tls/ssl certificates
def tlss():
  os.system("xdg-open https://www.ssllabs.com/ssltest/analyze.html?d=" + sitex + " 2> /dev/null")
  os.system("xdg-open https://certdb.com/search/index?q=domain%3A%22" + sitex + "%22 2> /dev/null")
  os.system("xdg-open https://transparencyreport.google.com/https/certificates?cert_search_auth=&cert_search_cert=p:c291cWFuYS5jb206dHJ1ZTp0cnVlOjpFQUU9&cert_search=include_expired:true;include_subdomains:true;domain:" + sitex + "&lu=cert_search_cert 2> /dev/null")

 # 5th wave Analyze
def analyze():
  os.system("xdg-open http://toolbar.netcraft.com/site_report?url=" + sitex + " 2> /dev/null")
  os.system("xdg-open https://sitecheck.sucuri.net/results/" + sitex + " 2> /dev/null")
  os.system("xdg-open https://www.siteguarding.com/spam/viewreport?domain=" + sitex + " 2> /dev/null")
  os.system("xdg-open https://app.upguard.com/webscan#/www." + sitex + " 2> /dev/null")
  os.system("xdg-open https://observatory.mozilla.org/analyze/" + sitex + " 2> /dev/null")

 # 6th wave Wayback machine
def wayback():
  os.system("xdg-open https://web.archive.org/web/*/" + sitex + " 2> /dev/null")

 #7th wave Search engines
def srchengne():
  os.system("xdg-open https://fofa.so/result?q=" + sitex + "&qbase64=ImZhY2Vib29rLmNvbSI%3D&full=true 2> /dev/null")
  os.system("xdg-open https://www.zoomeye.org/searchResult/bugs?q=" + sitex + " 2> /dev/null")
  os.system("xdg-open https://www.zoomeye.org/searchResult?q=" + sitex + "")
  os.system("xdg-open https://www.shodan.io/search?query=" + sitex + " 2> /dev/null")
  os.system("xdg-open https://www.censys.io/ipv4?q=" + sitex + " 2> /dev/null")

 # 8th wave google dorks
def godork():
  os.system("xdg-open https://www.google.ca/search?q=site:" + sitex + "+ext:cgi+OR+ext:php+OR+ext:asp+OR+ext:aspx+OR+ext:jsp+OR+ext:jspx+OR+ext:swf+OR+ext:fla+OR+ext:xml 2> /dev/null")
  os.system("xdg-open https://www.google.ca/search?q=site:" + sitex + "+ext:doc+OR+ext:docx+OR+ext:csv+OR+ext:pdf+OR+ext:txt+OR+ext:log+OR+ext:bak 2> /dev/null")
  os.system("xdg-open https://www.google.ca/search?q=site:" + sitex + "+ext:action+OR+struts 2> /dev/null")
  os.system("xdg-open https://www.google.ca/search?q=site:pastebin.com+" + sitex + " 2> /dev/null")
  os.system("xdg-open https://www.google.ca/search?q=site:linkedin.com+employees+" + sitex + " 2> /dev/null")
  os.system("xdg-open https://www.google.ca/search?q=site:" + sitex + "+username+OR+password+OR+login+OR+root+OR+admin 2> /dev/null")
  os.system("xdg-open https://www.google.ca/search?q=site:" + sitex + "+inurl:shell+OR+inurl:backdoor+OR+inurl:wso+OR+inurl:cmd+OR+shadow+OR+passwd+OR+boot.ini+OR+inurl:backdoor 2> /dev/null")
  os.system("xdg-open https://www.google.ca/search?q=site:" + sitex + "+inurl:readme+OR+inurl:license+OR+inurl:install+OR+inurl:setup+OR+inurl:config 2> /dev/null")
  os.system("xdg-open https://www.google.ca/search?q=site:" + sitex + "+inurl:wp-+OR+inurl:plugin+OR+inurl:upload+OR+inurl:download 2> /dev/null")
  os.system("xdg-open https://www.google.ca/search?q=site:" + sitex + "+inurl:redir+OR+inurl:url+OR+inurl:redirect+OR+inurl:return+OR+inurl:src=http+OR+inurl:r=http 2> /dev/null")

 # 9th wave github dorks p1
def gidork1():
  os.system("xdg-open https://github.com/search?q=" + sitex + " 2> /dev/null")
  os.system("xdg-open https://github.com/search?q=" + sitex + "+filename:.npmrc_auth 2> /dev/null")
  os.system("xdg-open https://github.com/search?q=" + sitex + "+filename:.dockercfg+auth 2> /dev/null")
  os.system("xdg-open https://github.com/search?q=" + sitex + "+extension:pem+private 2> /dev/null")
  os.system("xdg-open https://github.com/search?q=" + sitex + "+extension:ppk+private 2> /dev/null")
  os.system("xdg-open https://github.com/search?q=" + sitex + "+filename:id_rsa 2> /dev/null")
  os.system("xdg-open https://github.com/search?q=" + sitex + "+filename:id_dsa 2> /dev/null")
  os.system("xdg-open https://github.com/search?q=" + sitex + "+extension:sql+mysql+dump 2> /dev/null")

def gidork2():
 # 10th wave github.com p2
  os.system("xdg-open https://github.com/search?q=" + sitex + "+extension:sql+mysql+dump+password 2> /dev/null")
  os.system("xdg-open https://github.com/search?q=" + sitex + "+filename:.htpasswd 2> /dev/null")
  os.system("xdg-open https://github.com/search?q=" + sitex + "+HEROKU_API_KEY+language:shell 2> /dev/null")
  os.system("xdg-open https://github.com/search?q=" + sitex + "+HEROKU_API_KEY+language:json 2> /dev/null")
  os.system("xdg-open https://github.com/search?q=" + sitex + "+filename:.bash_history 2> /dev/null")
  os.system("xdg-open https://github.com/search?q=" + sitex + "+filename:.history 2> /dev/null")

# script Begin

while True:
  os.system('clear')
  print(banner)
  opt = input(menu)

  if opt == '01' or opt == '1':
    while True:
      os.system('clear')
      print(banner)
      lisx = input(liscan)

      if lisx == '1' or lisx == '01':
        print("\033[1;91m[*] \033[1;97mLaunching subdomain Enumaration")
        time.sleep(1.3)
        dnsenum()

      elif lisx == '2' or lisx == '02':
        print("\033[1;91m[*] \033[1;97m Launching Port, DNS, Whois")
        time.sleep(1.2)
        portis()

      elif lisx == '3' or lisx == '03':
        print("\033[1;91m[*] \033[1;97m Launching Header Built With")
        time.sleep(1.2)
        header()

      elif lisx == '4' or lisx == '04':
        print("\033[1;91m[*] \033[1;97m Launching TLS/SSL Certificates")
        time.sleep(1.2)
        tlss()

      elif lisx == '5' or lisx == '05':
        print("\033[1;91m[*] \033[1;97m Launching Analyze")
        time.sleep(1.2)
        analyze()

      elif lisx == '6' or lisx == '06':
        print("\033[1;91m[*] \033[1;97m Launching Wayback Machine")
        time.sleep(1.2)
        wayback()

      elif lisx == '7' or lisx == '07':
        print("\033[1;91m[*] \033[1;97m Launching Search Engine")
        time.sleep(1.2)
        srchengne()

      elif lisx == '8' or lisx == '08':
        print("\033[1;91m[*] \033[1;97m Launching Google Dorks")
        time.sleep(1.2)
        godork()

      elif lisx == '9' or lisx == '09':
        print("\033[1;91m[*] \033[1;97m Launching Github Dorks P1")
        time.sleep(1.2)
        gidork1()

      elif lisx == '10':
        print("\033[1;91m[*] \033[1;97m Launching Github Dorks P2")
        time.sleep(1.2)
        gidork2()

      elif lisx == '95':
        print("\n\033[1;91m[*] \033[1;97mGetting Back\n")
        time.sleep(1.3)
        break

      elif lisx == '0' or lisx == '00':
        print("\n\033[1;91m[*] \033[1;97mQuiting...\n")
        time.sleep(1.3)
        exit()
        
      else:
        print("\n\033[1;91mInvalid Input\n")
        time.sleep(1)

  elif opt == '02' or opt == '2':
    print()
    print("\033[1;91m[*] \033[1;97mPreparing ...")
    time.sleep(1)
    print("\033[1;91m[*]\033[1;97m] Note: \033[1;91mDon't forget to close Active Tabs")
    time.sleep(1)
    # 1st wave
    print()
    input("\033[1;94mPress ENTER To Launch First Wave")
    print("\033[1;91m[*] \033[1;97mLaunching First Wave [Subdomain Enumaration]")
    time.sleep(1)
    dnsenum()

    # 2nd wave
    print()
    input("\033[1;94mPress ENTER To Launch Next Wave")
    print("\033[1;91m[*] \033[1;97mLaunching Second Wave [Port, DNS, Whois]")
    time.sleep(1)
    portis()

    # 3rd wave
    print()
    input("\033[1;94mPress ENTER To Launch Next Wave")
    print("\033[1;91m[*] \033[1;97mLaunching Third Wave [Header Built With]")
    time.sleep(1)
    header()

    # 4th wave
    print()
    input("\033[1;94mPress ENTER To Launch Next Wave")
    print("\033[1;91m[*] \033[1;97mLaunching Fourth Wave [TLS/SSL Certificates]")
    time.sleep(1)
    tlss()

    # 5th wave
    print()
    input("\033[1;94mPress ENTER To Launch Next Wave")
    print("\033[1;91m[*] \033[1;97mLaunching Fifth Wave [Analyze]")
    time.sleep(1)
    analyze()

    # 6th wave
    print()
    input("\033[1;94mPress ENTER To Launch Next Wave")
    print("\033[1;91m[*] \033[1;97mLaunching Sixth Wave [Wayback Machine]")
    time.sleep(1)
    wayback()

    # 7th wave
    print()
    input("\033[1;94mPress ENTER To Launch Next Wave")
    print("\033[1;91m[*] \033[1;97mLaunching Seventh Wave [Search Engines]")
    time.sleep(1)
    srchengne()

    # 8th wave
    print()
    input("\033[1;94mPress ENTER To Launch Next Wave")
    print("\033[1;91m[*] \033[1;97mLaunching Eighth Wave [Google Dorks]")
    time.sleep(1)
    godork()

    # 9th wave
    print()
    input("\033[1;94mPress ENTER To Launch Next Wave")
    print("\033[1;91m[*] \033[1;97mLaunching Ninth Wave [Github Dork P1]")
    time.sleep(1)
    gidork1()

    # 10th wave
    print()
    input("\033[1;94mPress ENTER To Launch Last Wave")
    print("\033[1;91m[*] \033[1;97mLaunching Tenth and Last Wave [Github Dork P2]")
    time.sleep(1)
    gidork2()
    print()
    print("\033[1;91m[*] \033[1;97mThanks for using ScannerX.")
    exit()



  elif opt == '03' or opt == '3':
    os.system("clear")
    print(banner)
    print("\033[1;91m[*] \033[1;97mThanks for using my tool 'ScannerX' For scanning websites. So you can follow me on various social media site. Link and options are given down below, So select here options where you want to follow me ")
    print()
    print()
    while True:
      fol = input(soc)
      if fol == '1' or fol == '01':
        print()
        print("\033[1;91m[*] \033[1;97mOpening my Instagram profile in your device \n")
        time.sleep(1)
        os.system("xdg-open https://instagram.com/0hacker_x0")
      
      elif fol == '2' or fol == '02':
        print()
        print("\033[1;91m[*] \033[1;97mOpening my Facebook page in your device \n")
        time.sleep(1)
        os.system("xdg-open https://facebook.com/hackerxmr")

      elif fol == '3' or fol == '03':
        print()
        print("\033[1;91m[*] \033[1;97mOpening my Github profile in your device \n")
        time.sleep(1)
        os.system("xdg-open https://github.com/MrHacker-X")

      elif fol == '4' or fol == '04':
        print()
        print("\033[1;91m[*] \033[1;97mOpening my YouTube channel in your device \n")
        time.sleep(1)
        os.system("xdg-open https://youtube.com/c/Sololex")
      
      elif fol == '5' or fol == '05':
        print()
        print("\033[1;91m[*] \033[1;97mOpening my Telegram Channel in your device \n")
        time.sleep(1)
        os.system("xdg-open https://t.me/hackwithalex")

      elif fol == '95':
        print()
        print("\033[1;91m[*]\033[1;97m Getting back ...\n")
        time.sleep(1)
        break

      elif fol == '0' or fol == '00':
        print()
        print("\033[1;91m[*]\033[1;97m Thanks for using ScannerX")
        print("\033[1;91m[*]\033[1;97m Quiting ...\n")
        time.sleep(1)
        exit()

      else:
        print()
        print("\033[1;91mInvalid Input")
        print()
        time.sleep(1)

  elif opt == '04' or opt == '4':
    os.system("clear")
    print(banner)
    print(about)
    input("\033[1;94mPress ENTER To Continue")

  elif opt == '05' or opt == '5':
    os.system('clear')
    print(banner)
    patx = '/data/data/com.termux/files'
    chex = os.path.exists(patx)
    
    #True
    if chex == True:
      print()
      print('\033[1;91m[*] \033[1;97mScannerX is updating in your Termux\n')
      print("\033[1;91m[*] \033[1;97mThis process can take few minutes, So Be patience\n")
      os.system("wget https://raw.githubusercontent.com/MrHacker-X/ScannerX/main/scannerx.py")
      os.system("chmod +x scannerx.py")
      os.system("rm /data/data/com.termux/ScannerX/scannerx.py")
      os.system("mv scannerx.py /data/data/com.termux/ScannerX/")
      print()
      print("\n\033[1;97m[*] \033[1;92mScannerX is updated successfully\n")
      exit()

    #False
    elif chex == False:
      print()
      print('\033[1;91m[*] \033[1;97mScannerX is updating in your Linux OS\n')
      print("\033[1;91m[*] \033[1;97mThis process can take few minutes, So Be patience\n")
      os.system("sudo wget https://raw.githubusercontent.com/MrHacker-X/ScannerX/main/scannerx.py")
      os.system("sudo chmod +x scannerx.py")
      os.system("sudo rm /usr/local/ScannerX/scannerx.py")
      os.system("sudo mv scannerx.py /usr/local/ScannerX/")
      print()
      print("\n\033[1;97m[*] \033[1;92mScannerX is updated successfully\n")
      exit()


    else:
      print()
      print('\033[1;91msomething is wrong')
      print()
      exit()
  
  elif opt == '06' or opt == '6':
    conf = input('\n\033[1;91m[*] \033[1;97mDo you really want to uninstall it [Y/n]: ')
    if conf == 'y' or conf == 'Y':
      print('\n\033[1;91m[*] \033[1;97mThanks for confirmation')
      time.sleep(0.5)
      print()

    elif conf == 'n' or conf == 'N':
      print('\n\033[1;97m[*]\033[1;91m Aborted')
      print()
      exit()

    elif conf == '':
      print('\n\033[1;91m[*] \033[1;97mThanks for confirmation')
      time.sleep(0.5)
      print()

    else:
      print('\n\033[1;97m[*] \033[1;91mAborted')
      print()
      exit()
    

    fil = '/data/data/com.termux/files'
    che = os.path.exists(fil)
    if che == True:
      print('\033[1;91m[*] \033[1;97mUninstalling ScannerX from Your termux\n')
      os.system('rm -rf /data/data/com.termux/ScannerX /data/data/com.termux/files/usr/bin/scanx')
      time.sleep(1.3)
      print('\033[1;91m[*] \033[1;97mUninstalled successfully ')
      print()
      exit()


    else:
      print('\033[1;91m[*] \033[1;97mUninstalling ScannerX from Your Linux OS\n')
      os.system('rm -rf /usr/local/bin/scanx /usr/local/ScannerX')
      time.sleep(1.3)
      print('\033[1;91m[*] \033[1;97mUninstalled successfully ')
      print()
      exit()


  elif opt == '00' or opt == '0':
    print("\n\033[1;91m[*]\033[1;97m Thanks for using ScannerX\n")
    print("\033[1;91m[*] Quiting...\n")
    time.sleep(1.5)
    exit()

  else:
    print('\n\033[1;91mInvalid Input\n')
    time.sleep(1)

