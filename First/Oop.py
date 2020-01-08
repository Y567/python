class StudentMem(object):
    def __init__(self, name, sex, age):
        self.__name = name
        self.__sex = sex
        self.__age = age

    def getName(self):
        return self.__name

    def getSex(self):
        return self.__sex

    def getAge(self):
        return self.__age

    def setName(self, name):
        if not isinstance(name, str):
            print('请输入一个字符串')
            return
        self.__name = name

    def setSex(self, sex):
        if sex != 'man' and sex != 'woman':
            print('请输入man或者woman')
            return
        self.__sex = sex

    def setAge(self, age):
        if not isinstance(age, int):
            print('请输入一个数字')
            return
        self.__age = age


# Student类继承StudentMem类
class Student(StudentMem):
    def __init__(self, name, sex, age, grade, number, count):
        super(Student, self).__init__(name, sex, age)
        self.__grade = grade
        self.__number = number
        self.__count = count

    def getGrade(self):
        return self.__grade

    def getNumber(self):
        return self.__number

    def getCount(self):
        return self.__count

    def setGrade(self, grade):
        if not isinstance(grade, int):
            print('请输入一个数字')
            return
        self.__grade = grade

    def setNumber(self, number):
        if not isinstance(number, str):
            print('请输入一个字符串')
            return
        self.__number = number

    def setCount(self, count):
        if not isinstance(count, int):
            print('请输入一个数字')
            return
        self.__count = count

    def printInfo(self):
        print('学生名字：%s' % (self.getName()))
        print('学生性别：%s' % (self.getSex()))
        print('学生年龄：%d' % (self.getAge()))
        print('学生班级：%d' % (self.getGrade()))
        print('学生学号：%s' % (self.getNumber()))
        print('学生数量：%d' % (self.getCount()))


# Teacher类继承StudentMem类
class Teacher(StudentMem):
    def __init__(self, name, sex, age, office, number, count):
        super(Teacher, self).__init__(name, sex, age)
        self.__office = office
        self.__number = number
        self.__count = count

    def getOffice(self):
        return self.__office

    def getNumber(self):
        return self.__number

    def getCount(self):
        return self.__count

    def setOffice(self, office):
        if not isinstance(office, int):
            print('请输入一个数字')
            return
        self.__office = office

    def setNumber(self, number):
        if not isinstance(number, str):
            print('请输入一个字符串')
            return
        self.__number = number

    def setCount(self, count):
        if not isinstance(count, int):
            print('请输入一个数字')
            return
        self.__count = count

    def printInfo(self):
        print('教师名字：%s' % (self.getName()))
        print('教师性别：%s' % (self.getSex()))
        print('教师年龄：%d' % (self.getAge()))
        print('教师科室：%d' % (self.getOffice()))
        print('教师工号：%s' % (self.getNumber()))
        print('教师数量：%d' % (self.getCount()))


# 主方法
if __name__ == '__main__':
    student = Student('阿狗', 'man', 21, 1703, '17408070814', 1)
    teacher = Teacher('阿强', 'man', 21, 1703, '17408070813', 1)
    print('学生信息：')
    student.printInfo()
    print('========================')
    print('教师信息：')
    teacher.printInfo()

    print('========================')
    # 测试set方法
    student.setAge(24)
    teacher.setName('会长')
    print('修改后的学生信息：')
    student.printInfo()
    print('========================')
    print('修改后的教师信息：')
    teacher.printInfo()
