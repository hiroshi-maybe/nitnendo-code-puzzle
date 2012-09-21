# Second version for Nintendo Code Puzzle Question 2
# http://cp1.nintendo.co.jp/2012
#
#  - Simplified focusing on previous value on the same index
#  - Removing duplicate logic using exclusive OR condition bool(condition_a) != bool(condition_b)
#  - However, a little redundant because of initial value "None"
#
# more refined version is second_code.py
#

class SimpleBars(list):
    
    def __init__(self, str):
        super(SimpleBars, self).__init__(list(str))

    def comp(self, prev, ins, i):
        prev_i = len(self)+i-1 if i-1<0 else i-1
        next_i = i-len(self)+1 if i>len(self)-2 else i+1
        if bool(prev[prev_i]=='i') != bool(prev[next_i]=='i'):
            self[i]=ins

    def next(self):
        prev=self[:]
        length=len(prev)
        for i in range(length):
            self[i]=None

        for i in range(length):
            if prev[i]=='i':
                self[i]='T'
            elif prev[i]=='T':
                self[i]='i'
                self.comp(prev, ' ', i)
            else:
                self[i]=' '
                self.comp(prev, 'i', i)
        return self

    def __str__(self):
        return "".join(self)
