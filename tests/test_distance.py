from mlproject.computedist import haversine

def test_haversine():
    assert haversine(48.865070, 2.380009, 48.235070, 2.393409) == 70.00789153218594
