# # with open('../images//'+'hi','wb') as f:
# #     f.write(b'123')
# import ctypes
# import inspect
# import re
#
# # pic = '/https://necaptcha.nosdn.127.net/79020c0a7bb94e8a8ac2846669f55837.jpg'
# # name = re.search(r'net/(.*)',pic).group(1)
# # print(name)
#
# # result = {'success': True, 'code': '0', 'message': 'success', 'data': {'result': '125,95', 'id': 'ZF0t0PhDRf68CuWd9vnJqg'}}
# # s=int(result['data']['result'].split(',')[0])
# #
# # print(s)
#
# # try:
# #     pass
# # except Exception as t:
# #     t.with_traceback()
#
# # str = 'https://blog.csdn.net/hhladminhhl/article/details/119154761/123'
# # result = re.search(r'details/(\d*)?',str).group(1)
# # print(type(result))
#
# # a = bytes(string='你',encoding='utf-8')
# # b = bytes(encoding='utf-8',string='你')
# # print(a is b)
#
# # a = bytes('你','utf-8')
# # b = bytes('你','utf-8')
# # print(a is b)
#
# # a = 1
# # b = 2
# # a,b = b,a
# # print(a,b)
# # import threading
# # import time
# #
# #
# # def run():
# #     time.sleep(5)
# #     print('完成')
# #
# # if __name__ == '__main__':
# #     t1 = threading.Thread(target=run)
# #     t1.start()
# #     t1.join(timeout=1)
# #     print(t1.isAlive(),)
# #     # try:
# #     #     t1.join(timeout=1)
# #     # except Exception as e:
# #     #     print("已超时")
# import threading
#
# from time import sleep
#
#
# def _async_raise(tid, exctype):
#     """raises the exception, performs cleanup if needed"""
#     tid = ctypes.c_long(tid)
#     if not inspect.isclass(exctype):
#         exctype = type(exctype)
#     res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
#     if res == 0:
#         raise ValueError("invalid thread id")
#     elif res != 1:
#         # """if it returns a number greater than one, you're in trouble,
#         # and you should call it again with exc=NULL to revert the effect"""
#         ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
#         raise SystemError("PyThreadState_SetAsyncExc failed")
#
#
# def stop_thread(thread):
#     _async_raise(thread.ident, SystemExit)
#
# class TimeoutException(Exception):
#     pass
#
# # class timeThread(threading.Thread):
# #     def timeout(self):
# #         if self.is_alive():
# #             raise TimeoutException()
# #     def run(self):
# #         while True:
# #             inputMessage()
#
#
#
# # if __name__ == '__main__':
# #    t=timeThread(target=inputMessage(),)
# #    t.start()
# #    print(t.join(timeout=1.5))
# #    try:
# #        t.timeout()
# #    except TimeoutException as e:
# #        stop_thread(t)
# #        print("输入超时")
#
# import pynput
# from time import sleep
#
# class Father(threading.Thread):
#
#     def __init__(self):
#         threading.Thread.__init__(self)
#         self.message = None
#
#     def inputMessage(self):
#         self.message = input("输入信息:\n")
#
#     def run(self):
#         t1 = threading.Thread(target=self.inputMessage)
#         t1.setDaemon(True)
#         t1.start()
#         sleep(2)
#
#
#         if self.message is None:
#             ctr = pynput.keyboard.Controller()
#             # with ctr.pressed(':'):
#             #     pass
#             with ctr.pressed(pynput.keyboard.Key.enter):
#                 pass
#             print("超时")
#         else:
#             print(self.message)
#
#         # try:
#         #     print(self.message)
#         # except Exception as e:
#         #     ctr = pynput.keyboard.Controller()
#         #     with ctr.pressed('a'):
#         #         pass
#         #     with ctr.pressed(pynput.keyboard.Key.enter):
#         #         pass
#         #     print(str(e))
#         print(input("输入下一条信息\n"))
#
#
#         # while True:
#         #     print("1",end='')
#         #     sleep(0.5)
#
# if __name__ == '__main__':
#     f = Father()
#     f.start()
#     f.join()
#
#
#
#

import pymysql
if __name__ == '__main__':
    dic = {}
    dic['user'] = 'root'  # The first four arguments is based on DB-API 2.0 recommendation.
    dic['password'] = "123456"
    dic['host']= '8.140.15.126'
    dic['database']= 'csdn'
    dic['port'] = 3306

    conn = pymysql.Connect(**dic)
    curser = conn.cursor()
    result = curser.execute("SELECT * FROM csdndata")
    for data in result:
        print(data)


















