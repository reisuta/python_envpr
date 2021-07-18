#コンストラクタ

class SampleClass:

    def __init__(self, msg, name=None):
        print('コンストラクタが呼ばれました。')
        self.msg = msg  #インスタンス変数
        self.name = name #インスタンス変数
        
    def __del__(self):
        print('デストラクタが呼ばれました。')
        print('name = {}'.format(self.name))


    def print_msg(self):
        print(self.msg)

    def print_name(self):
        print(self.name)


var_1 = SampleClass('hello','aaam')
var_1.print_msg()
var_1.print_name()
del var_1


