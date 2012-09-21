#!/usr/bin/ruby
i=0
while(true)
  if (i**17) % 3569 == 915 then
    p i.to_s
    break
  end
  i+=1
end
