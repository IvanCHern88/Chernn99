"""
2. Write a script to print out a set containing all the colours from color_list_1 which are not present in color_list_2.
        Test Data :
        color_list_1 = set(["White", "Black", "Red"])
        color_list_2 = set(["Red", "Green"])
        Expected Output :
        {'Black', 'White'}
"""
        
        
print("Введіть список1 через кому без відступу:")
inp1=input().split(',')
print("Введіть список2 через кому без відступу:")
inp2=input().split(',')
color_list_1=set(inp1)
color_list_2=set(inp2)
x=color_list_1.difference(color_list_2)
print("Результат:",x,sep=" ")        
