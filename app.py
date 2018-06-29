
from flask import Flask, render_template, request
from vsearch import search4letters

app = Flask(__name__)

def log_requests(req, res):
  with open("weblog.txt", "a") as log:
    print(req.form, req.remote_addr, req.user_agent, res, sep="|", end="|",  file=log)

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    print(request.form)
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    log_requests(request,results)
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results,)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')
@app.route('/viewlog')
def viewlog_page() -> 'html':
    with open("weblog.txt") as log:
      data =  str(log.readlines()) 
      return data 


if __name__ == '__main__':
    app.run(debug=True, port=8080)



