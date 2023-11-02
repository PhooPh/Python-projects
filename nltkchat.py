import nltk
from nltk.chat.util import Chat, reflections

pairs = [
[
    r"(.*)My name is(.*)",
    ["Hello , How are you",]
],
[
    r"I'm(.*) good|nice|fine|well|ok",
    ["It nice to hear that", "it cool","It alright",]
],
[
     r"I'm(.*)",
     ["I glad to here that"]
],
[
    r"(hi|hello|hey|hola|Mingalarpar)(.*)",
    ["Hello","Hey there",]
],
[
    r"(.*)student.(.*)",
    ["You do the best","Keep working and stay strong "]
],
[
    r"who(.*) (Myanmar actress | acter)?",
    ["Nay Toe", " Thet Mon Myint"]
],
[
    r"(.*) Season(.*)",
    ["Rain season","Hot season","Winter season", "Spring",]
],
[
    r"(.*)w.w.w",
    ["w.w.w stands for is world-wide-web",]
],

[
    r"(.*)(good moring|Good Moring|Good Evening|good evening|goodnight|Goodnight)",
    ["Have a good day.How can I help you",]
],
[
    r"(.*) What does it mean?",
    [" I'm sorry. Pls tell me exactly what you wanna know about the word meaning.. ",]
],
[
    r"(.*)(Have you had a lunch|Have you had a dinner)(.*)",
    ["Thank you for ask me . I never hungry because I'm robot heehe. ",]
],
[
    r"(.*)Myanmar(.*)",
    ["Myanmar, also known as Burma, is a country located in Southeast Asia. It shares borders with Bangladesh, India, China, Laos, and Thailand. The official name of the country is the Republic of the Union of Myanmar. The capital city is Naypyidaw, while the former capital and largest city is Yangon (also known as Rangoon)."]
],
[
    r"(.*)English Lanuage",
    ["The English language is a West Germanic language that originated in England. It is one of the most widely spoken languages in the world and serves as a global lingua franca, meaning it is used as a common language for communication between people who do not share a native language."]
],
[
    r"(.*)three plus three",
    ["It must be six",]
],
[
    r"(.*)Justin Bieber(.*)",
    ["Justin Bieber is a singer",]
],
[
    r"(.*)Today(.*)",
    ["Thursday,Monday,November 24th",]
],
[
    r"(.*)(asking|ask|asist)(.*)",
    ["yes,How can i help you? And what is this?"]
],
[
    r"(.*)",
    [" Thank you so much for your asking me questions"]
],

[
    r"quit",
    ["Bye Bye .See you soon.Have a  good day"]
],
]
print("Have a good day")
chat = Chat(pairs, reflections)
chat.converse()
