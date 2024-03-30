import requests
from bs4 import BeautifulSoup
import os

history = []

def show_content(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            for p in soup.find_all('p'):
                print(p.get_text())
        else:
            print(f"\033[31mERROR. Status code : {response.status_code}\033[0m")
    except requests.RequestException as e:
        print("\033[31mAn error occurred while fetching the content:", e, "\033[0m")

def main():
    os.system("clear")
    print("""
    
=========================================
__      __.____    .__                
/  \    /  \    |   |__| ____   ____   
\   \/\/   /    |   |  |/    \_/ __ \  
\        /|    |___|  |   |  \  ___/  
\__/\  / |_______ \__|___|  /\___  > 
    \/          \/       \/     \/  

==========================================
Offline CLI web browser.
License : BSD-3 Clause
Version 1.0.0
    """)

    while True:
        print("\033[1;36m", end="")
        url = input("Enter command (help for more infos) : \033[0m").strip()
        if url:
            history.append(url)

        if url.lower() == 'q':
            print("Goodbye !")
            os.system("clear")
            break

        elif url == 'history':
            print("\033[38;5;22mHistory of your current session :\033[0m")
            for item in history:
                print(item)

        elif url == 'history clear':
            history.clear()
            print("History cleared.")

        elif url == 'history rm':
            remove_history = input("Remove in history : ")
            if remove_history in history:
                history.remove(remove_history)
                print("Successfully removed.")
            else:
                print("\033[31mIt is not in history.\033[0m")

        elif url == 'help':
            print("\033[1;33mCommands list :\033[0m")
            print("[URL] : enter an URL to go to page")
            print("history : show the history of your cuurent session")
            print("back : back to one page")
            print("history clear : clear the history")
            print("history rm : remove something from the history")
            print("q : quit")

        elif url == 'back':
            if len(history) > 1:
                history.pop()
                show_content(history[-1])
            else:
                print("\033[31mNo previous page in history.\033[0m")
        else:
            show_content(url)

if __name__ == "__main__":
    main()
