# import threading
# import random
#
# def fill_list(lst):
#     for _ in range(10):
#         lst.append(random.randint(1, 100))
#
# def calculate_sum(lst):
#     return sum(lst)
#
# def calculate_average(lst):
#     return sum(lst) / len(lst)
#
# def main():
#
#     my_list = []
#     fill_thread = threading.Thread(target=fill_list, args=(my_list,))
#     fill_thread.start()
#     fill_thread.join()
#     sum_thread = threading.Thread(target=calculate_sum, args=(my_list,))
#     average_thread = threading.Thread(target=calculate_average, args=(my_list,))
#     sum_thread.start()
#     average_thread.start()
#     sum_thread.join()
#     average_thread.join()
#     sum_result = sum_thread.result
#     average_result = average_thread.result
#     print("Отриманий список:", my_list)
#     print("Сума елементів у списку:", sum_result)
#     print("Середнє арифметичне у списку:", average_result)
#
# if __name__ == "__main__":
#     main()


# import threading
#
# def print_info(info):
#     print(info)
#
# def sort_array(arr):
#     print(sorted(arr))
#
# t1 = threading.Thread(target=print_info, args=("Thread1",))
# t2 = threading.Thread(target=print_info, args=([2, 1, 3, 5, 4],))
#
# t1.start()
# t2.start()

# t1.join()
# t2.join()

#
# import threading
# def print_cude(num):
#     #можна додати for i in range(5):
#     print("Cude:{}".format(num * num * num))
#
# def print_square(num):
#         print("Square:{}".format(num * num * num))
#
# t1 = threading.Thread(target=print_square, args=(10,))
# t2 = threading.Thread(target=print_cude, args=(10,))
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
# print("Dome!")

# import threading
#
# shared_resource = 0
# lock = threading.Lock()
#
# def increment():
#     global shared_resource
#     for _ in range(10000):
#         lock.acquire()
#         lock.release()
#
# def decrement():
#     global shared_resource
#     for _ in range(10000):
#         lock.release()
#
# t1 = threading.Thread(target=increment)
# t2 = threading.Thread(target=decrement)
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
import threading


global_number = 0
lock = threading.Lock()


def append():
    for _ in range(100):
        global global_list
        lock.acquire()
        global_list.append(1)
        lock.release()

def remove():
    for _ in range(100):
        global global_list
        global_list.pop()
        lock.release()

t1 = threading.Thread(target=append, args=())
t2 = threading.Thread(target=remove, args=())

t1.start()
t2.start()

t1.join()
t2.join()
print(f"Final result{global_list}")