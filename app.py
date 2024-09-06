from flask import Flask, render_template, url_for,request
import numpy as np
import pickle
import ScrapperUltimate

app = Flask(__name__)
model = pickle.load(open('ensemble_model.pkl','rb'))

## fake profile usernames 
## mayur19942018

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        # Get form data
        username = request.form ['username']
        
        print(request.form)

        data = ScrapperUltimate.get_data_from_username(username)
        # profilepic = int(data['profile_pic'])
        # usernameLength = float(data['nums_username'])
        # fullnameWords = int(data['fullname_words'])
        # fullnameLength = int(data['nums_fullname'])

        # Define variables and cast them to their respective data types
        profile_pic = int(data["profile_pic"])
        nums_username = float(data["nums_username"])
        length_username = int(data["length_username"])
        fullname_words = int(data["fullname_words"])
        nums_fullname = float(data["nums_fullname"])
        length_fullname = int(data["length_fullname"])
        name_equals_username = int(data["name_equals_username"])
        description_length = int(data["description_length"])
        external_url = int(data["external_url"])
        private = bool(data["private"])  # Assuming 0 represents False and non-zero represents True
        num_posts = int(data["num_posts"])
        num_followers = int(data["num_followers"])
        num_follows = int(data["num_follows"])
        engagement_ratio = float(data["engagement_ratio"])
        social_interaction_index = int(data["social_interaction_index"])
        profile_completeness_score = int(data["profile_completeness_score"])
        avg_description_word_length = float(data["avg_description_word_length"])
        list_ = [
            profile_pic,
            nums_username,
            # length_username,
            fullname_words,
            nums_fullname,
            # length_fullname,
            name_equals_username,
            description_length,
            external_url,
            private,
            num_posts,
            num_followers,
            num_follows,
            engagement_ratio,
            social_interaction_index,
            profile_completeness_score,
            avg_description_word_length
        ]

        # features = [profilepic, username, words, fullname, equal, description, external, private, posts, followers, following]
        features = list_
        # Make prediction
        prediction = model.predict([features])
        
        if prediction[0] == 1:
            result = "Fake Profile"            
        else:
            result = "Real Profile"
            
        print("Features:", features)  # Check the features being passed to the model
        print("Prediction:", prediction)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)