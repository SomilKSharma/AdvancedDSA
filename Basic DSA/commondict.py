'''Given two dictionaries, write a program for creating a dictionary in such a way that it consists of all the keys that are common in both dictionaries. '''
def commonKey(dict1, dict2):
    '''dict1, dict2 are the two dictionaries
    print the required dictionary'''
     
    dict3 = {}
    
    #YOUR CODE GOES HERE
    for key,value in dict1.items():
        if key in dict2:
            dict3[key]=dict1[key]+dict2[key]
    
    print(dict3)
