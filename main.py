from flask import Flask

app = Flask(__name__,static_url_path="/static")


@app.route('/')
def index():
    return 'Hello from Flask!'

@app.route('/home')
def home():
  page = """<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>replit</title>
  <link href="style.css" rel="stylesheet" type="text/css" />
</head>

<body>
  
  <script src="script.js"></script>

  <img src= "static/images/picard.jpg" width="200px" />
  <h1>Doggu</h1>
  <p>"The Best Guy-Dog Ever"</p>
  <h2>Socials</h2>
  <ul>
  <li>Instagrm(<a href="https://www.instagram.com/_.haxxann/#">_.Haxxann</a>)</li>
  <li>Twitter(<a href="https://twitter.com/Haxxankashif">HassanKashif</a>)</li>
  </ul>
  <script src="https://replit.com/public/js/replit-badge.js" theme="blue" defer></script> 
  
</body>

</html>"""

  
  return page

@app.route('/portfolio') # Creates the path to the home page
def portfolio(): # Subroutine to create the home page
  page = """<html>

<head>
  <title>My Portfolio</title>
</head>

<body>
  <h1>Haxxan's Portfolio</h1> 
  <h2>My First Project:</h2>
  <p>This is my first project. I'm learning how to code.</p>
  <img src="static/images/picard.jpg" width="50%" height="80%">
    <a href="https://replit.com/@HassanKashif2/Day72100Days">Details</a>
  
</body>
"""
  # Three quotes - I'm going to write or paste my HTML code here. The HTML gets assigned to the page variable
  return page # returns the contents of the page variable


app.run(host='0.0.0.0', port=81)
