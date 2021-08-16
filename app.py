from flask import Flask


app = Flask(__name__)

inventory = dict()
# {id : [brand, price, year]}
sold_cars = dict()
totalProfit = [0]
@app.route('/')
def hello_world():
    return 'Hello!'


@app.route('/api/purchase/<string:brand>/<int:price>/<int:year>/<int:id>', endpoint='/api/purchase_car')
def purchase_car(brand, price, year, id):
    inventory[id] = [brand, price, year]
    totalProfit[0] -= int(price)
    return "Purchase Succeed", 200


@app.route('/api/sell_car/<int:car_id>/<int:price>', endpoint='/api/sell_car')
def sell_car(car_id, price):
    inventory.pop(car_id, None)
    sold_cars[car_id] = price
    totalProfit[0] += int(price)
    return "SOLD!", 200


@app.route('/api/all_cars')
def all_cars():
    return inventory, 200


@app.route('/api/results')
def results():
    return "total Profit :" + str(totalProfit[0]), 200


if __name__ == '__main__':
    app.run()
