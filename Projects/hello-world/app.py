from dotenv import load_dotenv
import os
import requests
from chalice import Chalice
from datetime import datetime
from chalicelib.greeting_model import Greeting
from chalicelib.secrets import API_KEY

load_dotenv()
app = Chalice(app_name='hello-world')

# '/hello/james' -> {"hello": "james"}
@app.route('/hello/{name}')
def hello_name(name : str):
   return {'hello': name}

@app.route('/', methods=['GET'])
def get_index():
    return {'hello': 'world'}

@app.route('/{name}', methods=['GET'])
def get_name(name):
    greetings = Greeting()
    return {'message': greetings.get_greetings(name)}

@app.route('/today')
def today():
    now:str = datetime.now().strftime("%B %d, %Y")
    return {'today' : now}

# http://localhost:8000/echo | {"Code":"MethodNotAllowedError","Message":"Unsupported method: GET"}
# Jmeter로 리퀘스트 보내는게 좋을듯.
@app.route('/echo', methods=['GET'])
def get_echoback():
    request = app.current_request
    message = request.json_body
    return message

@app.route('/echo', methods=['POST'])
def post_echoback():
    request = app.current_request
    message = request.json_body
    return message

# gitignore된 secrete.py 혹은 .env를 사용해서 API_KEY 불러오기
# symbol : {btc, eth, lit}
@app.route('/price/{symbol}')
def get_price_with_symbol(symbol):
    symbol = symbol.upper()
    url = f"https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest?symbol={symbol}"
    # API_KEY = os.getenv('api_key')
    r = requests.get(url, headers={"X-CMC_PRO_API_KEY": API_KEY, "Content-Type":"application/json"})
    name = r.json()['data'][symbol][0]['name']
    price = r.json()['data'][symbol][0]['quote']['USD']['price']
    price = str('%.2f'%(float(price)))
    return f"{symbol}: The Price of {name} is {price}!"

# dynamoDB를 쓰고싶으면 AWS 콘솔에서 DB를 추가하자.
# @app.on_dynamodb_record(stream_arn="")
# def on_getting_stream_data(event):
#     for record in event:
#         print(record.new_image)
#         print(record.old_image)