from flask import Flask, jsonify, request

from services import retrieve_orders, create_order

app = Flask(__name__)

@app.route('/api/orders/computers', methods=['GET'])
def get_computer_orders():
    return retrieve_orders()

@app.route('/api/orders/computers', methods=['POST'])
def create_computer_order():
    return create_order(request.json)

@app.route('/health')
def health():
    return jsonify({'response': 'Hello World!'})

if __name__ == '__main__':
    app.run()
