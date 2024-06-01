from pdf2docx import Converter
from docx import Document
import string
import re

#from json_manager import ResumeManager
def validate_email(email):
    if re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
        return email


def validate_phone_number(phone_number):
    match = re.search(re.compile(r"(\+\d{1,3})?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}"), phone_number)
    if match:
        return phone_number


def rtf_or_doc_to_docx(rtf_path, docx_path):
    f = open(docx_path, 'w')
    f.write(open(rtf_path, 'r').read())
    print(f"Converted {rtf_path} to {docx_path}")


def pdf_to_docx(pdf_path, docx_path):
    """Convert PDF to DOCX"""
    cv = Converter(pdf_path)
    cv.convert(docx_path)
    cv.close()
    print(f"Converted {pdf_path} to {docx_path}")


def docx_to_txt(docx_path, txt_path):
    """Convert DOCX to TXT"""
    doc = Document(docx_path)
    with (open(txt_path, 'w', encoding='utf-8') as txt_file):
        for para in doc.paragraphs:
            txt_file.write(para.text + '\n')
    print(f"Converted {docx_path} to {txt_path}")


def checkLeftLastName(lastword, lastnames):
    for lastName in lastnames.split():
        if lastword == lastName:
            return lastName


def findCompetitionSystemAnalytic(resume, competitions):
    listOfNeedsCompetition = []
    for word in resume:
        for competition in competitions:
            if competition == word:
                listOfNeedsCompetition.append(word)
    return listOfNeedsCompetition


if __name__ == "__main__":

    # path for test docs
    pdf_path = "test1.pdf"
    docx_path = "example.docx"
    # example.doc
    rtf_or_doc_path = "example.rtf"
    txt_path = "example.txt"

    # Convert PDF to DOCX
    pdf_to_docx(pdf_path, "example.docx")
    # Convert RTF to DOCX
    rtf_or_doc_to_docx(rtf_or_doc_path, "docx_from_rtf.docx")
    # Convert DOCX to TXT
    docx_to_txt(docx_path, txt_path)

    path_Names = 'Names.txt'
    path_LastNames = 'LastNames.txt'
    path_SurNames = 'SurNames.txt'

    with open(path_Names, 'r',encoding='utf-8') as file:
        names = file.read()
    with open(path_LastNames, 'r',encoding='utf-8') as file:
        lastNames = file.read()
    with open(path_SurNames, 'r',encoding='utf-8') as file:
        surNames = file.read()

    path_competitions = "Competentions.txt"
    with open(path_competitions, 'r',encoding='utf-8') as file:
        competitions = file.read()

    with open(txt_path, 'r',encoding='utf-8') as file:
        data = re.compile('[%s]' % re.escape(string.punctuation)).sub('', file.read().replace('\n', ' ')).split()

    for word in data:
        email = validate_email(word)
        if email is not None:
            print(email)
        phoneNumber = validate_phone_number(word)
        if phoneNumber is not None:
            print(phoneNumber)

    lastWord = 'Test'
    full_name = None
    json_file_path = "db.json"
    manager = ResumeManager(json_file_path)

    for word in data:
        for name in names.split():
            if word == name:
                result = checkLeftLastName(lastWord, lastNames)
                if result is not None:
                    # Имя, Фамилия (чек её слева), Отчество (по остаточному принципу)
                    # Работает без ошибок, если всегда есть очтество

                    print(name, result, data[data.index(word) + 1])
                    full_name = name + ' ' + result + ' ' + data[data.index(word) + 1]
                    break
                else:
                    index = data.index(word) + 1
                    # Имя, Фамилия, Отчество (по остаточному принципу)
                    # Работает без ошибок, если всегда есть очтество
                    full_name = name + ' ' + data[index] + ' ' + data[index + 1]
                    print(name, data[index], data[index + 1])
                    break
        lastWord = word

    listOfNeedCompetition = findCompetitionSystemAnalytic(data, competitions.split())
    for elem in listOfNeedCompetition:
       print(elem)

    manager.create_resume(full_name, listOfNeedCompetition)

