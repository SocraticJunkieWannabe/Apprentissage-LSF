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
    with open("sentences.json", "r", encoding="utf-8") as file:
        sentences = json.load(file)
    with open("video-links.json", "r", encoding="utf-8") as file:
        links = json.load(file)

    file_names = []

    for sentence in sentences:
        with open("lesson_template.html", "r", encoding="utf-8") as source:
            soup = BeautifulSoup(source, "html.parser")

        createSentencePage(sentences, sentence, links, soup)
        sentence = sentence.replace('?', "").replace(" ", "_").replace(",", "")
        title = sentence.replace("À", "A").replace("à", "a").replace("ç", "c")
        file_name = f"lesson_{title}"
        file_names.append(file_name)
        with open(f"Output\\{file_name}.html", "w", encoding="utf-8") as outf:
            outf.write(soup.prettify())
    
    with open("Output\\files.json","w", encoding="utf-8") as outf:
        json.dump(file_names, outf, indent=4, ensure_ascii=False)

    pass

def createSentencePage(sentences: dict, sentence : str, links : dict, soup : BeautifulSoup):
    new_content_div = soup.new_tag("div", **{"class": "lesson-content"})
    new_sentence_div = soup.new_tag("div", **{"class": "video-container", "id": sentence})

    before_sentence = soup.new_tag("h1")
    before_sentence.string = sentence
        
    after_sentence = soup.new_tag("div", **{"class": "controls", "id": f"{sentence}"})
    button = soup.new_tag("button", **{"class": "button-primary", "id": "playButton"})
    button.string = "Lancer"
    after_sentence.append(button)

    new_content_div.append(before_sentence)
    new_content_div.append(new_sentence_div)
    new_content_div.append(after_sentence)

    soup.body.append(new_content_div)

    for word in sentences[sentence]:
        link = links[word]
        addWordWrapper(word, link, new_sentence_div)
    pass

addSentencesLessons()


