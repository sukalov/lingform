from flask import Flask
from flask import url_for, render_template, request, redirect
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
        a = random.choice(numbers)
        numbers.remove(a)
        html = html.replace(template, a)

    write_txt(html, "templates/" + lang + "_pictures.html")


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/ru')
def rus():
    if request.args:
        results = open("results.tsv", 'a', encoding='utf-8')
        sex = request.args['sex']
        age = request.args['age']
        land1 = request.args['land1']
        land2 = request.args['land2']
        language = request.args['language']
        languages = request.args['languages']
        try:
            email = request.args['email']
        except:
            email = ""
        try:
            langcomment = request.args['langcomment']
        except:
            langcomment = ""
        results.write(sex + '\t' + age + '\t' + land1 + '\t' + land2 + '\t' + language + '\t' + languages + '\t' + email + '\t' + langcomment + '\t')
        results.close()
        randomize_stimulus_in_html("ru")
        return redirect(url_for("rus_instruction"))
    return render_template('ru_private.html')


@app.route('/ruinstruction')
def rus_instruction():
    return render_template('ru_instruction.html')

@app.route('/ruform')
def rus_form():
    if request.args:
        results = open("results.tsv", 'a', encoding='utf-8')
        try:
            T011 = request.args['T011']
        except:
            T011 = ""
        try:
            T012 = request.args['T012']
        except:
            T012 = ""
        try:
            T021 = request.args['T021']
        except:
            T021 = ""
        try:
            T022 = request.args['T022']
        except:
            T022 = ""
        try:
            T031 = request.args['T031']
        except:
            T031 = ""
        try:
            T032 = request.args['T032']
        except:
            T032 = ""
        try:
            T041 = request.args['T041']
        except:
            T041 = ""
        try:
            T042 = request.args['T042']
        except:
            T042 = ""
        try:
            T051 = request.args['T051']
        except:
            T051 = ""
        try:
            T052 = request.args['T052']
        except:
            T052 = ""
        try:
            T061 = request.args['T061']
        except:
            T061 = ""
        try:
            T062 = request.args['T062']
        except:
            T062 = ""
        try:
            T071 = request.args['T071']
        except:
            T071 = ""
        try:
            T072 = request.args['T072']
        except:
            T072 = ""
        try:
            T081 = request.args['T081']
        except:
            T081 = ""
        try:
            T082 = request.args['T082']
        except:
            T082 = ""
        try:
            T091 = request.args['T091']
        except:
            T091 = ""
        try:
            T092 = request.args['T092']
        except:
            T092 = ""
        try:
            T101 = request.args['T101']
        except:
            T101 = ""
        try:
            T102 = request.args['T102']
        except:
            T102 = ""
        try:
            T111 = request.args['T111']
        except:
            T111 = ""
        try:
            T112 = request.args['T112']
        except:
            T112 = ""
        try:
            T121 = request.args['T121']
        except:
            T121 = ""
        try:
            T122 = request.args['T122']
        except:
            T122 = ""
        try:
            T131 = request.args['T131']
        except:
            T131 = ""
        try:
            T132 = request.args['T132']
        except:
            T132 = ""
        try:
            T141 = request.args['T141']
        except:
            T141 = ""
        try:
            T142 = request.args['T142']
        except:
            T142 = ""
        try:
            T151 = request.args['T151']
        except:
            T151 = ""
        try:
            T152 = request.args['T152']
        except:
            T152 = ""
        try:
            T161 = request.args['T161']
        except:
            T161 = ""
        try:
            T162 = request.args['T162']
        except:
            T162 = ""

        results.write(T011 + '\t' + T012 + '\t' + T021 + '\t' + T022 + '\t' + T031 + '\t' + T032 + '\t' + T041 + '\t' + T042 + '\t' + T051 + '\t' + T052 + '\t' + T061 + '\t' + T062 + '\t' + T071 + '\t' + T072 + '\t' + T081 + '\t' + T082 + '\t' + T091 + '\t' + T092 + '\t' + T101 + '\t' + T102 + '\t' + T111 + '\t' + T112 + '\t' + T121 + '\t' + T122 + '\t' + T131 + '\t' + T132 + '\t' + T141 + '\t' + T142 + '\t' + T151 + '\t' + T152 + '\t' + T161 + '\t' + T162 + '\t')
        results.close()
        return redirect(url_for('rus_comment'))
    return render_template('ru_pictures.html')

@app.route('/rucomment')
def rus_comment():
    if request.args:
        results = open("results.tsv", 'a', encoding='utf-8')
        try:
            finalcomment = request.args['finalcomment']
        except:
            finalcomment = ""

        results.write(finalcomment + '\n')
        results.close()

        return redirect(url_for('rus_finish'))
    return render_template('ru_comment.html')

