reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

# Task 1: Keyword Highlighter
# Write a program that searches through reviews list and looks for keywords such as "good", "excellent", "bad", "poor", and "average".
# We want you to capitalize those keywords then print out each review. Print out each review with the keywords in uppercase so they stand out.
# So for the first string in the reviews list, we want it to say: "This product is really GOOD. I'm impressed with its quality."


keywords = positive_words + negative_words

def keyword_highlighter(review, keywords):
    for keyword in keywords:
        review = review.replace(keyword, keyword.upper())
        review = review.replace(keyword.capitalize(), keyword.upper())
    return review

for review in reviews:
    highlighted_review = keyword_highlighter(review, keywords)
    print(highlighted_review)


# Task 2: Sentiment Tally
# Develop a function that tallies the number of positive and negative words in each review.
# The function should return the total count of positive and negative words.

def sentiment_tally(reviews, positive_words, negative_words):
    import re
    positive_count = 0
    negative_count = 0

    for review in reviews:

        words = re.findall(r"\b\w+\b", review.lower())

        for word in words:
            if word in positive_words:
                positive_count += 1
            elif word in negative_words:
                negative_count += 1
    return positive_count, negative_count


positive_count, negative_count = sentiment_tally(reviews, positive_words, negative_words)

print(f"Positive words count: {positive_count}")
print(f"Negative words count: {negative_count}")





# Task 3: Review Summary
# Implement a script that takes the first 30 characters of a review and appends "…" to create a summary.
# Ensure that the summary does not cut off in the middle of a word.



def review_summary(review, max_length=30, appended_ending='...'):
    max_length = 30

    if len(review) <= max_length:
        return review + appended_ending
    else:
        return ' '.join(review[:max_length+1].split(' ')[0:-1]) + appended_ending
    
summaries = [review_summary(review) for review in reviews]

for summary in summaries:
    print(summary)