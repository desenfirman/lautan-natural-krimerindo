import main


def test_below_12():
    test_variable = {
        0: 'nol',
        1: 'satu',
        2: 'dua',
        3: 'tiga',
        4: 'empat',
        5: 'lima',
        6: 'enam',
        7: 'tujuh',
        8: 'delapan',
        9: 'sembilan',
        10: 'sepuluh',
        11: 'sebelas'
    }
    for test, result in test_variable.items():
        assert main.get_literal_number_less_than_m(test) == result


def test_teen():
    test_variable = {
        12: 'dua belas',
        13: 'tiga belas',
        14: 'empat belas',
        15: 'lima belas',
        16: 'enam belas',
        17: 'tujuh belas',
        18: 'delapan belas',
        19: 'sembilan belas'
    }
    for test, result in test_variable.items():
        assert main.get_literal_number_less_than_m(test) == result


def test_tens():
    test_variable = {
        20: 'dua puluh',
        21: 'dua puluh satu',
        55: 'lima puluh lima',
        63: 'enam puluh tiga',
        99: 'sembilan puluh sembilan',
    }
    for test, result in test_variable.items():
        assert main.get_literal_number_less_than_m(test) == result


def test_hundred():
    test_variable = {
        100: 'seratus',
        105: 'seratus lima',
        111: 'seratus sebelas',
        155: 'seratus lima puluh lima',
        163: 'seratus enam puluh tiga',
        199: 'seratus sembilan puluh sembilan',
        200: 'dua ratus',
        211: 'dua ratus sebelas',
        255: 'dua ratus lima puluh lima',
        263: 'dua ratus enam puluh tiga',
        999: 'sembilan ratus sembilan puluh sembilan',
    }
    for test, result in test_variable.items():
        assert main.get_literal_number_less_than_m(test) == result


def test_thousands():
    test_variable = {
        1000: 'seribu',
        1001: 'seribu satu',
        1011: 'seribu sebelas',
        1019: 'seribu sembilan belas',
        1155: 'seribu seratus lima puluh lima',
        1199: 'seribu seratus sembilan puluh sembilan',
        2000: 'dua ribu',
        2001: 'dua ribu satu',
        2011: 'dua ribu sebelas',
        2200: 'dua ribu dua ratus',
        2211: 'dua ribu dua ratus sebelas',
        2255: 'dua ribu dua ratus lima puluh lima',
        9999: 'sembilan ribu sembilan ratus sembilan puluh sembilan',
        10111: 'sepuluh ribu seratus sebelas',
        11111: 'sebelas ribu seratus sebelas',
        12345: 'dua belas ribu tiga ratus empat puluh lima',
        54321: 'lima puluh empat ribu tiga ratus dua puluh satu',
        99999: 'sembilan puluh sembilan ribu sembilan ratus sembilan puluh sembilan',
        100001: 'seratus ribu satu',
        100011: 'seratus ribu sebelas',
        100111: 'seratus ribu seratus sebelas',
        101111: 'seratus satu ribu seratus sebelas',
        111111: 'seratus sebelas ribu seratus sebelas',
        200111: 'dua ratus ribu seratus sebelas',
        201111: 'dua ratus satu ribu seratus sebelas',
        211111: 'dua ratus sebelas ribu seratus sebelas',
        123456: 'seratus dua puluh tiga ribu empat ratus lima puluh enam',
        654321: 'enam ratus lima puluh empat ribu tiga ratus dua puluh satu',
        999999: 'sembilan ratus sembilan puluh sembilan ribu sembilan ratus sembilan puluh sembilan'
    }
    for test, result in test_variable.items():
        assert main.get_literal_number_less_than_m(test) == result


def test_millions():
    test_variable = {
        1000000: 'satu juta',
        1000001: 'satu juta satu',
        1000011: 'satu juta sebelas',
        1000111: 'satu juta seratus sebelas',
        1001111: 'satu juta seribu seratus sebelas',
        1011111: 'satu juta sebelas ribu seratus sebelas',
        1234567: 'satu juta dua ratus tiga puluh empat ribu lima ratus enam puluh tujuh',
        9999999: 'sembilan juta sembilan ratus sembilan puluh sembilan ribu sembilan ratus sembilan puluh sembilan',
        10000001: 'sepuluh juta',
        10000001: 'sepuluh juta satu',
        11000001: 'sebelas juta satu',
        22000001: 'dua puluh dua juta satu',
        99999999: 'sembilan puluh sembilan juta sembilan ratus sembilan puluh sembilan ribu sembilan ratus sembilan puluh sembilan',
        100000001: 'seratus juta',
        100000001: 'seratus juta satu',
        110000011: 'seratus sepuluh juta sebelas',
        110001000: 'seratus sepuluh juta seribu',
        111111111: 'seratus sebelas juta seratus sebelas ribu seratus sebelas',
        123456789: 'seratus dua puluh tiga juta empat ratus lima puluh enam ribu tujuh ratus delapan puluh sembilan',
        999999999: 'sembilan ratus sembilan puluh sembilan juta sembilan ratus sembilan puluh sembilan ribu sembilan ratus sembilan puluh sembilan'
    }
    for test, result in test_variable.items():
        assert main.get_literal_number_less_than_m(test) == result

    def test_more_than_millions():
        test_variable = {
            1000000000: 'Number should be less than 999.999.999',
        }
    for test, result in test_variable.items():
        assert main.get_literal_number_less_than_m(test) == result
