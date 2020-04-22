# Reddit-Saved-Post_Extractor
## REQUIREMENTS  
  Python 3.6 (untested with Python 3.7+)  
  PSAW (pip install psaw)  
  PRAW (pip install praw)  
  Reddit API key (for scraping comments only)

## INFO

Reddit has an annoying limit on all page results. It will only show you the first 1,000 results, no matter what. This means you can only access your 1,000 most recently saved posts, and anything over that limit used to effectivly be gone.

However, your saved posts are still remembered by Reddit, you just can't SEE anything but the first thousand. This means that, thanks to the GDPR, you can request your full userdata, which includes all of your saved posts.

In order to use this tool, you must first get your data from https://www.reddit.com/settings/data-request. This can take quite a while (it took over a month each for all three of my accounts). Once it finally comes through, you'll get a .zip file full of .csv files. The ones we're interested in are saved_posts.csv and saved_comments.csv.

Put the file in the same folder as the corrosponding Python script and run the script. It will make a new .csv file, which includes all the important data about each saved post, such as the date, title, link, media, etc. etc.

post-extractor.py requires no special setup, but comment-extractor.py uses the official Reddit API instead of PushShift.IO because the latter mysteriously can't access certain comments (see here: https://redd.it/g6an89). This means you need to get an API key from Reddit (search Google if you're not sure how), and put the information in comment-extractor.py. You can then run it like normal.

I plan to provide easy-to-use executable files in the future. 
