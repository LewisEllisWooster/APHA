#Finds nearby users and likes all of them



def handle_likes():
       
    while BOT1.likes_remaining>0:
	    try:
	    	users = BOT1.nearby_users() #.nearby_users() object contains methods
					    #for gender, age
		    for u in users:
			    u.like()
			    log('Liked '+u.name())
	    except ValueError:
		    continue
