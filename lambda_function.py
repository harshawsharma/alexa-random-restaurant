import logging

from flask import Flask
from flask_ask import Ask, question
from api import search


app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

def lambda_handler(event, _context):
    return ask.run_aws_lambda(event)

@ask.launch
def launch():
    speech_text = 'Welcome to the Alexa Skills Kit, you can say. Pick a place for me in New York'
    return question(speech_text).reprompt(speech_text).simple_card('HelloWorld', speech_text)

@ask.intent('RestaurantByCityIntent')
def get_restuarant_by_city(USCitySlot):
    return search (USCitySlot)


if __name__ == '__main__':
    app.run(debug=True)