from concurrent.futures import ThreadPoolExecutor, wait, as_completed
import time


# concurrent.futures 线程池模块

def do(sec, name):
    time.sleep(sec)
    print('{}:{} sec done!'.format(name, sec))
    return sec


def doone(one):
    time.sleep(one)
    print('{} sec done!'.format(one))
    return one


executor = ThreadPoolExecutor(max_workers=2)

# task = executor.submit(do, 1, 't0')
# task1 = executor.submit(do, 1.5, 't1')
# task2 = executor.submit(do, 2, 't2')

# task2.cancel()  # 取消任务，task2没有被执行，pool中worker为2
#
# print(task.done())  # 判断是否完成
# print(task.result(timeout=None))  # 取返回值，阻塞主线程

args = [[1, 't0'], [1.5, 't1'], [2, 't2']]
all_task = [executor.submit(do, *arg) for arg in args]  # 出现错误不会被抛出
# wait(all_task, return_when='FIRST_COMPLETED')  # 等待，阻塞主线程
# print('main')
# for future in as_completed(all_task):  # 得到已经完成的task，as_completed 是生成器 yield
#     res = future.result()
#     print(res, 'success.')


# one_args = [0.5, 1, 1.5]
# for future in executor.map(do, one_args):
#     # 直接得到task返回值
#     print(future, 'success')
