import base64
import email
from apiclient import errors
from apiclient import discovery
import httplib2
from oauth2client import file, client, tools


SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
http = creds.authorize(httplib2.Http())
service = discovery.build('gmail', 'v1', http=http)
msg_id="1585a9d7d7e2fb28"
user_id="sruthisneha@gmail.com"

def GetMessage(service, user_id, msg_id):
  """Get a Message with given ID.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    msg_id: The ID of the Message required.

  Returns:
    A Message.
  """
  try:
    message = service.users().messages().get(userId=user_id, id=msg_id).execute()

    print ('Message snippet: %s' % message['snippet'])

    return message
   
    #headers = ['X-Original-To','Message-ID','Date','Delivered-To']
    #result = message.get(userId = user_id,id = msg_id,format = 'metadata',metadataHeaders = headers).execute()
  except errors.HttpError or error:
    print ('An error occurred: %s' % error)


def GetMimeMessage(service, user_id, msg_id):
  """Get a Message and use it to create a MIME Message.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    msg_id: The ID of the Message required.

  Returns:
    A MIME Message, consisting of data from Message.
  """
  try:
    message = service.users().messages().get(userId=user_id, id=msg_id,
                                             format='raw').execute()

    print ('Message snippet: %s' % message['snippet'])

    msg_str = base64.urlsafe_b64decode(message['raw'].encode('ASCII'))

    mime_msg = email.message_from_string(msg_str)

    return mime_msg
  except errors.HttpError or error:
    print ('An error occurred: %s' % error)


message=GetMessage(service,user_id,msg_id)
print(message)

