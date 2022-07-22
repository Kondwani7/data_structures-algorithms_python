#time complexity O(1)
#key-value store
#e.g find a repeated character
#hash table can be used a to find a kth element in a array
# k will act as a key
# the hash table can convert a key into an index - hash function
# the aim is will creating an index, is to minimize collsions and
#  reduce time complextiy for querying or updating
# collisions: two records stored in the same location
# techniques to resolve collsion: direct chaining (linked list)
# open addressing (linear search , two hash functions)
# load factor - (No of elements in hash table) hash table size
# where the keys change dynamic hashing may be idea
# hash tables are not ideal for: multidimension data, prefix searching
# data without unique keys, problems with dyanmaic data, data ordering
# bloom filter - used to check an eleemnt is present in a set with memory and time efficiency