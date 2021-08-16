import unittest
import app


class MyTestCase(unittest.TestCase):
    def test_for_purchase(self):
        response = app.purchase_car("Tesla", "1000", "2021", "4")
        self.assertEqual(response[1], 200)
        self.assertIn('Purchase Succeed', response[0])

    def test_for_all(self):
        app.purchase_car("Toyota", "50", "1999", "2")
        app.purchase_car("Hunda", "50", "1995", "3")
        app.purchase_car("miniCooper", "100", "2021", "1")
        response = app.all_cars()
        inv = {'1': ["miniCooper", "100", "2021"], '2': ["Toyota", "50", "1999"], '3': ["Hunda", "50", "1995"]}
        self.assertEqual(response[0], inv)

    def test_for_sell(self):
        response = app.sell_car(1, 100)
        self.assertEqual(response[1], 200)
        self.assertIn('SOLD!', response[0])

    def test_results(self):
        app.sell_car(1, 250)
        app.sell_car(2, 250)
        response = app.results()
        self.assertEqual(response[0], "total Profit :-600")


if __name__ == '__main__':
    unittest.main()
