import os
import subprocess
from colorama import init, Fore, Style

import os
import subprocess
from colorama import init, Fore, Style


os.system('cls' if os.name == 'Multi Tools By Sandati' else 'clear')

init(autoreset=True)

os.system('cls' if os.name == 'Multi Tools By Sandati' else 'clear')

init(autoreset=True)

def display_ascii_art():
    art = f""" {Fore.RED}            
               
    
           ██▀███  ▓█████ ▓█████▄      █████▒██▓    ▄▄▄        ▄████    
           ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌   ▓██   ▒▓██▒   ▒████▄     ██▒ ▀█▒   
           ▓██ ░▄█ ▒▒███   ░██   █▌   ▒████ ░▒██░   ▒██  ▀█▄  ▒██░▄▄▄░   
           ▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌   ░▓█▒  ░▒██░   ░██▄▄▄▄██ ░▓█  ██▓   
           ░██▓ ▒██▒░▒████▒░▒████▓    ░▒█░   ░██████▒▓█   ▓██▒░▒▓███▀▒   
           ░▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒     ▒ ░   ░ ▒░▓  ░▒▒   ▓▒█░ ░▒   ▒    
             ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒     ░     ░ ░ ▒  ░ ▒   ▒▒ ░  ░   ░    
             ░░   ░    ░    ░ ░  ░     ░ ░     ░ ░    ░   ▒   ░ ░   ░    
              ░        ░  ░   ░                  ░  ░     ░  ░      ░    
                            ░                                            


                 Developers : ! " Sandati " シ(sandativ4)
          ────────────────────────────────────────────────────────────────────────────────────────── 
                 Version : 3.0
          ──────────────────────────────────────────────────────────────────────────────────────────
                 Website : https://qwartaungen.x10.mx/
          ──────────────────────────────────────────────────────────────────────────────────────────

     
      ╒═════════════════════════════════════════════════════════════════════════════════════════════════╕                                              
      │ 1 - Account Nuker           │ 26 - Token Generator           │ 51 - Token Leaver                │                                           
      │ 2 - Badge Changer           │ 27 - Dos Voice                 │ 52 - Token Saver                 │
      │ 3 - Clear Dm                │ 28 - Dox Create                │ 53 - Token Server Nicker         │                                       
      │ 4 - Group Spammer           │ 29 - Password Encrypted        │ 54 - Token Typer                 │                                      
      │ 5 - Server Info             │ 30 - Server Nuker              │ 55 - Discord Token Block Friends │                                       
      │ 6 - Status Rotator          │ 31 - Token Joiner Server       │ 56 - Discord Token Delete Friends│
      │ 7 - Token Checker           │ 32 - Dox-Tracker-(OSINT)       │ 57 - Discord Webhook Delete      │        
      │ 8 - Token Mass Dm           │ 33 - Sql-Vulnerability         │ 58 - Dark Web                    │      
      │ 9 - Webhook Info            │ 34 - Ip-Port-Scanner           │ 59 - Password Decrypted          │      
      │ 10 - Webhook Spammer        │ 35 - Bot ID-To-Invite          │ 60 - Phishing Attack             │
      │ 11 - Ip Information         │ 36 - Ip-Generator              │ 61 - Roblox Cookie Info          │
      │ 12 - Email Information      │ 37 - Ip-Pinger                 │ 62 - Roblox Cookie Login         │
      │ 13 - Number Information     │ 38 - Id to Token               │ 63 - Roblox Id Info              │
      │ 14 - Get your Ip            │ 39 - Nitro Check               │ 64 -                             │
      │ 15 - Roblox Id Information  │ 40 - DDOS                      │ 65 -                             │
      │ 16 - Token Information      │ 41 - SoundBoard Spammer        │ 66 -                             │
      │ 17 - Roblox User Inforamtion│ 42 - Mass Report               │ 67 -                             │
      │ 18 - Username Tracker       │ 43 - IP Open Port              │ 68 -                             │
      │ 19 - Nitro Generator        │ 44 - IP Localisation           │ 69 -                             │
      │ 20 - Tools Information      │ 45 - Generator                 │ 70 -                             │
      │ 21 - Number Scrapper        │ 46 - Discord Token Bruteforce  │ 71 -                             │
      │ 22 - Website Scrapper       │ 47 - SNUSBASE                  │ 72 -                             │
      │ 23 - IBAN Generator         │ 48 - Discord Change Settings   │ 73 -                             │
      │ 24 - CC Generator           │ 49 - Email Bomber              │ 74 -                             │
      │ 25 - Obfuscator             │ 50 - Bypass Rules              │ 75 -                             │
      ╘═════════════════════════════════════════════════════════════════════════════════════════════════╛
"""
    print(art)

