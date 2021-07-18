#classの練習
class Car:
    """"車クラス"""
    country = 'Japan'
    year = 2019
    name = 'Prius'
    def print_name(self):
        print(self.name)

mycar = Car()#インスタンス化
print(mycar.year)
mycar.print_name()

list_a = ['apple','banana',Car()]
# second_list = list_a[2]()
# second_list.print_name()
list_a[2].print_name()
help(Car)