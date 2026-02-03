from abc import ABC, abstractmethod

class ABCclass(ABC):
    def print(self, x):
        print(f"Passed value: {x}")

    @abstractmethod
    def task(self):
        print("We're all inside ABCclass task")

class test_class(ABCclass):
    def task(self):
       print("We're all inside test_class task") 

test_obj = test_class()
test_obj.task
test_obj.print(100)