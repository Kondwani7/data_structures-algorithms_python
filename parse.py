import re


def parse1():
    for line in open("log.txt"):
        print(line.split("[")[1].split("]")[0])
print("parse1")
parse1()

def parse2():
    for line in open("log.txt", "r"):
        print(line.split()[3].strip("[]"))
print("parse 2")
parse2()


def parse5():
    for line in open("log.txt"):
        print(re.split("\[|\]", line)[1])

print("parse 5")
parse5()