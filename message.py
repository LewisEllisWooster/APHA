def message(match):
  ms = match['messages']
  thisUSR = BOT1.profile.id
  if not ms:
    send(match,"Initial Message") #if no message send initial message
    return
  said = False
  count=0
  name = match['person']['name']
  for m in ms:
    if m['from'] == thisUSR: #checks whether messages come from BOT or not.
      count+=1
      said = False
  if count>=len(messages):
    log('Finished conversation with ' + name)
        return
  if said:
    send(match,count)
  else:
    log('No new messages from ' + name)
    

def send(match, message_no):
    for m in messages[message_no]:
        BOT1._api._post('/user/matches/' + match['id'],
                           {"message": m})
        time.sleep(3)
    log('Sent message ' + str(message_no) + ' to ' + match['person']['name'])


def handle_matches():
  str(len(BOT1._api.matches())) + ' matches')
  matches = BOT1._api.matches()
  for m in matches:
	  message(m)
