from datetime import datetime
import random
import os

# Color codes
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    CYAN = '\033[96m'

def clear_console():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_banner():
    clear_console()
    print(f"""{Colors.HEADER}{Colors.BOLD}
   ▄████▄   ▒█████   ███▄ ▄███▓ ▄▄▄       ██▀███  
  ▒██▀ ▀█  ▒██▒  ██▒▓██▒▀█▀ ██▒▒████▄    ▓██ ▒ ██▒
  ▒▓█    ▄ ▒██░  ██▒▓██    ▓██░▒██  ▀█▄  ▓██ ░▄█ ▒
  ▒▓▓▄ ▄██▒▒██   ██░▒██    ▒██ ░██▄▄▄▄██ ▒██▀▀█▄  
  ▒ ▓███▀ ░░ ████▓▒░▒██▒   ░██▒ ▓█   ▓██▒░██▓ ▒██▒
  ░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░
    ░  ▒     ░ ▒ ▒░ ░  ░      ░  ▒   ▒▒ ░  ░▒ ░ ▒░
  ░        ░ ░ ░ ▒  ░      ░     ░   ▒     ░░   ░ 
  ░ ░          ░ ░         ░         ░  ░   ░     
  ░                                              
{Colors.END}{Colors.CYAN}     ⚡ Auto Comment Console | By Saiim Lejend ⚡
{Colors.END}""")

def log_success(msg):
    print(f"{Colors.GREEN}[✓] {datetime.now().strftime('%H:%M:%S')} - {msg}{Colors.END}")

def log_info(msg):
    print(f"{Colors.BLUE}[i] {datetime.now().strftime('%H:%M:%S')} - {msg}{Colors.END}")

def log_warn(msg):
    print(f"{Colors.WARNING}[!] {datetime.now().strftime('%H:%M:%S')} - {msg}{Colors.END}")

def log_error(msg):
    print(f"{Colors.FAIL}[×] {datetime.now().strftime('%H:%M:%S')} - {msg}{Colors.END}")

# Example Usage:
if __name__ == "__main__":
    print_banner()
    log_info("Tool Started...")
    log_success("Comment sent using Token #1")
    log_warn("Waiting for next token rotation...")
    log_error("Failed to send comment! Retrying...")
