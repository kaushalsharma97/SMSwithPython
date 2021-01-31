from twilio.rest import Client 
 
account_sid = 'AC734e02cb45fe236b05db2c2009d5e102' 
auth_token = 'bdad6d49b3180b1a41cbcc7054ce9980' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MG19c36e129ed690d443c1dee386ffb040', 
                              body='I can\'t believe i am doing it!',      
                              to='+917877420051' 
                          ) 
 
print(message.sid)