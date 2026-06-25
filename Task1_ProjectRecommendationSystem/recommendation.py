import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("projects.csv")

# Create vectors
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(df["description"])

print("=== AI Project Recommendation System ===")
print("Type 'exit' anytime to quit.\n")

while True:

    user_interest = input("Enter your interests: ")

    if user_interest.lower() == "exit":
        print("Thank you for using the system!")
        break

    user_vector = vectorizer.transform([user_interest])

    similarity_scores = cosine_similarity(
        user_vector,
        tfidf_matrix
    )

    top_indices = similarity_scores.argsort()[0][-5:][::-1]

    print("\nRecommended Projects:")

    for index in top_indices:
        print("-", df.iloc[index]["project_name"])

    print("\n" + "-" * 40 + "\n")