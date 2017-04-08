# class Stack:
	
# 	def __init__(self,name=[]):
# 		self.name = name
# 	def push(self):
# 		self.name.append(self.name)


		


# def main():
# 	ram = Stack('Ram')
# 	ram.push()
# 	am = Stack('shyam')
# 	am.push()

# main()


class Stack:
	def __init__(self):
		self.__list =[]
	def push(self,item):
		self.__list.append(item)
	def pop(self):
		return self.__list.pop()

