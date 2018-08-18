from flask import Flask
from flask import url_for, render_template, request, redirect
import random
import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

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
    imgorder = ''

    for i in range(1,17):
        template = "N" + str(i) + "N"
        a = random.choice(numbers)
        numbers.remove(a)
        html = html.replace(template, a)
        if numbers != []:
            imgorder = imgorder + a + ','
        else:
            imgorder = imgorder + a

    write_txt(html, "templates/" + lang + "_pictures.html")

    results = open("results.tsv", 'a', encoding='utf-8')
    results.write(imgorder + '\t')
    results.close()

sex = None
age = None
land1 = None #country_native
land2 = None #country_actual
language = None #lang_native
languages = None #lang_others
email = None
langcomment= None
imgorder = None
T011= None
T012= None
T021= None
T022= None
T031= None
T032= None
T041= None
T042= None
T051= None
T052= None
T061= None
T062= None
T071= None
T072= None
T081= None
T082= None
T091= None
T092= None
T101= None
T102= None
T111= None
T112= None
T121= None
T122= None
T131= None
T132= None
T141= None
T142= None
T151= None
T152= None
T161= None
T162= None
finalcomment= None

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

        DATABASE_URL = os.environ['DATABASE_URL']
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = conn.cursor()
        cur.execute('''
        insert into results(
        sex,
        age,
        country_native,
        country_actual,
        lang_native,
        lang_other,
        email,
        lang_comment,
        given_order,
        fog01_name,
        fog01_comment,
        fog02_name,
        fog02_comment,
        fog03_name,
        fog03_comment,
        fog04_name,
        fog04_comment,
        fog05_name,
        fog05_comment,
        fog06_name,
        fog06_comment,
        fog07_name,
        fog07_comment,
        fog08_name,
        fog08_comment,
        fog09_name,
        fog09_comment,
        fog10_name,
        fog10_comment,
        fog11_name,
        fog11_comment,
        fog12_name,
        fog12_comment,
        fog13_name,
        fog13_comment,
        fog14_name,
        fog14_comment,
        fog15_name,
        fog15_comment,
        fog16_name,
        fog16_comment,
        final_comment
        ) values (
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s
        )
        ''', (sex,age,land1,land2,language,languages,email,langcomment,imgorder,T011,T012,T021,T022,T031,T032,T041,T042,T051,T052,T061,T062,T071,T072,T081,T082,T091,T092,T101,T102,T111,T112,T121,T122,T131,T132,T141,T142,T151,T152,T161,T162,finalcomment))
        conn.commit()
        cur.close()
        conn.close()

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

        DATABASE_URL = os.environ['DATABASE_URL']
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = conn.cursor()
        cur.execute('''
        insert into results(
        sex,
        age,
        country_native,
        country_actual,
        lang_native,
        lang_other,
        email,
        lang_comment,
        given_order,
        fog01_name,
        fog01_comment,
        fog02_name,
        fog02_comment,
        fog03_name,
        fog03_comment,
        fog04_name,
        fog04_comment,
        fog05_name,
        fog05_comment,
        fog06_name,
        fog06_comment,
        fog07_name,
        fog07_comment,
        fog08_name,
        fog08_comment,
        fog09_name,
        fog09_comment,
        fog10_name,
        fog10_comment,
        fog11_name,
        fog11_comment,
        fog12_name,
        fog12_comment,
        fog13_name,
        fog13_comment,
        fog14_name,
        fog14_comment,
        fog15_name,
        fog15_comment,
        fog16_name,
        fog16_comment,
        final_comment
        ) values (
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s
        )
        ''', (sex,age,land1,land2,language,languages,email,langcomment,imgorder,T011,T012,T021,T022,T031,T032,T041,T042,T051,T052,T061,T062,T071,T072,T081,T082,T091,T092,T101,T102,T111,T112,T121,T122,T131,T132,T141,T142,T151,T152,T161,T162,finalcomment))
        conn.commit()
        cur.close()
        conn.close()

        return redirect(url_for('eng_finish'))
    return render_template('en_comment.html')

@app.route('/enfinish')
def eng_finish():
    return render_template('en_finish.html')



# DATABASE_URL = os.environ['DATABASE_URL']
# conn = psycopg2.connect(DATABASE_URL, sslmode='require')
# cur = conn.cursor()
# cur.execute('''
# insert into results(
# sex,
# age,
# country_native,
# country_actual,
# lang_native,
# lang_other,
# email,
# lang_comment,
# given_order,
# fog01_name,
# fog01_comment,
# fog02_name,
# fog02_comment,
# fog03_name,
# fog03_comment,
# fog04_name,
# fog04_comment,
# fog05_name,
# fog05_comment,
# fog06_name,
# fog06_comment,
# fog07_name,
# fog07_comment,
# fog08_name,
# fog08_comment,
# fog09_name,
# fog09_comment,
# fog10_name,
# fog10_comment,
# fog11_name,
# fog11_comment,
# fog12_name,
# fog12_comment,
# fog13_name,
# fog13_comment,
# fog14_name,
# fog14_comment,
# fog15_name,
# fog15_comment,
# fog16_name,
# fog16_comment,
# final_comment
# ) values (
# {},
# {},
# {},
# {},
# {},
# {},
# {},
# {},
# {},
# {},
# {},
# {},
# {},
# {},
# {},
# {},
# {},
# {},
# {},
# {},
# {},
# {},
# {},
# {},
# {},
# {},
# {},
# {},
# {},
# {},
# {},
# {},
# {},
# {},
# {},
# {},
# {},
# {},
# {},
# {},
# {},
# {}
# )
# ''', #(sex,age,land1,land2,language,languages,email,langcomment,imgorder,T011,T012,T021,T022,T0#31,T032,T041,T042,T051,T052,T061,T062,T071,T072,T081,T082,T091,T092,T101,T102,T111,T112,T#121,T122,T131,T132,T141,T142,T151,T152,T161,T162,finalcomment))
# cur.commit()
# cur.close()
# conn.close()

# @app.route('/enfinish')
# @app.route('/rufinish')
# def finish():


if __name__ == '__main__':
    import os
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
