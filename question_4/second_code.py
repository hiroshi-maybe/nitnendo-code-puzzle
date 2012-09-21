# Nintendo Code Puzzle Question 3
# http://cp1.nintendo.co.jp/moon

class Bars(list):
    
    def __init__(self, str):
        super(Bars, self).__init__(list(str))

    def xor(self, left, right):
        return bool(left)!=bool(right)

    def oneside_rule(self, prev_v, next_v, ins, i):
        if ( self.xor(prev_v=='i', next_v=='i') or self.xor(prev_v=='I', next_v=='I') ):
            self[i]=ins

    def bothside_rule(self, prev_v, next_v, ins, i):
        if ( (prev_v=='i' and next_v=='I') or (prev_v=='I' and next_v=='i') ):
            self[i]=ins
        
    def apply_complex_rule(self, prev_v, next_v, i, oneside_replace_char, bothside_replace_char):
        self.oneside_rule(prev_v, next_v, oneside_replace_char, i)
        self.bothside_rule(prev_v, next_v, bothside_replace_char, i)

    def next(self):
        prev_list=self[:]
        for i in range(len(prev_list)):
            self[i]=' '
            prev_v=prev_list[i-1]
            next_v=prev_list[(i+1)%len(prev_list)]
            if prev_list[i]=='i':
                self[i]='T'
                self.apply_complex_rule(prev_v, next_v, i, 'I', 'T')
            elif prev_list[i]=='T':
                self[i]='i'
                self.apply_complex_rule(prev_v, next_v, i, ' ', 'i')
            elif prev_list[i]=='I':
                self[i]='I'
                self.apply_complex_rule(prev_v, next_v, i, 'T', 'I')
            else:
                # case " "
                self.apply_complex_rule(prev_v, next_v, i, 'i', ' ')
        return self

    def __str__(self):
        return "".join(self)
