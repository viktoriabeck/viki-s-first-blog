"""
print ("Hello Djangogirls!")
if 1 == 2:
	print ("mindig igaz") 
else:
	print ("nemigaz")

szam = 7
if szam % 2 == 0:
	print ("ez a szám páros  %s" % szam)
else:
	print ("ez a szám páratlan %s" % szam)

def name (text):
	print ("Viki %s" % text)
name("Beck")

def name2 (text1, text2 = "mindigez"):
	print ("Viki %s %s" % (text1, text2))
name2("Beck")

girls = ["Viki", "Anna", "Livi"]
for girl in [girls[1]]:
	if girl == "Anna":
		print (girl + " micimacko")
"""

def name2 (text1 = "", text2 = "mindigez", text3 = "sosemez"):
	return ("Viki %s %s %s" % (text1, text2, text3))
print (name2())