def chkstr(s):
    """Checking if the string is valid"""
    if type(s) == str:
        return s
    else:
        raise ValueError('Not a valid string')

def chkList(a):
    if not a:
      raise ValueError("List is empty")
    else:
        return a;
    
def list_copy(l):
    chkList(l)
    result = list()
    result=[items for items in l]
    return(result)


def list_intersect(l1, l2):
       
    chkList(l1)
    chkList(l2)
    result = list()
    result=[item for item in l1 if(item in l2)]
    return(result)
    


def list_difference(l1, l2):
    
    chkList(l1)
    chkList(l2)
    result = list()
    result=[item for item in l1 if(item not in l2)]            
    return(result)


def remove_vowels(string):
    chkstr(string)
    result = list()
    result=[item for item in string if(item not in 'AaEeIiOoUu')]
    resultStr="".join(result)
    return(resultStr)




def check_pwd(password):
    chkstr(password)
    result = list()
    result=["L" if(item.islower()==True) else "U" if(item.isupper()==True) else "N" if(item.isdigit()==True) else "F" for item in password]
    pwdd="".join(result)
    final=False
    if(pwdd.endswith('N')):
        if('U' in pwdd):
            if('L' in pwdd):
                final=True
    return(final)
           

def insertion_sort(l):
    chkList(l)
    result = list()
    for i in l:
        for offset, j in enumerate(result):
            if(j>=i):
                result.insert(offset,i)
                break
                
        else:
            result.append(i)
    return(result)