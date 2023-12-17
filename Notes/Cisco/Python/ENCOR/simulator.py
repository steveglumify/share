def print_facts(facts): 
    """Print two facts from facts dictionary 
       (Undefined multi-line string literal used to create
       a comment block)
    """  
 
    platform = facts.get('platform', 'unknown platform')  # Dictionary method get(keyname, value) returns the
    print('platform', platform)                           # value parameter if the keyname does not exist
 
    print ('os', facts['os'])
 
if __name__ == "__main__": 
 
    # Define basic facts about a device  

    facts = {'os': '7.2', 'fqdn': 'cisco.com', 'location': 'sjc', 'vlans_list': [1, 5, 10], 'neighbors': ['s2', 's3']}  
 
    # Call print_facts function  
    print_facts(facts)  
 
    # Extract neighbors from facts dictionary and assign to new variable  
    neighbors = facts['neighbors']  
 
    # Print each neighbor  
    for item in neighbors:  # <-- Colon.
        print(item)