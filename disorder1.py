def get_number():
    "Returns a float number"
    number = float(input("Enter a float number: "))
    return number

while True:
    try:
        print(get_number())
    except ValueError:
        print("You Entered a wrong values")   

# 可以使用 try...except... 模块来处理任何异常，try...无异常，后面省略；try...出现异常，直接跳转except...，在其中挑选匹配异常，无传回上一级 try... 中，最终找不到匹配异常，终止程序运行，显示匹配信息。
