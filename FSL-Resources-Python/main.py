import VideoExtractor as ve

phrases_asl = {
    "salut_ca_va": ["salut", "ça va"],
    "tu_fais_quoi": ["toi", "faire", "quoi"],
    "tu_veux_manger_avec_moi": ["toi", "vouloir", "manger", "avec", "moi"],
    "aimer_musique": ["moi", "aimer", "cette", "musique"],
    "content_te_voir": ["moi", "content", "voir", "toi"],
    "je_suis_fatigue": ["moi", "fatigué"],
    "on_y_va": ["nous", "aller"],
    "il_fait_froid": ["aujourd'hui", "froid"],
    "mal_a_la_tete": ["moi", "mal", "tête"],
    "mal_a_la_tete": ["moi", "mal", "ventre"],
    "tu_as_compris": ["toi", "comprendre"],
    "je_sais_pas": ["moi", "pas", "savoir"],
    "tu_es_occupe": ["toi", "occupé"],
    "a_tout_a_l_heure": ["tout à l'heure"],
    "desole_oublie": ["désolé", "moi", "oublier"],
    "je_taime": ["moi", "aimer", "toi"],
    "tu_me_manques": ["toi", "manquer", "moi"],
    "tu_veux_calin": ["toi", "vouloir", "câlin"],
    "je_pense_a_toi": ["moi", "penser", "toi"],
    "tu_veux_me_parler": ["toi", "vouloir", "parler", "moi"],
    "je_confiance_en_toi": ["moi", "confiance", "toi"],
    "ca_va_mieux": ["ça va", "mieux"],
    "tu_veux_etre_seul": ["toi", "vouloir", "être", "seul"],
    "tu_es_sexy": ["toi", "sexy"],
    "je_veux_te_sentir": ["moi", "vouloir", "sentir", "toi"],
    "aide_moi": ["aide", "moi"],
    "je_suis_en_colere": ["moi", "colère"]
}

words = []
for sentence in phrases_asl:
    for word in phrases_asl[sentence]:
        if word not in words:
            words.append(word)
 
def checkIfWordsInDatabase():      
    with open("mots_elix.txt", "r", encoding="utf8") as f:
        content = f.read()
        for word in words:
            if word not in content:
                print(f'{word} not in database')
                return False
    return True

ve.downloadVideos(words, "json")