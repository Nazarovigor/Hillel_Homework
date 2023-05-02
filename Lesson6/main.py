import Homework1
import Homework2
import Homework3
import Homework4
import Homework5
import Homework6

if __name__ == '__main__':

    number = Homework1.enter_number()
    print(Homework1.is_num_rec(number))

    side = Homework2.enter_number()
    print(Homework2.square(side))

    num = Homework3.enter_number()
    print(Homework3.is_prime(num))

    my_list = Homework4.enter_list()
    print(Homework4.change_list(my_list))

    lst = Homework4.enter_list()
    print(Homework5.to_dict(lst))

    start, end = Homework6.enter_numbers()
    print(Homework6.sum_range(start, end))
