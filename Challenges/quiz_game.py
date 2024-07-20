import requests
import json
import random

quiz_api_request = requests.get('https://opentdb.com/api.php?amount=10&category=27&difficulty=easy&type=multiple')
request_dictionary = json.loads(quiz_api_request.text)
score = 0

for i in range(len(request_dictionary["results"])):
    given_answers = []
    print(i+1, ".", request_dictionary["results"][i]["question"])
    given_answers = request_dictionary["results"][i]["incorrect_answers"]
    given_answers.insert(random.randint(0,3), request_dictionary["results"][i]["correct_answer"])
    for j in range(len(given_answers)):
        print("\t", j+1, ".",given_answers[j])
    # print(request_dictionary["results"][i]["question"])
    answer = input()
    if answer == request_dictionary["results"][i]["correct_answer"]:
        score += 1

print(f"You have answered {score} correctly")

