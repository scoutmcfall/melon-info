"""Print out all the melons in our inventory."""

#track flesh color, rind color, and average weight
#make it easy to add additional information as needed
from melons import melons

def print_melon(melons):
    """Print each melon with corresponding attribute information."""
    #don't need have or have not because we can just print the nested dictionary
    #have_or_have_not = 'have'
    #for name, attributes in melon_dict:
        #if attributes[1] == False:
            #have_or_have_not = 'do not have'
    #print(f'{name}s {have_or_have_not} seeds and are ${attribute[0]:.2f}')
   
    for name, attributes in melons.items():
        print(name.upper()) #prints melon name in uppercase
        for attribute, value in attributes.items(): #accesses the nexted dictionary of attributes for each melon
            print(f'{attribute}: {value}') #prints a list of each value and what that value is
        print("----------------------------------")
    
