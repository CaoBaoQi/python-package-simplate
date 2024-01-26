class Student:
    """
    学生信息类

    Attributes:
        name (str): 姓名
        age (int): 年龄
        email (str): 电子邮件地址
        school (str): 学校名称
        link (str): 学校官网


    Methods:
        __init__(self, name, age, email, school, link): 初始化 Student 类的新实例。
    """

    def __init__(self, name, age, email, school, link):
        """
        初始化Student类的一个新实例。

        Parameters:
            name (str): 姓名
            age (int): 年龄
            email (str): 电子邮件地址
            school (str): 学校名称
            link (str): 学校官网
        """
        self.name = name
        self.age = age
        self.email = email
        self.school = school
        self.link = link
