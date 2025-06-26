# # def binary_search(arr,target):
# # 	l,r =0, len(arr)-1
# #     arr.sort()  
# # 	while l<r:
# # 		m =(l+r)// 2

# # 		if arr[m] == target:
# # 			return True
# # 		if 

# # arr = [5,6,7,8,9,10,1,2,3,4]
# # target = 2

# # if binary_search(arr,target):
# # 	print(f"{target} is present in the array {arr}")
# # else:
# # 	print(f"{target} is not present in the array {arr}")

# # @route
# # def url():
# # app.route(/camp___):

# # def route(func):
# # 	print("route func")
	
# import asyncio
# async def task1():
# 	print("task1 started")
# 	await asyncio.sleep(2)
# 	print("task1 complete")

# async def task2():
# 	print("task2 start")
# 	await asyncio.sleep(1)
# 	print ("task2 complete")

# async def main():
# 	await asyncio.gather(task1(),task2())

# asyncio.run(main())


# employee taple

# name , salary 

# 3nd highest


# select max(salary) from employee 
# where salaray<(select max(salary) from employee)


# sorted arr
# rotated right side

# [5,6,7,8,1,2,3,4]
# [ 4 5 6 7 8 1 2 3]

# def binary_search(arr,target):
# 	l,r =0, len(arr)-1

# 	while l<r:
# 		m =(l+r) //2

# 		if arr[m] == target:
# 			return True
# 		elif arr[m]< target:
# 			l = m+1
# 		else:
# 			r = m-1
# 	return False

# def binary_search(arr,target):
# 	l,r =0, len(arr)-1
#     arr.sort()  
# 	while l<r:
# 		m =(l+r)// 2

# 		if arr[m] == target:
# 			return True
# 		if arr

# arr = [5,6,7,8,9,10,1,2,3,4]
# target = 2

# if binary_search(arr,target):
# 	print(f"{target} is present in the array {arr}")
# else:
# 	print(f"{target} is not present in the array {arr}")

# @route
# def url():
# app.route(/camp___):

# def route(func):
# 	print(route func)