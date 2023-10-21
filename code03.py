# 实现一个命令行版本的学生管理系统
import os.path
import sys

students = []


def save():
    """
    用于存档
    """
    with open('record.txt','w',encoding='utf8') as f:
        for s in students:
            f.write(f"[{s['stuID']}]\t{s['stuName']}\t{s['stuGender']}\t{s['className']}\n")
        print(f'[存档成功],共存储了{len(students)}条记录！')


def load():
    """
    用于读档
    """
    if not os.path.exists('record.txt'):
        return

    #读档的时候要保证先把旧的数据给清理干净
    global students
    students = []
    with open('record.txt','r',encoding='utf8') as f:
        for line in f:
            line = line.strip()
            token = line.split('\t')
            if len(token) != 4:
                print(f'当前格式存在问题！line = {line}')
                continue
            student = {
                'stuID':token[0],
                'stuName':token[1],
                'stuGender':token[2],
                'className':token[3]
            }
            students.append(student)
        print(f'[读档成功],共读取了{len(students)} 条记录')



#打印一个菜单
def menu():
    print('1.新增学生')
    print('2.显示学生')
    print('3.查找学生')
    print('4.删除学生')
    print('0.退出程序')
    choice = input("请输入您的选择:")
    return choice


def insert():
    print('[新增学生]开始:')
    stuID = input('请输入学生的学号:')
    stuName = input('请输入学生的姓名:')
    stuGender = input('请输入学生性别:')
    if stuGender not in ('男','女'):
        print('输入错误，请重新输入')
        return
    className = input('请输入学生班级:')
    student = {
        'stuID':stuID,
        'stuName':stuName,
        'stuGender':stuGender,
        'className':className
    }
    global students
    students.append(student)
    save()
    print('[新增学生]结束！')


def show():
    #遍历全局变量这个列表，把每个学生的信息给打印出来、
    print('[显示学生]开始:')
    for s in students:
        print(f"[{s['stuID']}]\t{s['stuName']}\t{s['stuGender']}\t{s['className']}\t")

    print(f'[显示学生]结束！共显示了{len(students)}条数据')


def find():
    #根据学生姓名查找
    print('[查找学生]开始:')
    name = input('请输入要查找的学生姓名:')
    count = 0
    for s in students:
        if name == s['stuName']:
            print(f"[{s['stuID']}]\t{s['stuName']}\t{s['stuGender']}\t{s['className']}\t")
            count += 1

    print(f'[查找学生]结束！共找到了{count}个匹配的同学')


def delete():
    print('[删除学生]开始:')
    stuID = input('请输入要删除学生的学号:')
    for s in students:
        if stuID == s['stuID']:
            print(f"删除{s['stuName']}同学的信息")
            students.remove(s)
    save()
    print('[删除学生]结束！')


def main():
    """
    学生管理系统入口函数
    """
    print('--------------------------')
    print('     欢迎来到学生管理系统     ')
    print('--------------------------')
    load()
    while True:
        # 通过 menu 函数来打印出菜单项
        choice = menu()
        choice = int(choice)
        if choice == 1:
            #插入学生
            insert()
        elif choice == 2:
            #查看学生
            show()
        elif choice == 3:
            #查找学生
            find()
        elif choice == 4:
            #删除学生
            delete()
        elif choice == 0:
            #退出系统
            print('GoodBye')
            sys.exit(0)
        else:
            print('输入非法，请重新输入')


main()


