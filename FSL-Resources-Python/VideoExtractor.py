import requests 
from bs4 import BeautifulSoup
import json

def downloadVideos(words: list, tag : str):
    links = extractVideoLinks(words)
    
    if tag == "mp4":
        for link in links:
            downloadVideo(link, links[link])
    elif tag == "json":
        downloadJSON(links)
    pass

def extractVideoLinks(words : list):
    links = {}
    for word in words:
        link = extractFromElix(word)
        links[word] = link
        
    return links

def extractFromElix(word):
    Elix_link = "https://dico.elix-lsf.fr/dictionnaire/"
    elix_url = f"{Elix_link}{word}"
    
    page = requests.get(elix_url)
    htmlData = BeautifulSoup(page.content, "html.parser")
    try:
        area1 = htmlData.find("ul", class_ = "sign-list single")
        link = area1.find("video")["src"]
        return link
    except:
        link = extractFromSematos(word)
        return link
    
def extractFromSematos(word):
    sematos_url = f"https://www.sematos.eu/lsf-p-{word}-7832-fr.html"
    page = requests.get(sematos_url)
    
    htmlData = BeautifulSoup(page.content, "html.parser")
    try:
        area1 = htmlData.find("div", id = "playermot")
        link = area1.find("source")["src"]
        return link
    except:
        print("no sign video available in sematos")
        return None
    
def downloadVideo(file_name, vid_link):
    save_path = f"Video Database/{file_name}.mp4"

    # Stream the download
    response = requests.get(vid_link, stream=True)

    # Check if the request was successful
    if response.status_code == 200:
        with open(save_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"{file_name} downloaded!")
    else:
        print(f"Failed to download. Status code: {response.status_code}")
        
def downloadJSON(links):
    with open("video-links.json", "w", encoding="utf-8") as f:
        json.dump(links, f, indent=4, ensure_ascii=False)
    pass