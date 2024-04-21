# 相对路径文件名
file = ""
# 打开 文本文档 并指定 编码GBK 或 utf-8
with open(file,encoding='gbk') as f:
	book = f.read()
	# 寻找字符串并返回索引
	index = book.find("python")
	# 创建一个新的文本文件来保存指定内容
	# a.txt | b.txt |  c.txt......
	with open("a.txt","w") as b:
		b.write(book[:index])
		# 更新·文件名 || 删除了前段部分，保留后段
		newText = "S" + file
		with open(newText,"w") as i:
			i.write(book[index:])
			# FBI.close()








