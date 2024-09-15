import praw
import prawcore
import pandas as pd
import time
import spacy
import string
import emoji

# Start the timer
start_time = time.time()

reddit = praw.Reddit(
    client_id="bABwupYmEVJzYQvqwSZZZg",
    client_secret="hjL4AZFbn4bIKb8MwoJNIX1iddLPxg",
    user_agent="kpop:v0.1"
)

nlp = spacy.load("en_core_web_sm")

# load phrases from a file
def load_support_phrases(file_path):
    with open(file_path, 'r') as file:
        phrases = [line.strip().lower() for line in file if line.strip()]
    return phrases

# detect and extract support instances in text
def extract_support_instances(text, category_phrases):
    doc = nlp(text.lower().translate(str.maketrans('', '', string.punctuation)))
    support_instances = []
    for sentence in doc.sents:
        if any(phrase in sentence.text for phrase in category_phrases):
            support_instances.append(sentence.text)
    return support_instances if support_instances else []

# Load emotional support phrases from file
emotional_support_phrases = load_support_phrases("wordlist.txt")

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

# store filtered post information
filtered_data = []

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
                "Comment": comment_text,
                "Emotional Support Instances": extract_support_instances(comment_text, emotional_support_phrases)
            }
            comment_data.append(comment_info)

    # support instances from title and body
    support_in_title = extract_support_instances(replace_emojis(submission.title), emotional_support_phrases)
    support_in_body = extract_support_instances(replace_emojis(submission.selftext), emotional_support_phrases)

    # store the post if it contains any support instances or at least one support instance in comments
    if support_in_title or support_in_body or any(c['Emotional Support Instances'] for c in comment_data):
        post_data = {
            "Subreddit": subreddit_name,
            "Title": submission.title,
            "Body": submission.selftext,
            "URL": submission.url,
            "Comments": '\n------\n'.join(f"{c['Username']}: {c['Comment']}" for c in comment_data),
            "Emotional Support Instances in Title": support_in_title,
            "Emotional Support Instances in Body": support_in_body,
            "Emotional Support Instances in Comments": [c['Emotional Support Instances'] for c in comment_data if c['Emotional Support Instances']]
        }
        filtered_data.append(post_data)

# Create a DataFrame from the filtered data
df_filtered = pd.DataFrame(filtered_data)

output_file = subreddit_name + "_filtered.csv"
df_filtered.to_csv(output_file, index=False)
print(f"Filtered data has been saved to '{output_file}'.")

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
print(f"Shape of the combined dataframe: {df_filtered.shape}")
