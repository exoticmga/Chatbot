import speech_recognition as sr
import pyttsx3
import random

# Initialize the recognizer and voice engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set the female voice and tone in English
voices = engine.getProperty('voices')
for voice in voices:
    if voice.id == 'en-US-AllisonVoice':
        engine.setProperty('voice', voice.id)
        break

# Define conversation paths
greeting_responses = ["Hello there!", "Hi there! How can I help you today?", "Good day! What can I do for you?"]
farewell_responses = ["Goodbye! Have a nice day!", "Take care! See you soon!", "Have a wonderful day!"]

# Define feedback mechanisms
positive_feedback_responses = ["Thank you for your kind feedback!", "I appreciate your positive words!", "It's nice to know you're satisfied."]
negative_feedback_responses = ["I apologize for the inconvenience. I'll try my best to improve.", "I'm sorry you're not happy with my response. Please let me know how I can do better."]

# Define user testing functions
def greet_user():
    greeting = random.choice(greeting_responses)
    speak(greeting)

def handle_user_input(user_input):
    if user_input.startswith("hello") or user_input.startswith("hi"):
        greet_user()
    elif user_input.startswith("goodbye") or user_input.startswith("bye"):
        farewell = random.choice(farewell_responses)
        speak(farewell)
    elif user_input.startswith("thank you") or user_input.startswith("nice"):
        positive_feedback = random.choice(positive_feedback_responses)
        speak(positive_feedback)
    else:
        negative_feedback = random.choice(negative_feedback_responses)
        speak(negative_feedback)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main chatbot loop
while True:
    try:
        # Record user audio
        with sr.Microphone() as source:
            audio = recognizer.listen(source)

        # Convert audio to text
        user_input = recognizer.recognize_google(audio)

        # Handle user input
        handle_user_input(user_input)
    except sr.UnknownValueError:
        speak("I couldn't understand you. Please try again.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {0}.".format(e))
