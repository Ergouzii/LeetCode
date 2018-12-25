def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    print(2)
    result = False
    if len(s) % 2 != 0: # len(s) must be even number
        return result
    open_brackets = ['(', '[', '{']
    closed_brackets = [')', ']', '}']
    dic = dict(zip(open_brackets, closed_brackets))
    for c in s:
        print(c)
        if c in open_brackets:
            print('1')
            
            if dic[c] not in s:
                print('2')
                result = False
            elif (s.index(dic[c]) - s.index(c)) % 2 == 1:
                result = True
            
    return result

def main():
    s = '[()]'
    result = isValid(s)

    main()