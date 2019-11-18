"""
运算符重载 - 自定义分数类

Version: 0.1
Author: 骆昊
Date: 2018-03-12
"""

from math import gcd


class Rational(object):

    def __init__(self, num, den=1):
        if den == 0:
            raise ValueError('分母不能为0')
        self._num = num
        self._den = den
        self.normalize()

    def simplify(self):
        x = abs(self._num)
        y = abs(self._den)
        #最大公约数
        factor = gcd(x, y)
        if factor > 1:
            #取整除 - 返回商的整数部分（向下取整）
            self._num //= factor
            self._den //= factor
        return self

    def normalize(self):
        if self._den < 0:
            self._den = -self._den
            self._num = -self._num
        return self

    def __add__(self, other):
        new_num = self._num * other._den + other._num * self._den
        new_den = self._den * other._den
        return Rational(new_num, new_den).simplify().normalize()

    def __sub__(self, other):
        new_num = self._num * other._den - other._num * self._den
        new_den = self._den * other._den
        return Rational(new_num, new_den).simplify().normalize()

    def __mul__(self, other):
        new_num = self._num * other._num
        new_den = self._den * other._den
        return Rational(new_num, new_den).simplify().normalize()

    def __truediv__(self, other):
        new_num = self._num * other._den
        new_den = self._den * other._num
        return Rational(new_num, new_den).simplify().normalize()

    def __str__(self):
        if self._num == 0:
            return '0'
        elif self._den == 1:
            return str(self._num)
        else:
            return '(%d/%d)' % (self._num, self._den)


if __name__ == '__main__':
    r1 = Rational(2, 3)
    print(r1)
    r2 = Rational(6, -8)
    print(r2)
    print(r2.simplify())
    '''
    方法名                  运算符和表达式      说明
    __add__(self,rhs)        self + rhs        加法
    __sub__(self,rhs)        self - rhs         减法
    __mul__(self,rhs)        self * rhs         乘法
    __truediv__(self,rhs)   self / rhs          除法
    __floordiv__(self,rhs)  self //rhs          地板除
    __mod__(self,rhs)       self % rhs       取模(求余)
    __pow__(self,rhs)       self **rhs         幂运算
    执行运算符，就会调用对应的方法
    '''
    print('%s + %s = %s' % (r1, r2, r1 + r2))
    print('%s - %s = %s' % (r1, r2, r1 - r2))
    print('%s * %s = %s' % (r1, r2, r1 * r2))
    print('%s / %s = %s' % (r1, r2, r1 / r2))
