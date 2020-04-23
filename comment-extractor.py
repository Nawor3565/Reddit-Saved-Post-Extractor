import csv
from datetime import datetime
import time
import praw
from praw.exceptions import ClientException

reddit = praw.Reddit(user_agent='Saved comment scraper',
                     client_id='CLIENT_ID', client_secret="CLIENT_SECRET",
                     username='USERNAME', password='PASSWORD')

with open('saved_comments.csv', 'r', newline='') as f:  # Opens the CSV files from your Reddit data request
    next(f)
    progress = 1
    errors = 0
    reader = csv.reader(f)
    first_column = next(zip(*reader))
    data = list(first_column)
    print(data)
    with open('fixed_comments.csv', 'a', newline='', encoding='utf-8') as f2:  # Opens/creates the new CSV where the post info will go
        writer = csv.writer(f2)
        writer.writerow(["Date/Time", "Subreddit", "Link", "Comment ID", "Body"])  # Writes name for each column
        for i in data:
            i = str(i)
            print(i)
            try:
                comment = reddit.comment(id=i)

                subreddit = comment.subreddit
                body = comment.body
                body = body.encode("ascii", errors="ignore").decode()  # Removes special chars like emoji
                link = comment.permalink
                link = "https://reddit.com" + link
                date = comment.created_utc
                date = datetime.fromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S')  # Makes date readable
                print(subreddit)
                print(link)
                print(date)
                print(body)
                writer.writerow([date, subreddit, link, i, body])  # Writes data to new line
                print("Saved comment #" + str(progress) + ", continuing to next item")

            except ClientException:
                print("No comment data returned for #" + str(progress) + ". Skipping...")
                writer.writerow(["NO DATA", "NO DATA", "NO DATA", i, "NO DATA"])
                errors += 1

            f2.flush()  # Forces file to save
            progress += 1
            time.sleep(2)

f2.close()
f.close()
print("FINISHED. Saved" + str(progress) + "comments, with" + str(errors) + "errors.")
