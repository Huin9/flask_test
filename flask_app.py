# Let's go
from flask import Flask, render_template, request
from vsearch import search4letters

# flask instance
app = Flask(__name__)

# app.route()
@app.route('/search4', methods = ['POST'])
def do_search() -> 'str' :
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = '당신의 문장에서 사용된 문자는 다음과 같습니다?'
    results = str(search4letters(phrase,letters))

    return render_template('results.html',
                            the_title = title,
                            the_phrase = phrase,
                            the_letters = letters,
                            the_results = results,)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                            the_title = "어서오십시오! 당신의 문장에 쓰인 글자를 찾아드립니다?")


if __name__ == '__main__' :
    app.run(debug = True)
