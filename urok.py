def test(meter):
    meter += 10
    return meter

meter = 100
meter = test(meter)
print(meter)