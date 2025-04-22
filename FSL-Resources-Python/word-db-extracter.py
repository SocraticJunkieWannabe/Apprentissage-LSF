import requests
from bs4 import BeautifulSoup
import time

BASE_URL = "https://dico.elix-lsf.fr/index-alphabetique/"

def get_words_from_letter(letter):
    page_number = 100
    words = []
    
    for i in range(1, page_number):
        try:
            url = f"{BASE_URL}{letter}/{i}"
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Chaque mot est dans un <li> avec <a> contenant le mot
            
            word_area = soup.select("ul.words li a")
            
            if len(word_area) != 0:
                for li in word_area:
                    word = li.get_text(strip=True)
                    words.append(word)
                print(f'page {i} scanned')
            else:
                print("no more pages")
                break
        except:
            print("no more pages")
            break
    print(f"{len(words)} words found")
    return words

def scrape_all_words():
    all_words = []
    test = "a"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        print(f"Scraping letter: {letter.upper()}")
        try:
            words = get_words_from_letter(letter)
            all_words.extend(words)
        except Exception as e:
            print(f"Erreur avec la lettre {letter}: {e}")
        time.sleep(1)  # éviter de surcharger le site

    return all_words

if __name__ == "__main__":
    words = scrape_all_words()
    print(f"\nTotal de mots récupérés : {len(words)}")
    with open("mots_elix.txt", "w", encoding="utf-8") as f:
        for word in sorted(set(words)):
            f.write(word + "\n")
