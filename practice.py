# t1 = ('Prime', 'Ix', 'Secundus', 'Caladan')
# t2 = (1, 2, 3, 4, 5, 6)
# print(t1[0])
# print(t2[2:4])
# print('Ix' in t1)
# print('Geidi' in t1)


# list2 = [ 'uli101', 'ops235', 'ops335', 'ops445', 'ops535', 'ops635' ]
# list2[0]= 'ica100'
# print(list2[0])
# print(list2)


import lab4b
list1 = [1,2,3,4,5]
list2 = [2,1,0,-1,-2]
print(lab4b.join_lists(list1,list2))
# Will output [0, 1, 2, 3, 4, 5, -2, -1]
print(lab4b.match_lists(list1,list2))                                                                                                                 
# Will output [1, 2]
print(lab4b.diff_lists(list1,list2))                                                                                                                  
# Will output [0, 3, 4, 5, -2, -1]