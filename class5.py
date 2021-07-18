#特殊メソッド
class Human:
    def __init__(self,name,age,phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number
    
    def __str__(self):
        return self.name + ',' + str(self.age) + ',' + self.phone_number

    def __eq__(self,other):
        return (self.age == other.age)

    def __hash__(self):
        return hash(self.name + self.phone_number)

    def __bool__(self):
        return True if self.age >= 20 else False


man = Human('Taro',34,'080339205430')
man2 = Human('tea',14,'080339205430')
man3 = Human('jiro',34,'9283999238')
# print(man)
# print(man == man2)

set_men = {man,man2,man3}
for x in set_men:
    print(x)

if man:
    print('man true')
if man2:
    print('man2 true')