# # num=256
# # sum=0
# # while num!=0:
# #     sum+=num%10
# #     num=num//10
# # print(sum)
# # res={v:k }
# newarr=sorted([9,421,99,0,15,100],reverse=True)
# def restore_num(arr):
#     size=len(arr)-1
#     num=0
#     i=0
#     while size!=-1:
#         num+=arr[i]*10**size
#         size-=1
#         i+=1
#     return num
# def find_max_num(arr):
#     final_arr=[]
#     for i in arr:
#       temp_arr=[]
#       num=i
#       if num ==0:
#          temp_arr.append(0)
#       while num>0:
#         elem=num%10
#         num=num//10
#         temp_arr.insert(0,elem)
#       final_arr.append(temp_arr)
#     final_arr=sorted(final_arr,reverse=True)
#     returned_arr=[]
#     for i in range(len(final_arr)):
#         for j in range(len(final_arr[i])):
#           returned_arr.append(final_arr[i][j])
#     num=restore_num(returned_arr)
#     return num
# print(find_max_num(newarr))
s=[1,4,5]
print(s[0])