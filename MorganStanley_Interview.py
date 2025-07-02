# # # # func(a1-list of int,a2- target)
# # # # int in list = target


# # # def sumsadd(lst,t):
# # #     seen = set()
# # #     for num in lst:
# # #         diff = t - num
# # #         if diff in seen:
# # #             return diff,num
# # #         seen.add(num)
# # #     return -1
# # # lst=[1,1,5]
# # # t=2
# # # print(sumsadd(lst,t))

# # # 1.multiple pairs as ans if exists
# # # 2.limit into just 2 int, can be any(1,2,3)
# # # 3.repeat any elements in list any no. of times

# # lst=[1,2,3] 
# # t=5

# # def pairs_combinations(lst,t):
# #     lst.sort()
# #     result = []
    
# #     def backtrack(start,curr,curr_sum):
# #         if curr_sum == t:
# #             result.append(list(curr))
# #             return
        
# #         if curr_sum > t:
# #             return
        
# #         for i in range(start,len(lst)):
# #             num = lst[i]
# #             curr.append(num)
            
# #             backtrack(i,curr,curr_sum + num)
# #             curr.pop()
            
# #     backtrack(0,[],0)
# #     return result
        
# # print(pairs_combinations(lst,t))

# emp 
# id name

# salary 
# id salary

# name of emp 3rd lowest salary 

# select e.name
# from emp e 
# join salary s on e.id =s.id
# order by s.salary asc 
# limit 1 offset 2 

# FETCH DOC IMG
# EXC 1ST DOC machine
# create a file named gaurav

# docker image ls 

# docker ps 

# docker exec -1234 sh -c 'echo"gaurav'> path


