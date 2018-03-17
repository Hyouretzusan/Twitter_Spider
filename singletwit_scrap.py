from twitter import *

aToken = r"2354306079-sDY74vrY2tIsO5B4lIgbGKni1y3UFYPuE7kGW3E"
aTokenSec = r"xJQGZipFJRU7yi0wAGsfo1TvrUaTp1TQklwveOqUDd6EY"
cKey = r"mjuoCpYhKAyInosFQbVdHMjrG"
cKeySec = r"Yq7PfP8Vy48JehXXjLNcNqekjVVDnpGTQStx7jTB89aHH7tGWN"

t = Twitter(auth=OAuth(aToken, aTokenSec, cKey, cKeySec))
statusUpdate = t.statuses.update(status='Be a pythonista')
print(statusUpdate)