def execute_script(script_name):
    script_path = os.path.join('utils', f'{script_name}')
    try:
        subprocess.run(['python', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing script '{script_name}': {e}")

def main():
    display_ascii_art()
    while True:
        choice = input(Fore.RED + "Choose an option:  " + Style.RESET_ALL)

        if choice == '1':
            execute_script('account_nuker.py')
        elif choice == '2':
            execute_script('badge_changer.py')
        elif choice == '3':
            execute_script('clear_dm.py')
        elif choice == '4':
            execute_script('groupe_spammer.py')
        elif choice == '5':
            execute_script('server_info.py')
        elif choice == '6':
            execute_script('status_rotator.py')
        elif choice == '7':
            execute_script('token_checker.py')
        elif choice == '8':
            execute_script('token_massdm.py')
        elif choice == '9':
            execute_script('webhook_info.py')
        elif choice == '10':
            execute_script('webhook_spammer.py')
        elif choice == '11':
            execute_script('ip_info.py')
        elif choice == '12':
            execute_script('email_info.py')
        elif choice == '13':
            execute_script('number_info.py')
        elif choice == '14':
            execute_script('get_ip.py')
        elif choice == '15':
            execute_script('roblox_id_info.py')
        elif choice == '16':
            execute_script('token_info.py')
        elif choice == '17':
            execute_script('roblox_user_info.py')
        elif choice == '18':
            execute_script('username_tracker.py')
        elif choice == '19':
            execute_script('nitro_generator.py')
        elif choice == '20':
            execute_script('tools_info.py')
        elif choice == '21':
            execute_script('scrapper_number.py')
        elif choice == '22':
            execute_script('website_scraper.py')
        elif choice == '23':
            execute_script('iban_scrapper.py')
        elif choice == '24':
            execute_script('credit_card_scrapper.py')
        elif choice == '25':
            execute_script('obfuscator.py')
        elif choice == '26':
            execute_script('token_generator.py')
        elif choice == '27':
            execute_script('dos_voice.py')
        elif choice == '28':
            execute_script('dox-create.py')
        elif choice == '29':
            execute_script('password-encrypted.py')
        elif choice == '30':
            execute_script('server-nuker.py')
        elif choice == '31':
            execute_script('token-joiner.py')
        elif choice == '32':
            execute_script('dox-tracker-(OSINT).py')
        elif choice == '33':
            execute_script('Sql-Vulnerability.py')
        elif choice == '34':
            execute_script('Ip-Port-Scanner.py')
        elif choice == '35':
            execute_script('Discord-Bot-ID-To-Invite.py')
        elif choice == '36':
            execute_script('Ip-Generator.py')
        elif choice == '37':
            execute_script('Ip-Pinger.py')
        elif choice == '38':
            execute_script('ID-To-Token.py')
        elif choice == '39':
            execute_script('NitroCheck.py')
        elif choice == '40':
            execute_script('DDOS.py')
        elif choice == '41':
            execute_script('soundboard_spammer.py')
        elif choice == '42':
            execute_script('mass_report.py')
        elif choice == '43':
            execute_script('IP_openport.py')
        elif choice == '44':
            execute_script('IP_localisation.py')
        elif choice == '45':
            execute_script('generator.py')
        elif choice == '46':
            execute_script('discord-token-bruteforce.py')
        elif choice == '47':
            execute_script('snusbase.py')
        elif choice == '48':
            execute_script('settingscycler.py')
        elif choice == '49':
            execute_script('email-bomber.py')
        elif choice == '50':
            execute_script('bypass_rules.py')
        elif choice == '51':
            execute_script('token_leaver.py')
        elif choice == '52':
            execute_script('token_saver.py')
        elif choice == '53':
            execute_script('token_server_nicker.py')
        elif choice == '54':
            execute_script('token_typer.py')
        elif choice == '55':
            execute_script('Discord-Token-Block-Friends.py')
        elif choice == '56':
            execute_script('Discord-Token-Delete-Friends.py')
        elif choice == '57':
            execute_script('Discord-Webhook-Delete.py')
        elif choice == '58':
            execute_script('Dark_Web.py')
        elif choice == '59':
            execute_script('Password-Decrypted.py')
        elif choice == '60':
            execute_script('Phishing-Attack.py')
        elif choice == '61':
            execute_script('Roblox-Cookie-Info.py')
        elif choice == '62':
            execute_script('Roblox-Cookie-Login.py')
        elif choice == '63':
            execute_script('Roblox-Id-Login.py')
        elif choice == '64':
            execute_script('Website-Scanner.py')
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
