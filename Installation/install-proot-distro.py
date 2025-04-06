import os
import time
import json
import sys
import subprocess
from colorama import init, Fore
from datetime import datetime

# horas & sistema & shell
agora = datetime.now()
system = sys.platform
update = "pkg update && apt update"
clear = "clear"
upgrade = "pkg upgrade -y ; apt upgrade -y"
proot_distro = "pkg install proot-distro -y ; apt install proot-distro -y"

init()

# banner e cor do Gato Félix
banner = subprocess.check_output(['figlet', "Felix The Cat"]).decode('utf-8')
vermelho = "\033[91m"
amarelo = Fore.YELLOW

def limpar_tela():
  if system == "windows" or system == "Windows":
    cls = "cls"
    os.system(cls)
  else:
    clear = "clear"
    os.system(clear)

def system_windows():
  if system == "windows" or system == "Windows":
    print("[!] Esse Script Não foi feito para windows apenas para Termux!")
    exit()

def system_termux():
  if system == "linux" and os.path.exists("/data/data/com.termux"):
    return "Termux"
  else:
    return system
    
def debian_system():
  print(f"{amarelo}[/] Executando pkg update & apt update...{Fore.RESET}")
  time.sleep(1)
  os.system(update)
  print(f"{amarelo}[✓] Atualização concluida!{Fore.RESET}")
  time.sleep(1.5)
  print(f"{amarelo}[/] Executando pkg upgrade & apt upgrade...{Fore.RESET}")
  os.system(upgrade)
  print(f"{amarelo}[✓] Instalação concluida!{Fore.RESET}")
  time.sleep(1.5)
  print(f"{amarelo}[/] Executando pkg install proot-distro...{Fore.RESET}")
  os.system(proot_distro)
  print(f"{amarelo}[✓] Instalação concluida!{Fore.RESET}")
  time.sleep(1.5)
  os.system(clear)
  print(f"{amarelo}[/] Instalando o Debian...{Fore.RESET}")
  os.system("proot-distro install debian")
  time.sleep(1.5)
  os.system(clear)
  print(f"{amarelo}[/] Login no Debian...{Fore.RESET}")
  time.sleep(1.5)
  os.system("proot-distro login debian -- bash -c 'cd / && apt update && apt install git python3 && git clone https://github.com/felix-the-cat177/Linux-installation-2025.git && cd Linux-installation-2025 && cd Installation && python setup-install-debian-cinammon.py'")
  with open("Dados/user.json", "r") as user_json:
    usuario = json.load(user_json)
    user = usuario["user"]
    os.system(clear)
    os.system(f"proot-distro login --user root debian -- apt install cinnamon-desktop-environment -y")
  
termux = system_termux()

limpar_tela()
print(f"{banner}")
print(f"{amarelo}[✓] Script By Diogo{Fore.RESET}")
print(f"{amarelo}[✓] Hora atual: {agora.hour:02d}:{agora.minute:02d}:{agora.second:02d}{Fore.RESET}")
system_windows()
try:
  if termux == "Termux":
    print("")
    print("1- Debian + Cinammon")
    opcao = int(input("Digite a opção: "))
    if opcao == 1:
      debian_system()
except ValueError:
  print(f"{vermelho}[X] opção inválida coloque apenas números...")
  time.sleep(1)
  