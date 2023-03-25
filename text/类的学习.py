class Student:
    native_place='bolan,此乃类的属性'
    def __init__(self,name,age):
        self.age=age
        self.name=name
    def info(self):
        print(self.age,self.name)
    def eat(self):
        print('学生们在吃饭','此乃实例方法')
    @classmethod
    def cs(cls):
        print('此乃类方法')
        pass
    @staticmethod
    def st(self):
        print('此乃静态方法')
class Teacher(Student):
    def __init__(self, name, age,year):
        super().__init__(name, age)
        self.year=year
    def info(self):
        super().info()
        print(self.year)
t1=Teacher('王五',34,10)
t1.info()