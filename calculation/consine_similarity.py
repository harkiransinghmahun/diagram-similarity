from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import spacy


def get_cosine(list1, list2):
    vectoriser = CountVectorizer()

    # Transform the strings into vectors
    vectors = vectoriser.fit_transform([" ".join(list1), " ".join(list2)])

    # Compute the cosine similarity
    cosine_sim = cosine_similarity(vectors)

    # Extract the similarity value
    similarity = cosine_sim[0, 1]

    print("list 1: " + str(list1) + " list 2: " + str(list2) + "-------->" + str(similarity))

    return similarity


nlp = spacy.load("en_core_web_md")


def get_cosine_similarity(list1, list2):
    # Convert each list of words to a vector representation

    vector1 = nlp(" ".join(list1)).vector
    vector2 = nlp(" ".join(list2)).vector

    # Calculate cosine similarity using sklearn
    similarity = cosine_similarity([vector1], [vector2])[0, 0]

    print("list 1: " + str(list1) + " list 2: " + str(list2) + "-------->" + str(similarity))

    return similarity


