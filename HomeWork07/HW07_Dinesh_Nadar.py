from collections import defaultdict, Counter


def anagram_1st(str1, str2):
    """returns True if both the string is anagram of each other. """
    return(sorted(str1.lower()) == sorted(str2.lower()))
# wrong function name

def anagrams_dd(str1, str2):
    """finds out if the both the strings are anagram of each other"""
    dd = defaultdict(int)
    for c in str1.lower():
        if(c in dd):
            dd[c] += 1
        else:
            dd[c] = 1
    for c in str2.lower():
        if(c in dd):
            dd[c] -= 1
        else:
            return False
    return(all(x == 0 for x in dd.values()))
#program if "all" is used if else is not required

def anagrams_cntr(str1, str2):
    """finds out if the both the strings are anagram of each other"""
    return(Counter(str1.lower()) == Counter(str2.lower()))



def covers_alphabet(sentence):
    """finds out if the sentence passed to the function has all the 26 alphabets or not"""
    sen = sentence.lower()
    c2 = Counter("abcdefghijklmnopqrstuvwxyz")
    for c in sen:
        if(c in c2):
            c2[c] -= 1
    return(all(x <= 0 for x in c2.values()))
# using sets


def book_index(words):
    """Returns the book index after arranging it in a proper way"""
    
    dd = defaultdict(list)
    d1 = list()
    aa = sorted(words)
    for k, v in aa:
        dd[k].append(v)
    ab = dd.items()
    for j in ab:
        d1.append(list(j))
    return d1
# Using Sets
    # indx=defaultdict(set)
    
    # for word,page in words:
    #     indx[word].add(page)