#словари
my_dict={'Sveta':32,'Vova':33,'Zlata':9, 'Alice':5}
print('Dict: ',my_dict)
print('Existing value: ',my_dict.get('Sveta'))

my_dict.update({'Molly':11,
                'Morty':5})
print('Modified dictionary: ',my_dict)

d=my_dict.pop('Vova')
print('Deleted value: ',d)
print('Modified dictionary: ',my_dict)

#множества
my_set={1,2,3,8,6,1,2,'арбуз'}
print('Set: ',my_set)

my_set.add(88)
my_set.add(33)
print('Modified set: ',my_set)

my_set.remove(2)
print('Modified set: ',my_set)