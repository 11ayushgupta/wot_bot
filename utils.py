import os
import requests
import json

from pymongo import MongoClient
db_client=MongoClient("<your mongo db database url>")
db=db_client.get_database("wot_bot")
records=db.news_bot
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "bot_secret.json"

url="https://dog.ceo/api/breeds/image/random"
import dialogflow_v2 as dialogflow
dialogflow_session_client = dialogflow.SessionsClient()
PROJECT_ID = "wot-bot-bhajlk"


from gnewsclient import gnewsclient
client= gnewsclient.NewsClient(max_results=1)

from forex_python.converter import CurrencyRates
c = CurrencyRates()

def get_news(parameters):
    print(parameters)
    records.insert_one(parameters)
    client.topic=parameters.get('news_type')
    client.language=parameters.get('language')
    client.location=parameters.get('geo-country')
    return client.get_news()


def detect_intent_from_text(text, session_id, language_code='en'):
    session = dialogflow_session_client.session_path(PROJECT_ID, session_id)
    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = dialogflow_session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result


def fetch_reply(msg, session_id):
    response= detect_intent_from_text(msg, session_id)

    if response.intent.display_name == 'get_news':
        print("SHOWING NEWS ON PHONE")
        news=get_news(dict(response.parameters))
        print(news)
        news_str='Here is your top news'
        for row in news:
            news_str+="\n\n{}\n\n{}\n\n".format(row['title'],row['link'])
        return '',news_str

    elif response.intent.display_name == 'get_rates':
        print("Showing conversion on phone")
        conv_from=(dict(response.parameters))["currency-name"]
        return '',str(c.get_rate(conv_from, 'INR'))

    elif response.intent.display_name == 'show_dog':
        print("Sending a dog image on phone")
        response=requests.get(url)
        link=json.loads(response.text)
        return("dog",link["message"])

    

    else:
        return ("Ayush "+response.fulfillment_text)
