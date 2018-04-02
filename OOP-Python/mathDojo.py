# PART I
# class MathDojo(object):
#     def __init__(self):
#         self.sum = 0

#     def number_add(self, *arg):
#         self.sum += sum(num)
#         return self

#     def substract(self, *arg):
#         self.sum -= sum(num)
#         return self

#     def result(self):
#         return self.sum

# md = MathDojo()
# print md.number_add(2).number_add(2, 5).substract(3, 2).result()


# PART II
class MathDojo(object):
    def __init__(self):
        self.summary = 0

    def number_add(self, *args):
        for arg in args:
            if isinstance(arg, int):
                self.summary += arg
            if isinstance(arg, float):
                self.summary += arg
            if isinstance(arg, tuple):
                self.summary += sum(arg)
            if isinstance(arg, list):
                self.summary += sum(arg)
        return self
            
    def subtract(self, *args):
        for arg in args:
            if isinstance(arg, int):
                self.summary -= arg
            if isinstance(arg, float):
                self.summary -= arg
            if isinstance(arg, tuple):
                self.summary -= sum(arg)
            if isinstance(arg, list):
                self.summary -= sum(arg)
        return self

md = MathDojo()
print md.number_add([1], 3,4).number_add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).summary
