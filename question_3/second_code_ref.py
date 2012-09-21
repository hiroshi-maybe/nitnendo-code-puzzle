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
    def _xor(self, prev, ins, i):
        if (bool(prev[self.prev_i(i)]=='i') != bool(prev[self.next_i(i)]=='i')) or (bool(prev[self.prev_i(i)]=='I') != bool(prev[self.next_i(i)]=='I')):
            self[i]=ins
    def _and(self, prev, ins, i):
        if (bool(prev[self.prev_i(i)]=='i') and bool(prev[self.next_i(i)]=='I')) or (bool(prev[self.prev_i(i)]=='I') and bool(prev[self.next_i(i)]=='i')):
            self[i]=ins

    def next(self):
        prev=self[:]
        for i in range(len(prev)):
            self[i]=' '
            if prev[i]=='i':
                self[i]='T'
                self._xor(prev, 'I', i)
                self._and(prev, 'T', i)
            elif prev[i]=='T':
                self[i]='i'
                self._xor(prev, ' ', i)
                self._and(prev, 'i', i)
            elif prev[i]=='I':
                self[i]='I'
                self._xor(prev, 'T', i)
                self._and(prev, 'I', i)
            else:
                # case " "
                self._xor(prev, 'i', i)
                self._and(prev, ' ', i)
        return self

    def __str__(self):
        return "".join(self)
