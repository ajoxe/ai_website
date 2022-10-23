from urllib.request import urlopen
import json


def search(cont):
    base_query_url = 'http://44.203.178.145/search?query='
    query_url = base_query_url + cont
    serialized_data = urlopen(query_url).read()

    data = json.loads(serialized_data)
    results = data.get('results')
    default_answer = "Sorry, we were not able to find an answer"
    answer1 = None
    link1 = None
    answer2 = None
    link2 = None
    if results:
        answer1_result = results[0]
        answer1 = answer1_result[0]
        link1 = answer1_result[1]
        if len(results) == 2:
            answer2_results = results[1]
            answer2 = answer2_results[0]
            link2 = answer2_results[1]
    answers = []
    if not answer1:
        answers.append(default_answer)
    else:
        answers.append(answer1)
        if answer2:
            answers.append(answer2)
    links = [link1] if link1 else None
    if links and link1:
        links.append(link2)
    return answers, links
