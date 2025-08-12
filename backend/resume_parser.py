import spacy

nlp = spacy.load("en_core_web_sm")

def extract_skills_from_resume(resume_text):
    doc = nlp(resume_text)
    skills = set()
    for ent in doc.ents:
        if ent.label_ in ["ORG", "PRODUCT", "SKILL", "TECHNOLOGY", "WORK_OF_ART"]:
            skills.add(ent.text)
    tokens = [token.text.lower() for token in doc if token.pos_ in ["NOUN", "PROPN"] and token.is_alpha]
    keywords = [word for word in tokens if word not in nlp.Defaults.stop_words]
    top_keywords = list(set(keywords))[:10]
    return list(skills.union(top_keywords))