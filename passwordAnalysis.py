import os, sys, operator
pw_hash = []

#Fox news db dump
"""
fox = open('foxnews.txt','r')
foxlines = fox.readlines()
for line in foxlines:
	pw_hash.append(line.strip().split(':')[1])
	
fox.close()

#PBS db dump
pbs = open('pbs.org_pressroom_users_database.txt','r')
pbslines = pbs.readlines()
for line in pbslines:
	pH = line.strip().split('|')[1]
	pw_hash.append(pH.strip())
pbs.close()
"""
#Sony 
auto = open("Sownage/Sony_Pictures/Sony_Pictures_International_AUTOTRADER_USERS.txt",'r')
autolines = auto.readlines()
tempEmail = []
prevPass = None
for line in autolines:
	lineList = line.strip().split('|')
	tEmail = (lineList[-2]).strip()
	newPass = str((lineList[-3]).strip())
	if tEmail not in tempEmail and newPass != prevPass:
		if '9452' == newPass:
			print tEmail
		tempEmail.append(tEmail)
		pw_hash.append(newPass)
	prevPass = newPass

#Sony 
beauty = open("Sownage/Sony_Pictures/Sony_Pictures_International_BEAUTY_USERS.txt",'r')
beautylines = beauty.readlines()
tempEmail = []
for line in beautylines:
	lineList = line.strip().split('|')
	tEmail = (lineList[0]).strip()
	newPass = (lineList[1]).strip()
	if tEmail not in tempEmail and newPass != prevPass:
		tempEmail.append(tEmail)
		pw_hash.append(newPass)
	prevPass = newPass

#boca
#Sony 
beauty = open("Sownage/Sony_Pictures/Sony_Pictures_International_DELBOCA_USERS.txt",'r')
beautylines = beauty.readlines()
tempEmail = []
for line in beautylines:
	lineList = line.strip().split('|')
	tEmail = (lineList[0]).strip()
	newPass = (lineList[1]).strip()
	if tEmail not in tempEmail and newPass != prevPass:
		tempEmail.append(tEmail)
		pw_hash.append(newPass)
	prevPass = newPass
	
pw_dict = {}
for el in pw_hash:
	if el in pw_dict:
		pw_dict[el] += 1
	else:
		pw_dict[el] = 1

sorted_pw = sorted(pw_dict.iteritems(), key=operator.itemgetter(1), reverse=True)
	
print 'Total elements:'+str(len(pw_hash))
print 'Unique elements:'+str(len(set(pw_hash)))
print 'Top 100 passwords'
print sorted_pw[:100]