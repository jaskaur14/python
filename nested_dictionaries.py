x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#changing number(index 0) in second x index (index 1)
x[1][0] = 15
# first [] indicates index to be changed, second [] indicates changed number
print(x)

#changing last name (key 0) of index 1
students [0]['last_name'] = "Bryant"
# second [] is the key to be changed
print (students)

#changing index 0 of key 1
sports_directory ['soccer'][0] = "Andres"
# changing key within key basically
print (sports_directory['soccer'])

#changing index 1
z[0]['y'] = 30
print (z)


students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

#printing dictionaries
def iterate_dictionary(some_list):
    for i in range ( 0, len(some_list)): 
        # all the values in the length of some_list
        output = ""
        for key, val in some_list[i].items():
            # .items iterates through keys and values
            output += f" {key} - {val} ,"
            #  can also use output += "[key] - [val]" ?
        print (output)
iterate_dictionary(students)

#printing specific values from dictionaries
def iterate_dictionary2(key_name, some_list):
    for i in range ( 0, len(some_list)):
        for key, val in some_list[i].items():
            if key == key_name:
                print (val)
iterate_dictionary2('first_name' , students)
iterate_dictionary2('last_name' , students)
# inside paratheses is how we find specific values within keys

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

#printing values from list
def printInfo (some_dict):
    for key, val in some_dict.items():
        print("")
        print (f"{len(val)} {key.upper()}")
        # prints the locations?
        for i in range(0, len(val)):
            print (val[i])
            # prints the instructors?
printInfo(dojo)
