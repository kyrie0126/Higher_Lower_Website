from random import randint
from flask import Flask
app = Flask(__name__)

# Generate random number from 0-9
random_num = randint(0,9)

# Create homepage
@app.route('/')
def home():
    return "<h1>Guess a number between 0-9!</h1>" \
           "<p>To guess 5, modify the url:</p>" \
           "<p>http://123.4.5.6:7890/<b>5</b></p>"

# Provide high/low/correct response to different paths
@app.route('/<value>')
def guess(value):
    if int(value) == random_num:
        return "<img src='https://media.tenor.com/ynST0DWtFqgAAAAM/pointing-that-is-correct.gif', width='500'>"
    elif int(value) > random_num:
        return "<img src='https://media.tenor.com/km6qbyrUioQAAAAM/jimmy-mcmillan-too-damn-high.gif', width='500'>"
    elif int(value) < random_num:
        return "<img src='https://media.tenor.com/HV9KIjODgK0AAAAS/tenor.gif', width='500'>"

# Run server
if __name__ =="__main__":
    app.run(debug=True)
