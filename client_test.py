import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))
    
    

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))



  """ ------------ Add more unit tests ------------ """
  # ----- Test for the average price for a given quote ----
  def test_getDataPoint_averagePrice(self): 
    quote = {
      'stock': 'XYZ',
      'top_bid': {'price': '150.0', 'size': 50},
      'top_ask': {'price': '155.0', 'size': 30}
    }

    expected_result = ('XYZ', 150.0, 155.0, 152.5)
    self.assertEqual(getDataPoint(quote), expected_result)

# ----Test for the ratio of price_a and price_b----
  def test_getRatio(self): 
      ratio_test1 = getRatio(150.0, 100.0)
      ratio_test2 = getRatio(200.0, 100.0)
      ratio_test3 = getRatio(100.0, 100.0)
      ratio_test4 = getRatio(60.0, 100.0)
      ratio_test5 = getRatio(0.0, 100.0)

      expected_result1 = 1.5
      expected_result2 = 2.0
      expected_result3 = 1.0
      expected_result4 = 0.6
      expected_result5 = 0.0

      self.assertEqual(ratio_test1, expected_result1)
      self.assertEqual(ratio_test2, expected_result2)
      self.assertEqual(ratio_test3, expected_result3)
      self.assertEqual(ratio_test4, expected_result4)
      self.assertEqual(ratio_test5, expected_result5)
    




if __name__ == '__main__':
    unittest.main()
