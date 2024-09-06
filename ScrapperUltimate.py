import instaloader
import json
import re

# Function to calculate engagement ratio
def calculate_engagement_ratio(followers_count, num_posts):
    if num_posts == 0:
        return 0
    return followers_count / num_posts

# Function to calculate social interaction index
def calculate_social_interaction_index(followers_count, following_count, num_posts):
    return followers_count + following_count + num_posts

# Function to calculate profile completeness score
def calculate_profile_completeness_score(has_profile_picture, has_external_url, bio_length):
    return int(has_profile_picture + has_external_url + (bio_length > 0))

# Function to calculate average description word length
def calculate_avg_description_word_length(bio_length, biography):
    if bio_length == 0:
        return 0
    return len(biography.split()) / bio_length

def get_data_from_username(username):
    # Create an instance of the Instaloader class
    loader = instaloader.Instaloader()

    # Load the profile of the user
    profile = instaloader.Profile.from_username(loader.context, username= username)

    # Extract profile metadata into separate variables
    username = profile.username
    full_name = profile.full_name
    biography = profile.biography
    followers_count = profile.followers
    following_count = profile.followees

    # Additional features
    has_profile_picture = bool(profile.profile_pic_url)  # 0 or 1 (1 if there's a profile picture, 0 otherwise)

    numerical_chars_in_username = sum(c.isdigit() for c in username)
    username_length = len(username)
    ratio_numerical_chars_in_username = numerical_chars_in_username / username_length  # Decimal format

    full_name_tokens = len(full_name.split())
    numerical_chars_in_full_name = sum(c.isdigit() for c in full_name)
    full_name_length = len(full_name)
    #ratio_numerical_chars_in_full_name = numerical_chars_in_full_name / full_name_length  # Float format

    # Remove all non-alphabetic characters from username and full name
    clean_username = re.sub(r'[^a-zA-Z]', '', username)
    clean_full_name = re.sub(r'[^a-zA-Z]', '', full_name)

    # Compare the cleaned username and full name
    same_username_and_full_name = int(clean_username.lower() == clean_full_name.lower())  # 0 or 1

    bio_length = len(biography)  # Number of characters in the biography

    has_external_url = int(bool(profile.external_url))  # 0 if no external URL, 1 if there is one

    is_private = int(profile.is_private)  # 0 if not private, 1 if private

    num_posts = profile.mediacount  # Number of posts

    # Calculate additional features
    engagement_ratio = calculate_engagement_ratio(followers_count, num_posts)
    social_interaction_index = calculate_social_interaction_index(followers_count, following_count, num_posts)
    profile_completeness_score = calculate_profile_completeness_score(has_profile_picture, has_external_url, bio_length)
    avg_description_word_length = calculate_avg_description_word_length(bio_length, biography)

    # Define a dictionary to hold the extracted data
    data = {
        "profile_pic": has_profile_picture,
        "nums_username": numerical_chars_in_username,
        "length_username": username_length,
        "fullname_words": full_name_tokens,
        "nums_fullname": numerical_chars_in_full_name,
        "length_fullname": full_name_length,
        "name_equals_username": same_username_and_full_name,
        "description_length": bio_length,
        "external_url": has_external_url,
        "private": is_private,
        "num_posts": num_posts,
        "num_followers": followers_count,
        "num_follows": following_count,
        "engagement_ratio": engagement_ratio,
        "social_interaction_index": social_interaction_index,
        "profile_completeness_score": profile_completeness_score,
        "avg_description_word_length": avg_description_word_length
    }

    # Convert the dictionary to JSON
    json_data = json.dumps(data, indent=4)

    # Print the JSON data
    print(json_data)
    return data
