import random
import re

def get_file_str(file):
    file = open(file, 'r', encoding='utf-8')
    content = file.read()
    file.close()
    return content

def write_txt(what, where):
    doc = open(where, 'w', encoding='utf-8')
    doc.write(what)
    doc.close()

def randomize_stimulus_in_html(lang):
    html = get_file_str('templates/' + lang + '_template.html')

    numbers = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16"]

    for i in range(1,17):
        template = "N" + str(i) + "N"
        html = html.replace(template, random.choice(numbers))

    write_txt(html, "templates/en_pictures.html")


randomize_stimulus_in_html('en')