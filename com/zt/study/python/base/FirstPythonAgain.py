#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('hello python!')
# name = input()
# print(name)
# print('100+500=',100+500)

# print('1.跟进IM 报错')
# print('2.跟进IM模块和集成的测试')
# print('3.对国际版灰度环境进行测试，并跟进，暂未发现问题')
# print('4.修复IM分库分表引起的问题，空指针')
# print('4.IM后台权限管理')
# print('5.拼接语音')
# print('6.连接层增加时间戳校检')
# print('7.处理线上问题：a)微聊延迟（存在未读消息） b)手表不能定位（手表没有去拉取单推会话消息，已通知手表处理）c)app未收到加群推送（APP同步请求错乱，后续跟进） d)APP已退出，依然收到推送（上下线的bug引起的，已修复2.3.3）')
#
#
#
# print('1.跟进国际版三期测试与发布')
# print('2.跟进模块 集成测试')
# print('3.分析处理线上问题')

# name = input()
# print('你好 ',name)
# number = 16
# if(number > 20):
#     print('很大')
# else:
#     print('很小')

# sum = 0;
# # for num in [1,2,3,4,5,6,7,8,9]:
# for num in range(10):
#     sum += num
# print(sum)

# i = 0
# while i < 100:
#     print(i)
#     i += 1
#     if i == 66:
#         break

# scoreName = {'mike': 90, 'marry': 100}
# print(scoreName.get('mike1'))
#
# scoreName.pop("mike")
# print(scoreName)


#求和
def sumNumber(m):
    if m == None:
        return None
    if not isinstance(m,(int,float)):
        raise TypeError('bad operand type')
    if m <= 0:
        return 0
    sum = 0
    while m > 0:
        sum += m
        m -= 1
    return sum


print(sumNumber('he'))

print(hex(100))