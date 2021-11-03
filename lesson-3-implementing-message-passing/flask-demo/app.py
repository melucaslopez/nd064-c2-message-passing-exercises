from flask import Flask, request, jsonify

from .services import retrieve_item, create_item

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/demo/<path_demo>', methods=['POST'])
def demo(path_demo=None):
    # Showcase different ways in which data can be passed
    path_value = path_demo
    header_value = request.headers.get('header_demo', None)
    param_value = request.args.get('param_demo', None)
    body_value = request.data
    return {
        'result': {
            'path': path_value,
            'header': header_value,
            'param': param_value,
            'body': str(body_value),
        }
    }

@app.route('/api/items/<item_id>', methods=['GET', 'POST'])
def pets(item_id):
    if request.method == 'GET':
        return jsonify(retrieve_item(item_id))
    elif request.method == 'POST':
        request_body = request.json
        return jsonify(create_item(item_id, request_body))
    else:
        raise Exception('Unsupported HTTP request type.')


if __name__ == '__main__':
    app.run()
