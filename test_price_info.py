import price_info

def test_total_cost_shopping():
    assert(price_info.total_cost_shopping() == 46.75)

def test_cost_of_fruits():
    result = price_info.cost_of_fruits('pineapple', 10)
    assert(result == 27)
