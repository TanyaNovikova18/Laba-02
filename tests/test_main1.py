import sys
sys.path.append('C:/Users/tatan/PycharmProjects/cicd-test-main')
from src.lib import fibona
from src.lib import puz
from src.lib import calcul

def test_Fibo_cor_n():
    assert fibona(5) == [1, 1, 2, 3, 5]

# def test_Fibonacchi_cor_n_and_incor_result():
#     assert fibona(3) == [0, 1, 2, 3, 5, 8, 13, 21, 34]

# def test_Fibonacchi_on_incor_n():
#     assert fibona("10") == [1, 1, 2, 3, 5, 8, 13, 21, 34]

def test_Puzirec_on_correct_a():
    assert puz([5, 8, 1, 3, 9, 12, 0]) == [0, 1, 3, 5, 8, 9, 12]

# def test_Puzirec_on_correct_a_and_incorrect_result():
#     assert puz([5, 8, 1, 3, 9, 12, 0]) == [5, 8, 1, 3, 9, 12, 0]

# def test_Puzirec_on_incorrect_a1():
#     assert puz([5, '8', 1, 3, '9', 12, 0]) == [1, 1, 2, 3, 5, 8, 13, 21, 34]

# def test_Puzirec_on_incorrect_a2():
#     assert puz('World$Cool') == [1, 1, 2, 3, 5, 8, 13, 21, 34]

def test_Calc_on_correct_n():
    assert calcul(8, 2, '+') == 10

# def test_Calc__on_correct_n_and_incorrect_result():
#     assert calcul(8, 2, '+') == 9

# def test_Calc__on_incorrect_n():
#     assert calcul('9', '1', '+') == 10
