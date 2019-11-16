import sys
from copy import deepcopy


def func(products, order_num, calibrate, result_list=[]):
    arr = result_list
    max_product = max(products)
    pros = deepcopy(products)
    floor_num = order_num // max_product
    floor_num -= calibrate

    modulo_num = order_num % max_product
    if modulo_num == 0:
        arr.append((floor_num, max_product))
    else:
        remain = order_num - (floor_num * max_product)
        products.pop(products.index(max_product))
        if len(products) == 0:
            return result_list
        if remain < sum(products):
            if [i for i in products if remain % i == 0 ]:
                arr.append((floor_num, max_product))
                return func(products, remain, 0, result_list)
            else:
                calibrate += 1
                return func(pros, order_num, calibrate, result_list)
        else:
            if (remain % max(products) == 1) and (len(products) == 1):
                calibrate += 1
                return func(pros, order_num, calibrate, result_list)
            else:
                arr.append((floor_num, max_product))
                return func(products, remain, 0, result_list)
    return result_list


def is_int_list(arr):
    list_check = [False for item in arr if isinstance(item, int) is False]
    if False in list_check:
        return False, arr
    else:
        return True, arr


def get_package(products, order_num):
    is_list_ok, products = is_int_list(products)
    if is_list_ok is False:
        return False, 'Array items can not be string'

    products_list_reduce = [i for i in products if i <= order_num]
    if not products_list_reduce:
        return False, 'Product list is empty'

    list_split = func(products_list_reduce, order_num, 0, [])
    if order_num == sum([i[0]*i[1] for i in list_split]):
        return True, list_split
    else:
        return False, 'Can not found'



def main():
    arg_list_products = sys.argv[1]
    arg_order_number = sys.argv[2]
    list_products = list(map(int, arg_list_products.strip('[]').split(',')))
    order_number = int(arg_order_number)
    is_ok, res = get_package(list_products, order_number)
    print (is_ok, res)

if __name__ == '__main__':
    main()
