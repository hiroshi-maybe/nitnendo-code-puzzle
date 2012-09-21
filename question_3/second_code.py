# Nintendo Code Puzzle Question 3
# http://cp1.nintendo.co.jp/moon
#

class Bars(list):
    
    def __init__(self, str):
        super(Bars, self).__init__(list(str))

    def prev_i(self, i):
        return len(self)+i-1 if i-1<0 else i-1
    def next_i(self, i):
        return i-len(self)+1 if i>len(self)-2 else i+1
    def xor(self, left, right):
        return bool(left)!=bool(right)

    def oneside_rule(self, prev_v, next_v, ins, i):
        if ( self.xor(prev_v=='i', next_v=='i') or self.xor(prev_v=='I', next_v=='I') ):
            self[i]=ins

    def bothside_rule(self, prev_v, next_v, ins, i):
        if ( (prev_v=='i' and next_v=='I') or (prev_v=='I' and next_v=='i') ):
            self[i]=ins

    def next(self):
        prev_list=self[:]
        for i in range(len(prev_list)):
            self[i]=' '
            prev_v=prev_list[self.prev_i(i)]
            next_v=prev_list[self.next_i(i)]
            if prev_list[i]=='i':
                self[i]='T'
                self.oneside_rule(prev_v, next_v, 'I', i)
                self.bothside_rule(prev_v, next_v, 'T', i)
            elif prev_list[i]=='T':
                self[i]='i'
                self.oneside_rule(prev_v, next_v, ' ', i)
                self.bothside_rule(prev_v, next_v, 'i', i)
            elif prev_list[i]=='I':
                self[i]='I'
                self.oneside_rule(prev_v, next_v, 'T', i)
                self.bothside_rule(prev_v, next_v, 'I', i)
            else:
                # case " "
                self.oneside_rule(prev_v, next_v, 'i', i)
                self.bothside_rule(prev_v, next_v, ' ', i)
        return self

    def __str__(self):
        return "".join(self)
