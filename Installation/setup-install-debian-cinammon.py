import os
import time
import json
import sys
import subprocess
from datetime import datetime

# horas & sistema & shell
agora = datetime.now()
system = sys.platform
nano = "apt install nano -y"
adduser = "apt install adduser -y"
sudo = "apt install sudo -y"
clear = "clear"
upgrade = "apt upgrade -y"

int()

# banner e cor do Gato Félix
banner = subprocess.check_output(['figlet', "Felix The Cat"]).decode('utf-8')
vermelho = "\033[91m"
amarelo = "\033[93m"
reset = "\033[0m]"

def limpar_tela():
  if system == "windows" or system == "Windows":
    os.system("cls")
  else:
    os.system(clear)

def system_windows():
  if system == "windows" or system == "Windows":
    print("[!] o script não foi feito para Windows apenas para termux!")

def system_termux():
  if system == "linux" and os.path.exists("/data/data/com.termux"):
    return "Termux"
  else:
    return system
    
termux = system_termux()

limpar_tela()
print(banner)
print(f"{amarelo}[✓] Script By Diogo{reset}")
print(f"{amarelo}[✓] Hora atual: {agora.hour:02d}:{agora.minute:02d}:{agora.second:02d}{reset}")
system_windows()
time.sleep(1.5)
try:
  if termux == "Termux":
    print(f"{amarelo}[/] Instalando nano{reset}")
    time.sleep(0.5)
    os.system(nano)
    print(f"{amarelo}[✓] Instalação nano concluida!{reset}")
    time.sleep(0.5)
    print(f"{amarelo}[/] Instalando adduser{reset}")
    time.sleep(0.5)
    os.system(adduser)
    print(f"{amarelo}[✓] Instalação adduser concluida!{reset}")
    time.sleep(0.5)
    print(f"{amarelo}[/] Instalando sudo{reset}")
    time.sleep(0.5)
    os.system(sudo)
    print(f"{amarelo}[✓] Instalação sudo concluida!{reset}")
    time.sleep(0.5)
    print(f"{amarelo}[/] Atualizando apt upgrade{reset}")
    os.system(upgrade)
    time.sleep(0.5)
    print(f"{amarelo}[✓] Todos os pacotes e upgrade instalado!{reset}")
    time.sleep(2.5)
    os.system(clear)
    user = input("Digite o seu usuário: ")
    full_name = input("Digite o full-name do usuário: ")
    senha = input("Digite uma senha para o usuário: ")
    usuario = {
      "user": user,
      "full_name": full_name,
      "senha": senha
    }
    user_atual = os.path.dirname(__file__)
    user_arquivo = os.path.join(user_atual, "Dados", "user.json")
    with open(user_arquivo, "w") as arquivo:
      json.dump(usuario, arquivo, indent=4)
    os.system(f"useradd -M -s /bin/bash -c '{full_name}' {user}")
    os.system(f"echo {user}:{senha} | chpasswd")
    os.system(f"echo '{user} ALL=(ALL:ALL) ALL' | sudo EDITOR='tee -a' visudo")
    os.system(f"echo 'proot-distro login --user {user} debian' >> $PREFIX/data/data/com.termux/files/usr/bin/debian")
    os.system("chmod +x /data/data/com.termux/files/usr/bin/debian")
    os.system("exit")
except ValueError:
  print(f"{vermelho}[X] ERROR ValueError{reset}")
except KeyboardInterrupt:
  print(f"{vermelho}[!] Forçamento com CTRL + C{reset}")
  exit()