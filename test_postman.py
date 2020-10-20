import requests

url = "https://api.twilio.com/2010-04-01/Accounts/ACcbb9a272aed2141702026e753988853b/Messages.json"

payload = 'Body=Sent%20from%20Postman%21&To=+19795714727&MediaUrl=https%3A//media.giphy.com/media/xUNemVaUZFSgHxvQXK/giphy.gif&From=+12058285281'
headers = {
  'Authorization': 'Basic QUNjYmI5YTI3MmFlZDIxNDE3MDIwMjZlNzUzOTg4ODUzYjo5ZDhiOTQzMTQ4ZTVhZTZhNjc5YjQ2YTQyNDNkNzZjYQ==',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': 'BCSI-CS-8e1b21bbc9dd7915=1'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
