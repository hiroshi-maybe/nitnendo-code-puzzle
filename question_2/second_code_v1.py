# First version for Nintendo Code Puzzle Question 2
# http://cp1.nintendo.co.jp/2012
# Including redundant logics
#  - default value is set to "None"
#  - complex conditional branches because of processing described rules naively

class SimpleBars(list):
    
    def __init__(self, str):
        super(SimpleBars, self).__init__(list(str))
    
    def next(self):
        prev_list=self[:]
        length=len(prev_list)
        for i in range(length):
            self[i]=None

        for i in range(length):
            if self[i] is not None:
              continue  
            elif prev_list[self.neibr(i-1)]=='i' and prev_list[self.neibr(i+1)]=='i':
                if  prev_list[i]=='T':
                    self[i]='i'
                elif prev_list[i]==' ':
                    self[i]=' '
            elif prev_list[self.neibr(i-1)]=='i':
                if prev_list[i]=='T':
                    self[i]=' '
                elif prev_list[i]==' ':
                    self[i]='i'
            elif prev_list[self.neibr(i+1)]=='i':
                    if prev_list[i]=='T':
                        self[i]=' '
                    elif prev_list[i]==' ':
                        self[i]='i'
            else:
                if prev_list[i]=='T':
                    self[i]='i'
                elif prev_list[i]==' ':
                    self[i]=' '
                else:
                    self[i]='T'
        return self

    def neibr(self, index):
        if index<0:
            return len(self)+index
        elif index<len(self):
            return index
        else:
            return index-len(self)
            

    def __str__(self):
        return "".join(self)
