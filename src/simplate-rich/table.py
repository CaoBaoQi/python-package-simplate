from rich.console import Console
from rich.table import Table
from src.entity.Student import Student

cb = Student(name="CaoBei", age=18, email="cb@jz.edu.com", school="JinZhong University",
             link="http://www.jzxy.edu.cn/")
cbq = Student(name="CaoBaoQi", age=22, email="cbq@jz.edu.com", school="JinZhong University",
              link="http://www.jzxy.edu.cn/")
cbh = Student(name="CaoBingHui", age=18, email="cbh@jz.edu.com", school="JinZhong University",
              link="http://www.jzxy.edu.cn/")
rhf = Student(name="RenHuiFa", age=18, email="rgf@tykj.edu.com", school="TaiYuanKeJi University",
              link="http://www.tyust.edu.cn/")

info_list = [cb, cbq, cbh, rhf]

table = Table(title="Student INFO")

table.add_column("Name", justify="center", style="cyan", no_wrap=True)
table.add_column("Age", style="white")
table.add_column("Email", style="red")
table.add_column("School", justify="center", style="green")

for student in info_list:
    table.add_row(
        student.name,
        str(student.age),
        f"[link=mailto:{student.email}?subject=Summary&body=Content]{student.email}[/link]",
        f"[link={student.link}]{student.school}[/link]")

Console().print(table)
