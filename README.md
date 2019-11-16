1. Install [Python 3](https://www.python.org/) for your OS.

2. cd to workdir and activate python

3. Please take a look on tests.py, I've prepare some test cases

4. Please find main function at `find_products_packages.py`
- sample input:
    + is_ok, result = get_package([3, 5, 9], 13)
- sample output:
    + True, [(0, 9), (2, 5), (1, 3)]
    + with 3 items in list
        - (0, 9): 
            + 0 x 9 @ $16.99
        - (2, 5):
            + 2 x 5 @ $9.95
        - (1, 3):
            + 1 x 3 @ $5.95


5. To define another packs and order_number, run command `python find_products_packages.py <packs: type List> <order_number: Int>`
=> for example: `python find_products_packages.py [2,3,8,14] 20`
