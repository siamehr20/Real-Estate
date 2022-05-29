# from cgitb import reset
# from mimetypes import init
# from unittest import result
import hashlib as hash
#
# sia = {
#     'name' :'siavash', 'last':'RAD','age':'21'
# }
#
# class person:
#
#     def __init__(self,name,last,age) :
#         self.name = name
#         self.last = last
#         self.age = age
#
# class student(person):
#     def __init__(self,**kw):
#         return super().__init__(**kw)
#
#
#         return result
# class Result(person):
#     def __init__(self,**kw):
#         super().__init__(**kw)
#
#     def prop():
#         name = 'Siavash'
#         last = 'Rad'
#         age = '21'
#
#         result = {
#             'name':name ,
#             'last': last
#             , 'age' : age
#         }
#
#         return result
#
#
#
# data = Result.prop()
# st = student(**data)
#
# print(st.age)


class pers:
    def __init__(self, name, age, uid):
        self.name = name
        self.age = age
        self.uid = uid


class proff(pers):
    def __init__(self, courseid, **kwargs):
        self.courseid = courseid


class Stu(pers):
    def __init__(self, term, **kwargs):
        self.term = term
        super().__init__(**kwargs)


kwargsstu1 = Stu(name='siavash', age=21, uid=9811415038, term=6)

result = {
    'floor ': 1, 'balcony': True
    , 'elevator': True
}
result2 = {
    'room ': 24, 'park': True
    , 'addss': 'taka st'
}
result.update(result2)

