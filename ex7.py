#-*- coding: utf-8 -*-
print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow' #使用%s代替后面的% ''的内容
print "And everywhere that Mary went."
print "." * 10 #Can print ten dots

end1="C"
end2="h"
end3="e"
end4="e"
end5="s"
end6="e"
end7="B"
end8="u"
end9="r"
end10="g"
end11="e"
end12="r"

#watch that command at the end. try removing it to see what happens
print end1+end2+end3+end4+end5+end6
print end7+end8+end9+end10+end11+end12
print end1 + end2 + end3 + end4 + end5 + end6, end7 + end8 + end9 + end10 + end11 + end12#

print end1 * 10
#print "Its fleece was white as %s." * 10  % 'snow' #错误是因为* 10的位置不对，如下面两条:
print "Its fleece was white as ." * 10
print "Its fleece was white as %s."  % 'snow' * 10 #放在后面才行
