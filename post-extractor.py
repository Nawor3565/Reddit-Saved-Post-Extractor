import csv
from datetime import datetime
import time
from psaw import PushshiftAPI

api = PushshiftAPI()

with open('saved_posts.csv', 'r', newline='') as f:  # Opens the CSV files from your Reddit data request
    next(f)
    progress = 1
    reader = csv.reader(f)
    first_column = next(zip(*reader))
    data = list(first_column)
    with open('fixed_posts.csv', 'a', newline='') as f2:  # Opens/creates the new CSV where the post info will go
        writer = csv.writer(f2)
        writer.writerow(["Date/Time", "Subreddit", "Post Title", "Link", "Is Self-Post?", "URL", "Post ID"])  # Writes name for each column
        for i in data:
            i = str(i)
            search = api.search_submissions(ids=i, limit=1, aggs='title')  # Searches Pushshift for matching post
            for post in search:
                subreddit = post.subreddit
                title = post.title
                title = title.encode("ascii", errors="ignore").decode()  # Removes special chars like emoji
                link = post.full_link
                date = post.created_utc
                date = datetime.fromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S')  # Makes date readable
                is_self = post.is_self
                media = ""
                print(subreddit)
                print(title)
                print(link)
                print(date)
                if is_self is False:  # If post is text-only, don't try to get whatever it links to
                    media = post.url
                    print(media)
                writer.writerow([date, subreddit, title, link, str(is_self), media, i])  # Writes data to new line
                f2.flush()  # Forces file to save
                print("Saved post #" + str(progress) + ", continuing to next item")
                progress += 1
            time.sleep(1)

f2.close()
f.close()
