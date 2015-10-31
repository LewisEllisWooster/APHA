###TINDER



#Session = BOT1


import pynder
FBID = "1479365245705394"
FACEBOOK_TOKEN="CAAGm0PX4ZCpsBAGsJptWYeSdgFQVSvv8XUZBQdz8HB7bb1oBIDdu2PCsiReGV5rXpNLoj3byZCLhqFtrqUZBb4kprabvxyO8n4je4EzTbbk8Iec5Y97tX5eZB2qZBxBPbLdzNmZAJuZB7i28bqKaLD0MIAdMVeZC1tSnwVEm829ljIZB6TfwaDiNFhQ4ttjqWisbciaG7NSWE3xJUIsIj7dCUL"
BOT1 = pynder.Session(FBID,FACEBOOK_TOKEN)


#################################3
#spits JSON script
#with likes


for usr in BOT1.nearby_users():
	usr.like()

####################################

#names of nearby users
print BOT1.nearby_users():

######################################
#gives profile name of bot usr
BOT1.profile

#change location of usr to outback
#BOT1.update_location("-23.3695078","126.5492293")


#Like nearby users




while BOT1.likes_remaining>100:
	try:
		users = BOT1.nearby_users() #.nearby_users() object contains methods
					    #for gender, age
		for u in users:
			u.like()
			log('Liked '+u.name())
	except ValueError:
		continue
	
##############
#Send messages


Method 1 - 

messages = ["Message"] #can do a string or list.

for match in BOT1.matches():
	match.message(messages)



Method 2 - 


str(len(BOT1._api.matches())) + ' matches')
matches = BOT1._api.matches()
for m in matches:
	message(m)



#prints out messages
for m in matches:
	print m["messages"]






