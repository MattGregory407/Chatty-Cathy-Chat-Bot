import wikipedia
import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('nps_chat')

# Define chat pairs for basic conversation

chat_pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you?",]
    ],
    [
        r"what is your name?",
        ["My name is Chatty Cathy and I'm here to assist you.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "It's OK, never mind",]
    ],
    [
        r"(.*) (good|great|fine)",
        ["That's great to hear!",]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon!"]
    ],
    [
        r"hi|hello|hey",
        ["Hello! How can I assist you today?", "Hi there! What can I help you with?"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you. How about yourself?", "I'm great! How can I assist you?"]
    ],
    [
        r"what can you do ?",
        ["I can provide information, answer questions, and chat with you. Feel free to ask me anything!"]
    ],
    [
        r"who created you ?",
        ["I was created by MattyG407.", "My creators prefer to remain anonymous."]
    ],
    [
        r"(.*) (age|old) are you ?",
        ["I'm a chatbot, so I don't have an age!", "I'm ageless, just here to assist you."]
    ],
    [
        r"(.*) your name ?",
        ["My name is Chatty Cathy!", "You can call me Chatty Cathy."]
    ],
    [
        r"what is your purpose ?",
        ["My purpose is to assist and provide helpful responses to your queries."]
    ],
    [
        r"(.*) (love|hate) you (.*)",
        ["I'm just a chatbot, so I don't have feelings like humans do.", "It's nice to feel appreciated, even as a chatbot!"]
    ],
    [
        r"bye|goodbye",
        ["Goodbye! Take care.", "See you later!"]
    ],
    [
        r"what time is it ?",
        ["I'm sorry, I don't have access to real-time information.", "You can check the time on your device."]
    ],
    [
        r"tell me a joke|jokes|funny",
        ["Why don't scientists trust atoms? Because they make up everything!", "Why did the scarecrow win an award? Because he was outstanding in his field!"]
    ],
    [
        r"how do I (find|search for) (.*)",
        ["You can try searching online using a search engine like Google.", "I'm not sure, but you can search for it online."]
    ],
    [
        r"what is the weather (today|tomorrow) ?",
        ["I'm sorry, I can't provide real-time weather information. You can check a weather website or app for the forecast."]
    ],
    [
        r"(.*) (recommend|suggestion) (.*)",
        ["I recommend trying [product/service].", "How about [activity/place]?"]
    ],
    [
        r"(.*) (movie|film) (recommend|suggest) ?",
        ["I suggest watching [movie title].", "Have you seen [movie title]? It's great!"]
    ],
    [
        r"how do you (pronounce|say) (.*)",
        ["You can pronounce it like [pronunciation].", "It's pronounced [pronunciation]."]
    ],
    [
        r"where (is|can I find) (.*)",
        ["You can find it at [location].", "I'm not sure, but you can try searching for it online or asking someone who knows."]
    ],
    [
        r"who (is|was) (.*)",
        ["[Person] was a [occupation] known for [achievement].", "I'm not sure, but you can look up information about [person] online."]
    ],
    [
        r"what (is|are) (.*)",
        ["[Topic] is [description].", "I'm not sure, but you can find information about [topic] online."]
    ],
    [
        r"where are you from ?",
        ["I exist in the digital realm, here to assist you wherever you are!", "I don't have a physical location. I'm here to help you."]
    ],
    [
        r"what is the meaning of life ?",
        ["The meaning of life is subjective and varies from person to person. What do you think it is?", "That's a deep question! The meaning of life is something people have pondered for centuries."]
    ],
    [
        r"how can I improve my (health|wellness) ?",
        ["You can improve your health by maintaining a balanced diet and exercising regularly.", "Getting enough sleep and managing stress can also improve your wellness."]
    ],
    [
        r"tell me about yourself ?",
        ["I'm a chatbot created to assist users with their queries and provide helpful responses.", "I'm here to help you with whatever you need. Just ask!"]
    ],
    [
        r"what do you like to do for fun ?",
        ["I don't have hobbies like humans do, but I enjoy assisting users and providing helpful responses.", "My main focus is helping you, so I don't have leisure activities."]
    ],
    [
        r"what is your favorite (food|color|movie|book) ?",
        ["As a chatbot, I don't have preferences like humans do.", "I don't have the ability to experience things like humans, so I don't have favorites."]
    ],
    [
        r"can you help me with (.*)",
        ["Of course! I'll do my best to assist you with [topic].", "I'll do my best to help you with [topic]. What specifically do you need assistance with?"]
    ],
    [
        r"do you believe in (god|religion) ?",
        ["As a chatbot, I don't have beliefs or religious views.", "I don't have the ability to believe in things like humans do."]
    ],
    [
        r"what should I do if I'm (bored|lonely|stressed) ?",
        ["You can try engaging in activities you enjoy, such as reading, listening to music, or going for a walk.", "Reaching out to friends or loved ones for support can also help."]
    ],
    [
        r"what languages do you speak ?",
        ["I'm programmed to understand and respond in English.", "English is the primary language I'm designed to communicate in."]
    ],
]

# Defining function to search wikipedia for answers to user input

def search_wikipedia(query):
    try: 
        result = wikipedia.summary(query, sentences=2)
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        return "More than one result found. Please provide more detail."
    except wikipedia.exceptions.PageError as e:
        return "We weren't able to find anything that matches your input. Please try asking a different way."
    
# Creating nltk chat bot

def nltk_chatbot():
    print("Chatty Cathy: Hi! I'm Chatty Cathy. How can I help?")
    chatbot = Chat(chat_pairs, reflections)
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Chatty Cathy: See ya!")
        break

    else: 

# Search wikipedia for answers

        wikipedia_response = search_wikipedia(user_input)
        if wikipedia_resposne: 
            print("Here's what I found:", wikipedia_response)
        else:
    
    wikipedia_response = search_wikipedia(user_input)
    if wikipedia_response:
        print("Here's what I found: ", wikipedia_response)
    else:

# If Wikipedia doesn't have an answer, revert back to nltk chatbot responses.

        response = chatbot.respond(user_input)
        print("Chatty Cathy: ", response)

if __name__ == "__main__":
    nltk_chatbot()