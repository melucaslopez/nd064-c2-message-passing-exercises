from flask import Flask, jsonify, request

from .services import retrieve_orders, create_order

app = Flask(__name__)


@app.route('/health')
def health():
    return jsonify({'response': 'Hello World!'})

# URL Path
# POST <BASE_URL>/api/orders/computers
@app.route('new_request/api/orders/computers', methods=['POST'])
def createOrder():
    request_body = request.json
    return jsonify(create_order(request_body))

# URL Path
# GET <BASE_URL>/api/orders/computers

@app.route('order_numbers/api/orders/computers', methods=['GET'])
def getOrder():
    return jsonify(retrieve_orders())

class Status(Enum):
    Queued = 'Queued'
    Processing = 'Processing'
    Completed = 'Completed'
    Failed = 'Failed'

if __name__ == '__main__':
    app.run()