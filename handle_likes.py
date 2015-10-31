#Finds nearby users and likes all of them



def handle_likes():
    while True:
        try:
            users = session.nearby_users()
            for u in users:
                if u.name == 'Tinder Team':
                    log('Out of swipes, pausing one hour...')
                    return
                u.like()
                log('Liked ' + u.name)
        except ValueError:
            continue
