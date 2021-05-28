from pymongo import MongoClient, errors
from flask import Flask, jsonify, abort, request

DOMAIN = '0.0.0.0'
PORT = 27017

app = Flask(__name__)


@app.route('/', methods=['GET'])
def i_am_alive():
    return 'I am alive! <a href="mongo">Try MongoDB</a>'


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return '404'


@app.errorhandler(500)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return f'500 {str(e)}'


@app.route('/mongo', methods=['GET'])
def mongo():
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
        return f'error: {str(err)}'


if __name__ == '__main__':
    # app.run(debug=True, port=8080)
    # app.run(debug=True)
    # load_dotenv()
    # teleg = TelegramMy(os.getenv('TELEGRAMTOKEN'), os.getenv('CHATID'))

    app.run(host='0.0.0.0', port=8080)
