import os

import spacy
import docx
import fitz  # PyMuPDF
from findFIO import findName
nlp = spacy.load("ru_core_news_sm")
file_paths = None

def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_info(text):
    entities = {
        'NAME': '',
        'EDUCATION': '',
        'SKILLS': '',
        'EXPERIENCE': ''
    }

    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PER" and not entities['NAME']:
            entities['NAME'] = ent.text
        elif ent.label_ in ["ORG", "GPE"] and any(keyword in ent.text.lower() for keyword in ["университет", "институт", "образование"]):
            entities['EDUCATION'] += ent.text + "\n"

    skill_keywords = ["навыки", "умения", "ключевые навыки"]
    experience_keywords = ["опыт работы", "работал", "работала", "работы", "должность"]
    education_keywords = ["университет", "институт", "образование"]

    lines = text.split('\n')
    current_section = None
    for line in lines:
        line = line.strip()
        if any(keyword in line.lower() for keyword in skill_keywords):
            current_section = 'SKILLS'
            continue
        elif any(keyword in line.lower() for keyword in experience_keywords):
            current_section = 'EXPERIENCE'
            continue
        elif any(keyword in line.lower() for keyword in education_keywords):
            current_section = 'EDUCATION'
            continue

        if current_section == 'SKILLS':
            entities['SKILLS'] += line + "\n"
        elif current_section == 'EXPERIENCE':
            entities['EXPERIENCE'] += line + "\n"
        elif current_section == 'EDUCATION':
            entities['EDUCATION'] += line + "\n"

    return entities

def print_entities(entities, file_name):
    # document_info_list.append(
    #    DocumentInfo(
    #        file_name=file_name,
    #        name=entities['NAME'],
    #        education=entities['EDUCATION'],
    #        skills=entities['SKILLS'],
    #        experience=entities['EXPERIENCE']
    #    )
    # )
    print(f"Entities from {file_name}:")
    for category, item in entities.items():
        if item.strip():
            print(f"\n{category}:")
            print(f"{item.strip()}\n")


def set_file_path(file_path):
    text = ' '
    if file_path.endswith('.docx'):
        text = extract_text_from_docx(file_path)
    elif file_path.endswith('.pdf'):
        text = extract_text_from_pdf(file_path)
    entities = extract_info(text)
    print_entities(entities, os.path.basename(file_path))
