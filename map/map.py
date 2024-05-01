old_list = ['1', '2', '3', '4', '5', '6', '7']

new_list = []
for item in old_list:
    new_list.append(int(item))

print (new_list)

print ('\nmap version ----------------')
old_list = ['1', '2', '3', '4', '5', '6', '7']
new_list = list(map(int, old_list))
print (new_list)

print ('\nгенератор version ----------------')
new_list = [int(x) for x in old_list]
print (new_list)

#map также работает и с функциями созданными пользователем
print ('\nmap с функциями созданными пользователем')
def miles_to_kilometers(num_miles):
    """ Converts miles to the kilometers """
    return num_miles * 1.6

mile_distances = [1.0, 6.5, 17.4, 2.4, 9]
kilometer_distances = list(map(miles_to_kilometers, mile_distances))
print (kilometer_distances)

#или с lambda
kilometer_distances = list(map(lambda x: x*1.6, mile_distances))
print (kilometer_distances)

#или с генераторами
kilometer_distances = [x*1.6 for x in mile_distances]
print (kilometer_distances)