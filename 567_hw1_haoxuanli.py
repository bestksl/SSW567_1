# @Author: HaoxuanLi  
# @Date 1/25/2019
# CWID: 10434197
from unittest import TestCase
import math


class Hw1:

    @staticmethod
    def classify_triangle(a, b, c):
        l = sorted([a, b, c])
        a, b, c = l[0], l[1], l[2]
        result = []
        if a + b > c:
            if a ** 2 + b ** 2 == c ** 2:
                result.append("right")
            if a == b or b == c:
                result.append("isosceles")
                if a == b and b == c:
                    result.append("equilateral")
            if len(result) == 0:
                result.append("scalene")
        else:
            return -1
        return result

    def get_input(self, a, b, c):
        input_list = input("please input 3 numbers with ',':").split(',')
        a, b, c = input_list[0], input_list[1], input_list[2]


class MyTest(TestCase):

    def test_classify_triangle(self):
        self.assertEqual(-1, Hw1.classify_triangle(1, 3, 2))
        self.assertEqual(["right"], Hw1.classify_triangle(3, 4, 5))
        self.assertEqual(["isosceles"], Hw1.classify_triangle(1, 5, 5))
        self.assertEqual(["scalene"], Hw1.classify_triangle(2, 6, 5))
        self.assertEqual(["isosceles", "equilateral"], Hw1.classify_triangle(3, 3, 3))
