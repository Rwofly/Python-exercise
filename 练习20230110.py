#文件和异常
#从文件中读取数据
file_path='D:/python练习.txt'#将绝对文件路径赋值给变量file_path,用'/'而不用反斜杠表示为了与转义字符区分开
with open(file_path) as file_object:
#open（）函数接受文件路径，打开文件。关键字with在不需要访问文件后将其关闭，防止另使用close（）函数造成错误
    contents=file_object.read()#使用方法read读取文件全部内容，并赋值给变量contents
print(contents)


print("逐行读取文件内容")
with open(file_path) as file_object:
    for line in file_object:
        print(line)

print("创建一个包含文件各行内容的列表")
file_path='D:/python练习.txt'
with open(file_path) as file_object:
    lines=file_object.readlines()#readlines()从文件读取每一行，并将其储存在列表中。接下来该列表被赋值给lines
for line in lines:
    print(line.rstrip())#rstrip()方法是为了消除文件中的换行符
pi_string=''
for line in lines:
    pi_string+=line.rstrip()
print(pi_string)#输出内容
print(len(pi_string))#计算长度
print("变量pi_string指向的字符串包含原来位于每行左边的空格，为删除这些空格，可用strip()而非rstrip()")
pi_string=''
for line in lines:
    pi_string+=line.strip()
print(pi_string)#输出内容
print(len(pi_string))#计算长度
#写入文件

filename='D:/写入文件.txt'
with open(filename,'w') as file_object:
#open中第一个实参表示文件路径，第二个表示2以写入模式打开文件。如果要写入的文件不存在open将自动创建它
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")#写入多行，函数write()不会再写入文本中添加换行符
with open(filename) as file_object:
    contents=file_object.read()
print(contents)
#处理FileNotFoundError异常
fileename='D:不存在的文件.txt'#python无法读取不存在的文件，因此它会引发一个异常
try:
    with open(fileename) as f:
        contents=f.read()
except FileNotFoundError:
    print(f"Sorry,the file {filename} does not exit.")