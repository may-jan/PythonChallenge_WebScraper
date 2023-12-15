from flask import Flask, render_template, request, redirect, send_file
from extractors.wwr import extract_wwr_jobs
from extractors.indeed import extract_indeed_jobs
from file import save_to_file

app = Flask("JobScrapper")

db = {}

@app.route("/")
def home():
    return render_template("home.html", name='jan')

@app.route("/search")
def hello():
    keyword = request.args.get("keyword")
    if (keyword == None):
        return redirect("/")
    if(keyword in db):
        jobs = db[keyword]
    else:
        indeed = extract_indeed_jobs(keyword)
        wwr = extract_wwr_jobs(keyword)
        jobs = indeed+wwr
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)

@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if(keyword == None):
        return redirect("/")
    if(keyword not in db):
        return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword, db[keyword])
    return send_file(f"{keyword}.csv", as_attachment=True)


app.run("0.0.0.0", debug=True)

"""
HTML에서 파이썬 변수, 파이썬 문법 사용하기
1. {{ 변수이름 }} : 두개의 중괄호 안에 변수 → Flask가 변수를 값으로 변환해준다
2. {% 파이썬문법 %} :  HTML에서 파이썬 코드를 사용할 수 있다
3. {% endfor %} : 파이썬 코드 작성을 마쳤다는 표기
"""