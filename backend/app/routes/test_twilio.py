account_sid = "AC6ce4fb7e878b36fdb126ef65f498caf2".strip()
auth_token = "5259f15df4da3c6f8c3abc0a8cb82b48".strip()

from twilio.rest import Client
client = Client(account_sid, auth_token)

# Test authentication
account = client.api.accounts(account_sid).fetch()
print("Authenticated account SID:", account.sid)
