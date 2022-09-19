
TRUSTED_SENDER = ("test@hotmail.com",)
#TRUSTED_SENDER = ("xxx@c.q")

searchQeury = []
print(len(TRUSTED_SENDER))
if (len(TRUSTED_SENDER) == 1):
    searchQeury.append("FROM " + TRUSTED_SENDER[0])
if (len(TRUSTED_SENDER) == 2):
    searchQeury.append("OR")
    searchQeury.append(["FROM "+TRUSTED_SENDER[0]])
    searchQeury.append(["FROM "+TRUSTED_SENDER[1]])
if (len(TRUSTED_SENDER) > 2):
    searchQeury.append("OR")
    searchQeury.append(["FROM "+TRUSTED_SENDER[0]])
    searchQeury.append(["FROM "+TRUSTED_SENDER[1]])
    for m in range(2, len(TRUSTED_SENDER)):
        searchQeury.insert(0, ["FROM " + TRUSTED_SENDER[m]])
        searchQeury.insert(0, "OR")


print(searchQeury)
