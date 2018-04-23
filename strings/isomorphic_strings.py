def isIsomorphic(s, t):
    if len(s) == 0 or len(t) == 0 or len(s) != len(t):
        return False
    map = {}

    for i in range(len(s)): # We go over both together. That's how we maintain the pattern
        c1 = s[i]
        c2 = t[i]

        if c1 in map: # If already in map, the value of c1 should match
            if map[c1] != c2: # Not matching, so not isomorphic
                return False
        else:
            if c2 in map.values(): # Even if c1 not in map, we need to check if c2 is not already mapped by someone else.
                return False       # this is slow since we have loop at all values.
            map[c1] = c2 # Finally map them together.

    return True

"""
Faster:

def isIsomorphic(s, t):
    if len(s) == 0 or len(t) == 0 or len(s) != len(t):
        return False
    map = {}
    st = set()

    for i in range(len(s)): # We go over both together. That's how we maintain the pattern
        c1 = s[i]
        c2 = t[i]

        if c1 in map: # If already in map, the value of c1 should match
            if map[c1] != c2: # Not matching, so not isomorphic
                return False
        else: 
            if c2 in st: # Even if c1 not in map, we need to check if c2 is not already mapped by someone else. 
                return False       
            map[c1] = c2 # Finally map them together.
            st.add(c2) 
    
    return True
"""