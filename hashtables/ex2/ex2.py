#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)

# source is key -->  current location
#destination is value --> next point in trip
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    #need to iterate through t
    for t in tickets:
        #can use the method from hashtables to insert
        #need to add the length of the hashtable, key/value params source/destination
        hash_table_insert(hashtable, t.source, t.destination)
        
    #set current location to None 
    current_position = 'NONE'
    # find the ith location in the route by iterating
    for i in range(length):
        #retrieve method stored in route variable, needs hashtable and key = current position
        route[i] = hash_table_retrieve(hashtable, current_position)
        #set current location in ticket chain to route[index]
        current_position = route[i]
        
        
    #tests weren't passing, needed to slice off the last None     
    return route[:-1]
        