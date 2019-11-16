import unittest
from find_products_packages import get_package


class TestPacMethods(unittest.TestCase):
    def test_string_in_list(self):
        is_ok, mess = get_package(['a'], 3)
        self.assertEqual((False, 'Array items can not be string'), (is_ok, mess))



    def test_case_can_not_split(self):
        is_ok, mess = get_package([2], 3)
        self.assertEqual((False, 'Can not found'), (is_ok, mess))

    def test_case_product_list_is_empty(self):
        is_ok, mess = get_package([], 1)
        self.assertEqual((False, 'Product list is empty'), (is_ok, mess))

    def test_case_find_correct_package(self):
        is_ok, result = get_package([2, 5, 8], 67)
        self.assertEqual((True, [(7, 8), (1, 5), (3, 2)]), (is_ok, result))

    # Three expected test case
    '''
    10 VS5
    14 MB11
    13 CF
    10 VS5 $17.98
        2 x 5 $8.99
    14 MB11 $54.8
        1 x 8 $24.95
        3 x 2 $9.95
    13 CF $25.85
        2 x 5 $9.95
        1 x 3 $5.95
    '''
    def test_case_find_10VS5(self):
        is_ok, result = get_package([3, 5], 10)
        self.assertEqual((True, [(2, 5)]), (is_ok, result))

    def test_case_find_14MB115(self):
        is_ok, result = get_package([2, 5, 8], 14)
        self.assertEqual((True, [(1, 8), (0, 5), (3, 2)]), (is_ok, result))

    def test_case_find_13CF(self):
        is_ok, result = get_package([3, 5, 9], 13)
        self.assertEqual((True, [(0, 9), (2, 5), (1, 3)]), (is_ok, result))

if __name__ == '__main__':
    unittest.main()