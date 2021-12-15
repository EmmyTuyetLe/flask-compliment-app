"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""
    return """<!doctype html><html>Hi! This is the home page.
    <a href="/hello">Hello</a>
     </html>"""


@app.route('/insult', methods=["GET"])
def say_something_mean():
    """Say hello and prompt for user's name."""
    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        # <form action="/diss" method="GET">
        #   What's your name? <input type="text" name="person">
        #   Choose your insult:
        #   <select name="insult">
        #   <option value="weird">weird</option>
        #   <option value="boring">boring</option>
        #   <option value="stinky">stinky</option>
        #   <option value="lazy">lazy</option>
        #   </select>
        #   <input type="submit" value="Submit">
        # </form>
      </body>
    </html>
    """


@app.route('/hello', methods=["GET"])
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet" method="GET">
          What's your name? <input type="text" name="person">
          Choose your compliment:
          <select name="compliment">
          <option value="funny">funny</option>
          <option value="smart">smart</option>
          <option value="kind">kind</option>
          <option value="creative">creative</option>
          </select>
         <input type="submit" value="Submit">
          </form>
          <form action="/diss" method="GET">
          What's your name? <input type="text" name="person">
          Choose your insult:
          <select name="insult">
          <option value="weird">weird</option>
          <option value="boring">boring</option>
          <option value="stinky">stinky</option>
          <option value="lazy">lazy</option>
          </select>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")
    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """
@app.route('/diss')
def insult_person():
    """insult the user"""
    player = request.args.get("person")
    insult = request.args.get("insult")
    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A insult</title>
      </head>
      <body>
        Hi, {player}! I think you're {insult}!
      </body>
    </html>
      """



if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
