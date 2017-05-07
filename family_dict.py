# Define a dictionary that contains information about several members of your family. 
# Use the following example as a template.

# my_family = {
#     'sister': {
#         'name': 'Krista',
#         'age': 42
#     },
#     'mother': {
#         'name': 'Cathie',
#         'age': 70
#     }
# }
# Using a dictionary comprehension, produce output that looks like the following example.

# Krista is my sister and is 42 years old
# Helpful hint: To convert an integer into a string in Python, it's str(integer_value)

my_family = {
    'sister': {
        'name': 'Krista',
        'age': 42
    },
    'mother': {
        'name': 'Cathie',
        'age': 70
    },
    'brother': {
    	'name': 'Kevin',
    	'age': 900
    },
    'cousin': {
    	'name': 'Dragons',
    	'age': 6
    }
}

# Dictionaries, being a collection of key/value pairs, just works slightly differently. 
# You need to use the items() property on the original dictionary for the iteration.

# family = { 'mother': 'Margaret', 'father': 'Reginald', 'sister': 'Jenny'}
# my_family = {'my ' + k + ' is ' + v for (k,v) in family.items()}
# >>> my_family
# {'my father is Reginald', 'my sister is Jenny', 'my mother is Margaret'}

new_family = {str(v['name']) + ' is my ' + k +' and is ' + str(v['age']) for (k,v) in my_family.items()}


# better_dict = {str(v['name'])}

print(new_family)



       






