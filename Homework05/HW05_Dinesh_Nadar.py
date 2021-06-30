def chkstr(s):
    """Checking if the string is valid"""
    if type(s) == str:
        return s
    else:
        raise ValueError('Not a valid string')

def reverse(s):
    """reversing the string passed"""
    chkstr(s)
    s1 = ''
    for c in s:
        s1 = c + s1
    return s1


def rev_enumerate(seq):
    """reversing with offset value"""
    chkstr(seq)
    for i in range(len(seq)-1, -1, -1):
        yield(i, seq[i])


def find_second(target, string):
    """finding the second occurrence of the target in the passed string"""
    chkstr(target)
    chkstr(string)
    s1 = string.find(target)
    if(s1 == -1):
        print("target does not have first occurrence")
    else:
        return(string.find(target, s1+1))


def get_lines(file_name):
    """opening and reading the file"""
    try:
        fp = open(file_name, 'r')
    except FileNotFoundError:
        print("Can't Open", file_name)
    else:
        with fp:
            for line in fp:
                line = line.strip("\n")
                while(line.endswith("\\")):
                    line = line[:-1]+fp.readline().strip("\n")
                if(line.find('#') == 0):
                    continue
                if(line.find('#') != -1):
                    yield(line[:(line.find('#'))].strip())
                else:
                    yield(line.strip())
