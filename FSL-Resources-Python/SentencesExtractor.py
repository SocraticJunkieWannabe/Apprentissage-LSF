import json

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

def downloadJSON(phrases):
    with open("sentences.json", "w", encoding="utf-8") as f:
        json.dump(phrases, f, indent=4, ensure_ascii=False)
    pass

downloadJSON(phrases_asl)