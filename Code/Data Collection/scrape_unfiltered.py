import praw
import prawcore
import pandas as pd
import time
import spacy
import emoji

# Start the timer
start_time = time.time()

reddit = praw.Reddit(
    client_id="bABwupYmEVJzYQvqwSZZZg",
    client_secret="hjL4AZFbn4bIKb8MwoJNIX1iddLPxg",
    user_agent="kpop:v0.1"
)

nlp = spacy.load("en_core_web_sm")

def is_bot_comment(comment):
    bot_indicators = ["I am a bot", "action was performed automatically"]
    return any(phrase in comment.body for phrase in bot_indicators)

def replace_emojis(text):
    text = emoji.demojize(text, delimiters=("", ""))
    words = text.split()
    transformed_words = []
    for word in words:
        if word.startswith(':') and word.endswith(':'):
            # Transform and capitalize the emoji description, remove the colons
            word = word.strip(':').replace('_', ' ').upper()
            word = f"[{word}]"
        transformed_words.append(word)
    return ' '.join(transformed_words)

# store post information
data = []

subreddit_name = input("Enter subreddit name: r/")
print(f"Scraping from r/{subreddit_name}...")

def get_all_comments(submission):
    submission.comments.replace_more(limit=None)
    comment_queue = submission.comments[:]
    all_comments = []
    while comment_queue:
        comment = comment_queue.pop(0)
        all_comments.append(comment)
        comment_queue.extend(comment.replies)
    return all_comments

for post in reddit.subreddit(subreddit_name).hot(limit=10000):
    submission = reddit.submission(id=post.id)
    try:
        all_comments = get_all_comments(submission)
    except prawcore.exceptions.TooManyRequests:
        print("Rate limit exceeded, sleeping for 60 seconds.")
        time.sleep(60)
        all_comments = get_all_comments(submission)

    comment_data = []
    for comment in all_comments:
        if not is_bot_comment(comment):
            commenter = comment.author.name if comment.author else "Deleted_User"
            comment_text = replace_emojis(comment.body.replace('\n', ' ')) 
            comment_info = {
                "Username": commenter,
                "Comment": comment_text
            }
            comment_data.append(comment_info)

    # store the post without filtering
    post_data = {
        "Subreddit": subreddit_name,
        "Title": submission.title,
        "Body": submission.selftext,
        "URL": submission.url,
        "Comments": '\n------\n'.join(f"{c['Username']}: {c['Comment']}" for c in comment_data)
    }
    data.append(post_data)

# Create a DataFrame from the data
df = pd.DataFrame(data)

output_file = subreddit_name + "_unfiltered.csv"
df.to_csv(output_file, index=False)
print(f"All data has been saved to '{output_file}'.")

# End the timer and calculate the elapsed time
end_time = time.time()
elapsed_time = end_time - start_time

# Convert elapsed time to hours, minutes, and seconds
hours, rem = divmod(elapsed_time, 3600)
minutes, seconds = divmod(rem, 60)

# Construct the time taken message
time_taken = []
if hours > 0:
    time_taken.append(f"{int(hours)} hours")
if minutes > 0 or hours > 0:
    time_taken.append(f"{int(minutes)} minutes")
time_taken.append(f"{int(seconds)} seconds")

print(f"Time taken to scrape data: {', '.join(time_taken)}")
print(f"Shape of the combined dataframe: {df.shape}")
