import Lab2.bmi as bmi

def test_bmi_normal_weight():
    result = bmi.calculate_bmi(1.78, 70)
    assert(result == 0)

def test_bmi_over_weight():
    result = bmi.calculate_bmi(1.50, 70)
    assert(result == 1)

def test_bmi_under_weight():
    result = bmi.calculate_bmi(1.90, 50)
    assert (result == -1)
