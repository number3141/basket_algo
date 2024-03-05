# """Модуль с дескрипторами для Match
# Не особо нужен, запросы покроет DTO
# """
# from abc import ABC, abstractmethod
#
#
# class Validate(ABC):
#     def __set_name__(self, owner, name):
#         self.name_ser = name
#
#     def __set__(self, instance, value):
#         v = self.validate(value)
#         instance.__dict__[self.name_ser] = v
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name_ser]
#
#     @abstractmethod
#     def validate(self, val): ...
#
#
# class DateValidate(Validate):
#     def validate(self, val):
#         if isinstance(val, float | str):
#             return val
#         else:
#             raise ValueError('Введите дату в формате dd.mm')
#
#
# class TextValidate(Validate):
#     def validate(self, val):
#         if isinstance(val, str):
#             return val
#
#         raise ValueError('Имя команды должно быть в виде строки!')