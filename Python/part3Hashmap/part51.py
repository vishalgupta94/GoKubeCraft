"""
Custom Class and Hashing
 
how we can make our own custom classes keys and dictinoaries/.

how Python inserts a key/value item in a dicionary
    hash(key) -> mod dictionary size(allocated)  --> start index in hash table
it cannot keep incresing dictionary size every time we insert the key so expalin
              -> generate probe sequence (sequence of vlaid indices)
              -> iterate over prob sequence -> index
                -> is the slot at that index empty
                  yes   -> store the new item there(hash,key,value)
                  no    ->  hash collision

                        -> continue iteration to look for an empty slot

        # continue iteration to look for an empty slot


more hash collioss-> more ineffiencet          

What about th resvers how do we find empty in dictinoary.
                
"""