import re
import random


def message_probability(message, words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts word match
    for word in message:
        if word in words:
            message_certainty += 1

    # Calculates percentage
    percentage = float(message_certainty) / float(len(words))

    for word in required_words:
        if word not in message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    prob_list = {}

    def response(output_response, list_words, single_response=False, required_words=[]):
        prob_list[output_response] = message_probability(message, list_words, single_response, required_words)

    response('Hello!', ['hello', 'hi', 'hey', 'sup'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)

    best_match = max(prob_list, key=prob_list.get)

    return unknown() if prob_list[best_match] < 1 else best_match


def unknown():
    response = ["...",
                "Sorry, I didn't get you.",
                "What does that mean?"][
        random.randrange(3)]
    return response


def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


while True:
    print('Bot: '+get_response(input('You: ')))