from django.db import models
# Create your models here.

#  This is an abstract base class. Regardless of whether the post came
#  from Twitter or Facebook, they'll all have these following fields.
#  @param timestamp: The date and time at which the post was made.
#  @param author: The person who wrote the post.
#  @param source_text: The full text of the post.


class Post(models.Model):
    timestamp = models.DateTimeField(default=None, blank=True)
    author = models.CharField(
        default="Anonymous", blank=False, max_length=255)
    source_text = models.TextField(default=None, blank=False)

    class Meta:
        abstract = True

# The Tweet class extends Post, meaning that it inherits the member fields
# contained within the Post class while gaining additional functionality
# because there's just so much more data available on tweets.
# @param content_id: An identifying string. Not quite sure what it does yet,
#   but it looks important.
# @param detected_language: the detected language in which the post was written
# @param detected_language_strength: I think it's the system's confidence
#   that it detected the correct language.
# @param document_sentiment_strength: A quantitative sentiment score.
# @param document_sentiment_type: A qualitative sentiment score.


class Tweet(Post):
    POSITIVE = "POS"
    NEGATIVE = "NEG"
    NEUTRAL = "NEU"
    SENTIMENT_CHOICES = (
        (POSITIVE, "Positive"),
        (NEGATIVE, "Negative"),
        (NEUTRAL, "Neutral"),
    )
    content_id = models.CharField(default=None, blank=True, max_length=255)
    detected_language = models.CharField(
        default="English", blank=True, max_length=255)
    detected_language_strength = models.FloatField(default=0)
    document_sentiment_strength = models.FloatField(default=0)
    document_sentiment_type = models.CharField(
        choices=SENTIMENT_CHOICES, default=NEUTRAL, max_length=3)
