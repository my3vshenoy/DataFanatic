## 2. Authenticating with the API ##

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
response = requests.get("https://oauth.reddit.com/r/python/top", headers = headers, params = {"t":"day"})
python_top = response.json()

## 3. Getting the Most Upvoted Post ##

python_top_articles = python_top["data"]["children"]
most_upvoted = ""
most_upvotes = 0
for item in python_top_articles:
    i = item["data"]
    if i["ups"] >= most_upvotes:
        most_upvoted = i["id"]
        most_upvotes = i["ups"]


## 4. Getting Post Comments ##

response = requests.get("https://oauth.reddit.com/r/python/comments/4b7w9u", headers = headers)
comments = response.json()

## 5. Getting the Most Upvoted Comment ##

#Extract the comments list from the comments variable
comments_list = comments[1]["data"]["children"]
most_upvoted_comment = ""
most_upvotes_for_comments = 0
for comment in comments_list:
    i = comment["data"]
    if i["ups"] >= most_upvotes_for_comments:
        most_upvoted_comment = i["id"]
        most_upvotes_for_comments = i["ups"]

## 6. Upvoting a Comment ##

#Make a POST request to the /api/vote endpoint to upvote the most upvoted comment from the last screen.
params = {"dir": 1, "id" : "d16y4ry"}
response = requests.post("https://oauth.reddit.com/api/vote", headers = headers, json = params)
status = response.status_code