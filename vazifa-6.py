list1 = [1, 2, 3]
                     
list2 = [11, 22, 33]
                            
def qandaydir(l1, l2):
                                     
    list3 = []
                                       
    min_len = min(len(l1), len(l2))
                          
    for i in range(min_len):
                                     
        list3.append(l1[i])
                              
        list3.append(l2[i])
                                 
    if len(l1) > min_len:
        list3.extend(l1[min_len:])
                                         
    if len(l2) > min_len:
        list3.extend(l2[min_len:])
                                 
    return list3
                          
list3 = qandaydir(list1, list2)
                                      
print("Yangi list:", list3)
                                         