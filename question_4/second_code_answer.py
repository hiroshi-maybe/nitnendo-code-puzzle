from second_code import Bars
from third_code import decode_morse

val="ITT TI I T TIii"
bs = Bars(val)
i=0;
while(True):
    before=val
    val=str(bs.next())
    if (val == "ITT TI I T TIii"): break
print decode_morse(before)
#print("answer: " + decode_morse(str(bs)))
