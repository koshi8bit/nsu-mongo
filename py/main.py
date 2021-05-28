from pymongo import MongoClient, errors
from flask import Flask, jsonify, abort, request

DOMAIN = '0.0.0.0'
PORT = 27017

app = Flask(__name__)


@app.route('/', methods=['GET'])
def i_am_alive():
    return "I am alive!"


@app.route('/process', methods=['GET'])
def process():
    try:
        client = MongoClient(
            host=[DOMAIN + ":" + str(PORT)],
            serverSelectionTimeoutMS=3000,
            username="root",
            password="1234",
        )

        print("version:", client.server_info()["version"])

        database_names = client.list_database_names()
        print("OK:", database_names)
        return "ok"

    except errors.ServerSelectionTimeoutError as err:
        print("pymongo ERROR:", err)
        return "error"

if __name__ == '__main__':
    # app.run(debug=True, port=8080)
    # app.run(debug=True)
    # load_dotenv()
    # teleg = TelegramMy(os.getenv('TELEGRAMTOKEN'), os.getenv('CHATID'))

    app.run(host='0.0.0.0', port=8080)
