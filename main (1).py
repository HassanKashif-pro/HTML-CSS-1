from flask import Flask

app = Flask(__name__)

myReflections = {}

myReflections["78"] = {"date": "2020-01-01", "reflection": "I'm gonna write a book about programming"}
myReflections["79"] = {"date": "2020-01-02", "reflection": "I'm gonna write a book about programming HO HO HO"} 


@app.route('/<pageNumber>')
def index(pageNumber):
  page = ""
  f = open("static/days.html","r")
  page = f.read()
  f.close()

  page = page.replace("{Day}", pageNumber)
  page = page.replace("{Date}", myReflections[pageNumber]["date"])
  page = page.replace("{reflection}", myReflections[pageNumber]["reflection"])

  return page

app.run(host='0.0.0.0', port=81)
