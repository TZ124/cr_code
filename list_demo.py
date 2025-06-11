# 创建一个包含不同类型元素的列表
my_list = [1, "你好", 3.14, True, ["嵌套列表", 2]]

# 输出整个列表
print("完整列表：", my_list)

# 输出列表中的特定元素
print("\n列表中的第一个元素：", my_list[0])
print("列表中的第二个元素：", my_list[1])

# 使用循环遍历列表
print("\n使用循环遍历列表：")
for item in my_list:
    print(f"- {item}")

# 列表的一些基本操作
print("\n列表长度：", len(my_list))
print("列表是否包含'你好'：", "你好" in my_list) 