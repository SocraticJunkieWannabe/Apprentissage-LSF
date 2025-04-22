from bs4 import BeautifulSoup
import json


def addWordWrapper(word : str, link : str, sentence_container):
    video_wrapper_html = f'''
    <div class="video-wrapper">
        <video src="{link}"></video>
        <div class="video-caption">{word.capitalize()}</div>
    </div>
    '''

    new_video = BeautifulSoup(video_wrapper_html, "html.parser")
    sentence_container.append(new_video)
    pass

def addSentencesLessons():
    with open("lesson_template.html", "r", encoding="utf-8") as source:
        soup = BeautifulSoup(source, "html.parser")
    with open("sentences.json", "r", encoding="utf-8") as file:
        sentences = json.load(file)
    with open("video-links.json", "r", encoding="utf-8") as file:
        links = json.load(file)

    for sentence in sentences:
        appendSentenceToPage(sentences, sentence, links, soup)

    with open("leçon.html", "w", encoding="utf-8") as outf:
        outf.write(soup.prettify())
    pass

def appendSentenceToPage(sentences: dict, sentence : str, links : dict, soup : BeautifulSoup):
    new_sentence_div = soup.new_tag("div", **{"class": "video-container", "id": sentence})

    before_sentence = soup.new_tag("h1")
    before_sentence.string = sentence
        
    after_sentence = soup.new_tag("div", **{"class": "controls", "id": f"{sentence}"})
    button = soup.new_tag("button", id = f"{sentence}Button")
    button.string = "Lancer"
    after_sentence.append(button)

    soup.body.append(before_sentence)
    soup.body.append(new_sentence_div)
    soup.body.append(after_sentence)

    for word in sentences[sentence]:
        link = links[word]
        addWordWrapper(word, link, new_sentence_div)
    pass

addSentencesLessons()