@app.route('/rufinish')
def rus_finish():
    return render_template('ru_finish.html')



@app.route('/en')
def eng():
    if request.args:
        results = open("results.tsv", 'a', encoding='utf-8')
        sex = request.args['sex']
        age = request.args['age']
        land1 = request.args['land1']
        land2 = request.args['land2']
        language = request.args['language']
        languages = request.args['languages']
        try:
            email = request.args['email']
        except:
            email = ""
        try:
            langcomment = request.args['langcomment']
        except:
            langcomment = ""
        results.write(sex + '\t' + age + '\t' + land1 + '\t' + land2 + '\t' + language + '\t' + languages + '\t' + email + '\t' + langcomment + '\t')
        results.close()
        randomize_stimulus_in_html("en")
        return redirect(url_for("eng_instruction"))
    return render_template('en_private.html')

@app.route('/eninstruction')
def eng_instruction():
    return render_template('en_instruction.html')

@app.route('/enform')
def eng_form():
    if request.args:
        results = open("results.tsv", 'a', encoding='utf-8')
        try:
            T011 = request.args['T011']
        except:
            T011 = ""
        try:
            T012 = request.args['T012']
        except:
            T012 = ""
        try:
            T021 = request.args['T021']
        except:
            T021 = ""
        try:
            T022 = request.args['T022']
        except:
            T022 = ""
        try:
            T031 = request.args['T031']
        except:
            T031 = ""
        try:
            T032 = request.args['T032']
        except:
            T032 = ""
        try:
            T041 = request.args['T041']
        except:
            T041 = ""
        try:
            T042 = request.args['T042']
        except:
            T042 = ""
        try:
            T051 = request.args['T051']
        except:
            T051 = ""
        try:
            T052 = request.args['T052']
        except:
            T052 = ""
        try:
            T061 = request.args['T061']
        except:
            T061 = ""
        try:
            T062 = request.args['T062']
        except:
            T062 = ""
        try:
            T071 = request.args['T071']
        except:
            T071 = ""
        try:
            T072 = request.args['T072']
        except:
            T072 = ""
        try:
            T081 = request.args['T081']
        except:
            T081 = ""
        try:
            T082 = request.args['T082']
        except:
            T082 = ""
        try:
            T091 = request.args['T091']
        except:
            T091 = ""
        try:
            T092 = request.args['T092']
        except:
            T092 = ""
        try:
            T101 = request.args['T101']
        except:
            T101 = ""
        try:
            T102 = request.args['T102']
        except:
            T102 = ""
        try:
            T111 = request.args['T111']
        except:
            T111 = ""
        try:
            T112 = request.args['T112']
        except:
            T112 = ""
        try:
            T121 = request.args['T121']
        except:
            T121 = ""
        try:
            T122 = request.args['T122']
        except:
            T122 = ""
        try:
            T131 = request.args['T131']
        except:
            T131 = ""
        try:
            T132 = request.args['T132']
        except:
            T132 = ""
        try:
            T141 = request.args['T141']
        except:
            T141 = ""
        try:
            T142 = request.args['T142']
        except:
            T142 = ""
        try:
            T151 = request.args['T151']
        except:
            T151 = ""
        try:
            T152 = request.args['T152']
        except:
            T152 = ""
        try:
            T161 = request.args['T161']
        except:
            T161 = ""
        try:
            T162 = request.args['T162']
        except:
            T162 = ""

        results.write(T011 + '\t' + T012 + '\t' + T021 + '\t' + T022 + '\t' + T031 + '\t' + T032 + '\t' + T041 + '\t' + T042 + '\t' + T051 + '\t' + T052 + '\t' + T061 + '\t' + T062 + '\t' + T071 + '\t' + T072 + '\t' + T081 + '\t' + T082 + '\t' + T091 + '\t' + T092 + '\t' + T101 + '\t' + T102 + '\t' + T111 + '\t' + T112 + '\t' + T121 + '\t' + T122 + '\t' + T131 + '\t' + T132 + '\t' + T141 + '\t' + T142 + '\t' + T151 + '\t' + T152 + '\t' + T161 + '\t' + T162 + '\t')
        results.close()
        return redirect(url_for('eng_comment'))
    return render_template('en_pictures.html')

@app.route('/encomment')
def eng_comment():
    if request.args:
        results = open("results.tsv", 'a', encoding='utf-8')
        try:
            finalcomment = request.args['finalcomment']
        except:
            finalcomment = ""

        results.write(finalcomment + '\n')
        results.close()
        return redirect(url_for('eng_finish'))
    return render_template('en_comment.html')

@app.route('/enfinish')
def eng_finish():
    return render_template('en_finish.html')

if __name__ == '__main__':
    app.run()
