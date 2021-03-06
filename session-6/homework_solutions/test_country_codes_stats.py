import country_codes_stats


def test_country_codes_data():
    codes = country_codes_stats.country_codes_data(
        'befkbhalderstatkode_small.xlsx', 3)
    expected_result = {5120, 5122, 5126, 5128, 5129, 5130, 5134, 5140, 5142,
                       5150, 5151, 5152, 5153, 5154, 5156, 5158, 5159, 5160,
                       5162, 5164, 5170, 5172, 5174, 5180, 5182, 5700, 5704,
                       5706, 5708, 5710, 5712, 5202, 5714, 5204, 5716, 5718,
                       5207, 5720, 5722, 5724, 5213, 5214, 5215, 5216, 5222,
                       5228, 5231, 5232, 5233, 5234, 5235, 5236, 5238, 5750,
                       5240, 5752, 5242, 5243, 5244, 5245, 5246, 5247, 5754,
                       5756, 5757, 5758, 5759, 5761, 5255, 5258, 5259, 5262,
                       5776, 5266, 5778, 5268, 5269, 5272, 5277, 5278, 5279,
                       5281, 5282, 5283, 5284, 5285, 5287, 5288, 5289, 5292,
                       5293, 5294, 5295, 5296, 5297, 5298, 5299, 5302, 5303,
                       5304, 5305, 5306, 5308, 5314, 5316, 5318, 5322, 5324,
                       5326, 5328, 5338, 5339, 5342, 5345, 5347, 5348, 5352,
                       5354, 5356, 5358, 5364, 5366, 5372, 5374, 5376, 5390,
                       5392, 5402, 5403, 5404, 5408, 5410, 5412, 5414, 5416,
                       5418, 5422, 5424, 5432, 5434, 5436, 5438, 5442, 5444,
                       5446, 5448, 5452, 5454, 5456, 5457, 5458, 5459, 5462,
                       5464, 5466, 5472, 5474, 5478, 5482, 5484, 5486, 5487,
                       5488, 5999, 5492, 5496, 5499, 5502, 5505, 5508, 5001,
                       5514, 5522, 5525, 5526, 5607, 5609, 5611, 5100, 5102,
                       5103, 5104, 5105, 5106, 5107, 5108, 5110, 5115}
    assert set(codes) == expected_result


def test_country_codes_data2():
    codes = country_codes_stats.country_codes_data('country_codes.xlsx', 0)
    expected_result = {0, 5120, 5122, 5124, 5126, 5128, 5129, 5130, 5134, 5140,
                       5142, 5150, 5151, 5152, 5153, 5154, 5156, 5158, 5159,
                       5160, 5162, 5164, 5170, 5172, 5174, 5176, 5180, 5182,
                       5700, 5704, 5706, 5708, 5710, 5199, 5712, 5202, 5714,
                       5204, 5716, 5718, 5207, 5720, 5722, 5724, 5213, 5214,
                       5215, 5216, 5222, 5228, 5230, 5231, 5232, 5233, 5234,
                       5235, 5236, 5238, 5750, 5240, 5752, 5242, 5243, 5244,
                       5245, 5246, 5247, 5248, 5754, 5756, 5623, 5757, 5758,
                       5759, 5255, 5761, 5258, 5259, 5260, 5262, 5776, 5266,
                       5778, 5268, 5269, 5779, 5272, 5273, 5274, 5275, 5276,
                       5277, 5278, 5279, 5281, 5282, 5283, 5284, 5285, 5287,
                       5288, 5289, 5800, 5292, 5293, 5294, 5295, 5296, 5297,
                       5298, 5299, 5302, 5303, 5304, 5305, 5306, 5308, 5309,
                       5310, 5311, 5314, 5316, 5318, 5319, 5322, 5324, 5326,
                       5328, 5338, 5339, 5342, 5344, 5345, 5347, 5348, 5352,
                       5354, 5356, 5358, 5364, 5366, 5372, 5374, 5376, 5901,
                       5390, 5902, 5392, 5395, 5397, 5398, 5402, 5403, 5404,
                       5406, 5408, 5410, 5412, 5414, 5416, 5418, 5422, 5424,
                       5432, 5434, 5435, 5436, 5438, 5442, 5444, 5446, 5448,
                       5452, 5454, 5456, 5457, 5458, 5459, 5462, 5464, 5466,
                       5468, 5471, 5472, 5474, 5478, 5482, 5484, 5486, 5487,
                       5488, 5999, 5492, 5496, 5499, 5502, 5505, 5508, 5001,
                       5514, 5522, 5525, 5526, 5534, 5599, 5607, 5609, 5611,
                       5100, 5101, 5102, 5103, 5104, 5105, 5106, 5107, 5108,
                       5109, 5110, 5621, 5625, 5114, 5115}
    assert set(codes) == expected_result


def test_translate_code_to_text():
    country = country_codes_stats.translate_code_to_text(5126)
    assert country == 'Belgien'


def test_translate_code_to_text2():
    country = country_codes_stats.translate_code_to_text(5100)
    assert country == 'Danmark'


def test_translate_code_to_text3():
    country = country_codes_stats.translate_code_to_text(5120)
    assert country == 'Sverige'


def test_translate_many_codes_to_text():
    expected_result = ['Uoplyst (1)', 'Uoplyst (2)', 'Danmark', 'Grønland',
                       'Udlandet uoplyst', 'Statsløs', 'Finland',
                       'Island, ligeret dansk', 'Island', 'Liechtenstein']

    argument = [0, 5001, 5100, 5101, 5102, 5103, 5104, 5105, 5106, 5107]
    result = country_codes_stats.translate_many_codes_to_text(argument)
    assert expected_result == result


def test_filter_for_not_living_in_cph():
    cph_person_codes = country_codes_stats.country_codes_data(
        'befkbhalderstatkode_small.xlsx', 3)
    complete_codes = country_codes_stats.country_codes_data(
        'country_codes.xlsx', 0)
    cph_person_codes = set(cph_person_codes)
    complete_codes = set(complete_codes)

    result = country_codes_stats.filter_for_not_living_in_cph(complete_codes,
                                                              cph_person_codes)

    expected_result = {0, 5248, 5124, 5260, 5901, 5902, 5779, 5395, 5397, 5398,
                       5273, 5274, 5275, 5276, 5406, 5534, 5800, 5176, 5435,
                       5309, 5310, 5311, 5319, 5199, 5468, 5471, 5344, 5599,
                       5101, 5230, 5109, 5621, 5623, 5625, 5114}
    assert expected_result == result or sorted(list(expected_result)) == sorted(result)
