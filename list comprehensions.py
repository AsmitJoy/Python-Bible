even_numbers = [x for x in range(1,101) if  x%2 ==0]
print("There are {} even numbers and they are {} ".format(len(even_numbers),even_numbers))

odd_numbers = [x for x in range(1,101) if  x%2 !=0]
print("There are {} odd numbers and they are {} ".format(len(odd_numbers),odd_numbers))


words = ["the","quick","brown","Jump","dog","lazy"]
ans = [[w.upper(),w.lower(),len(w)] for w in words]

print(ans)
