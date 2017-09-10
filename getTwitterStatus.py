from twitter import Twitter, OAuth

t = Twitter(auth=OAuth("Access Token","Access Token Secret","Consumer Key","Consumer Secret"))
pythonStatuses = t.statuses.user_timeline(screen_name="montypython", count=5)
print(pythonStatuses)