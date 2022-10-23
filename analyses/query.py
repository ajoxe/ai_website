from urllib.request import urlopen
import urllib.parse
import json


# Runs a search query to ask ai site
def search(cont):
    # Format query url
    base_query_url = 'http://44.203.178.145/search?query='
    query = urllib.parse.quote(cont)
    query_url = base_query_url + query

    # Request query and deserialize
    serialized_data = urlopen(query_url).read()
    data = json.loads(serialized_data)
    results = data.get('results')

    # Format response for page
    answers = []
    for idx, result in enumerate(results):
        answer = result[0]
        if answer:
            answer_and_links = {'answer': answer}
            link = result[1]
            if link:
                answer_and_links['link'] = link
            answers.append(answer_and_links)

    # Set default answer if response is empty
    default_answer_text = "Sorry, we were not able to find an answer"
    default_answer = {'answer': default_answer_text}
    if not answers:
        answers.append(default_answer)

    return answers
