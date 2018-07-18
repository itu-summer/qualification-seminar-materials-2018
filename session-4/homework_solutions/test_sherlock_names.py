import sys
from cli_text_analysis import find_10_most_common_names

def test_find_10_most_common_names():
    #Returns a list of words with the first letter 
    #capitalised from a text 
    file = "his_last_bow.txt"
    with open(file) as f:
        text = f.read()
    output_dic = find_10_most_common_names(text)
    for name in output_dic.keys():
        assert type(name) == str
        assert len(name) >= 1
        assert output_dic[name] >= 20
    assert output_dic["Holmes"] > 100 and output_dic["Watson"] > 50