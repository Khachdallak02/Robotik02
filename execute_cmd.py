from text_to_speech import robotik_speak
import random
import datetime
from num2words import num2words
from PIL import Image
import time
import os
from config import *
TURN_ON_TEXT = f'Hello master. {ROBOTIK_NAME} just woke up from sleep, how can I help you?'

def execute_cmd(cmd: str):
    try:
        eval(str(cmd))()
    except Exception as e:
        if random.random() > 0.5:
            robotik_speak("Sorry, what?")
        else:
            robotik_speak("Can you please repeat?")

def help():
    text = "I can "
    text += "tell the time, "
    text += "retail hilarious jokes, "
    text += "send random pictures."
    robotik_speak(text)

def time():
    time_now = datetime.datetime.now()
    text = "It's " + num2words(time_now.hour) + " " + num2words(time_now.minute)
    robotik_speak(text)


def joke():
    joke_dictionary = {
        "question" : ['Did you hear about the mathematician who’s afraid of negative numbers?',
                      'Hear about the new restaurant called Karma?',
                      'Why couldn’t the leopard play hide and seek?',
                      'What’s the best thing about Switzerland?',
                      'I invented a new word!',
                      'Did you hear about the mathematician who’s afraid of negative numbers?',
                      'Why do we tell actors to “break a leg?”',
                      'Helvetica and Times New Roman walk into a bar.',
                      'Yesterday I saw a guy spill all his Scrabble letters on the road. I asked him, “What’s the word on the street?”',
                      'Hear about the new restaurant called Karma?',
                      'A woman in labor suddenly shouted, “Shouldn’t! Wouldn’t! Couldn’t! Didn’t! Can’t!”',
                      'A bear walks into a bar and says, “Give me a whiskey and … cola.”',
                      'Did you hear about the actor who fell through the floorboards?',
                      'Did you hear about the claustrophobic astronaut?',
                      'Why did the chicken go to the séance?',      'Where are average things manufactured?',
                      'How do you drown a hipster?',       'What sits at the bottom of the sea and twitches?',
                      'What does a nosy pepper do?', 'Why can’t you explain puns to kleptomaniacs?',
                      'How do you keep a bagel from getting away?',
                      'A man tells his doctor, “Doc, help me. I’m addicted to Twitter!”',
                      'What kind of exercise do lazy people do?', 'Why don’t Calculus majors throw house parties?',
                      'What does Charles Dickens keep in his spice rack?', 'What’s the different between a cat and a comma?',
                      'Why should the number 288 never be mentioned?', 'What did the Tin Man say when he got run over by a steamroller?',
                      'What did the bald man exclaim when he received a comb for a present?',
                      'What did the left eye say to the right eye?', 'What do you call a fake noodle?',
                      'How do you make a tissue dance?', 'What did the 0 say to the 8?',
                      'What do you call a pony with a cough?', 'What do you call a magic dog?',
                      'What did the shark say when he ate the clownfish?', 'What’s orange and sounds like a carrot?',
                      'Why can’t you hear a pterodactyl go to the bathroom?', 'What do you call a woman with one leg?',
                      'Why did the frog take the bus to work today?', 'What did the buffalo say when his son left for college?',
                      'What is an astronaut’s favorite part on a computer?', 'Why did the yogurt go to the art exhibition?',
                      'What do you call an apology written in dots and dashes?', 'Once my dog ate all the Scrabble tiles.',
                      'I told my wife she was drawing her eyebrows too high.',
                      'Did you hear about the two people who stole a calendar?', 'What’s Forest Gump’s password?',
                      'How do poets say hello?', 'Why did the Oreo go to the dentist?',
                      'What do you get from a pampered cow?', 'Why is it annoying to eat next to basketball players?',
                      'What breed of dog can jump higher than buildings?', 'How many times can you subtract 10 from 100?',
                      'Why do bees have sticky hair?', 'How does a rabbi make his coffee?',
                      'I got my daughter a fridge for her birthday.', 'I poured root beer in a square glass.',
                      'Why aren’t koalas actual bears?', 'What do you call a rooster staring at a pile of lettuce?',
                      'Why did the nurse need a red pen at work?', 'How do you throw a space party?',
                      'The numbers 19 and 20 got into a fight.', 'Why did it get so hot in the baseball stadium after the game?',
                      'Why did the math textbook visit the guidance counselor?', 'Why can’t male ants sink?',
                      'Want to hear a construction joke?', 'Talk is cheap?', 'Why did the gym close down?',
                      'I tried to sue the airport for misplacing my luggage.', 'I have a fear of speed bumps.',
                      'Where do you find a cow with no legs?', 'What did one traffic light say to the other?',
                      'What type of sandals do frogs wear?', 'What do you call a boomerang that doesn’t come back?',
                      'What starts with E, ends with E, and has only 1 letter in it?', 'Why doesn’t the sun go to college?',
                      'How do you count cows?', 'Why are skeletons so calm?', 'Did you hear about the kidnapping at school?',
                      'What are shark’s two most favorite words?', 'Can February march?', 'Where does the sheep get his hair cut?',
                      'Why are ghosts such bad liars?', 'Where do fish sleep?', 'How do trees get online?',
                      'What do you call a bear with no teeth?'],
        "answer" : ['He’ll stop at nothing to avoid them.',
                    'There’s no menu: You get what you deserve.',
                    'Because he was always spotted.',
                    'I don’t know, but the flag is a big plus.', 'Plagiarism!', 'He’ll stop at nothing to avoid them.',
                    'Because every play has a cast. Here are some dark jokes to check out if you have a morbid sense of humor.',
                    '“Get out of here!” shouts the bartender. “We don’t serve your type.”',
                    'Once my dog ate all the Scrabble tiles. For days he kept leaving little messages around the house. Don’t miss these hilarious egg puns that will absolutely crack you up.',
                    'There’s no menu: You get what you deserve.',
                    '“Don’t worry,” said the doc. “Those are just contractions.”',
                    '“Why the big pause?” asks the bartender. The bear shrugged. “I’m not sure; I was born with them.”',
                    'He was just going through a stage.', 'He just needed a little space.',
                    'To get to the other side. Check out these other “why did the chicken cross the road?” jokes for more laughs.',
                    'The satisfactory.', 'Throw him in the mainstream.', 'A nervous wreck.', 'Gets jalapeño business!',
                    'They always take things literally.', 'Put lox on it.',
                    'The doctor replies, “Sorry, I don’t follow you …”', 'Diddly-squats.',
                    'Because you should never drink and derive.', 'The best of thymes, the worst of thymes.',
                    'A cat has claws at the end of paws; A comma is a pause at the end of a clause. Don’t forget to bookmark these other “what’s the difference between” jokes that will crack you up.',
                    'It’s two gross.', '“Curses! Foil again!”', 'Thanks— I’ll never part with it!',
                    'Between you and me, something smells.', 'An impasta.', 'Put a little boogie in it.', 'Nice belt!',
                    'A little horse.', 'A labracadabrador.', '', 'A parrot.', 'Because the “P” is silent.', 'Eileen.',
                    'His car got toad away.', 'Bison.', 'The space bar.', 'Because it was cultured.', 'Re-Morse code.',
                    'He kept leaving little messages around the house.', 'She looked at me surprised.',
                    'They each got six months.', '1Forest1.',
                    'Hey, haven’t we metaphor? If you’re a word nerd, here are 20 grammar jokes that are hilarious.',
                    'Because he lost his filling.', 'Spoiled milk.', 'They dribble all the time.',
                    'Any dog, because buildings can’t jump.',
                    'Once. The next time you would be subtracting 10 from 90.', 'Because they use honeycombs.',
                    'Hebrews it.', 'I can’t wait to see her face light up when she opens it.', 'Now I just have beer.',
                    'They don’t meet the koalafications.', 'A chicken sees a salad.',
                    'In case she needed to draw blood.', 'You planet.', '21.', 'All of the fans left.',
                    'It needed help figuring out its problems.', 'They’re buoy-ant.',
                    'Oh never mind, I’m still working on that one.', 'Have you ever talked to a lawyer?',
                    'It just didn’t work out!', 'I lost my case.', 'But I am slowly getting over it.',
                    'Right where you left it.', 'Stop looking! I’m changing!', 'Open-toad!', 'A stick!', 'Envelope.',
                    'Because it has a million degrees!', 'With a cowculator.', 'Because nothing gets under their skin.',
                    '', 'Man overboard!', 'No, but April may.', 'The baa baa shop!', '', 'In the riverbed.',
                    'They just log on!', 'A gummy bear.']

    }
    cnt = len(joke_dictionary['answer'])

    decision = random.randint(0, cnt -1)

    robotik_speak(joke_dictionary['question'][decision])
    robotik_speak(joke_dictionary['answer'][decision])


def picture():
    path = r'reduced_images'
    files = os.listdir(path)
    d = random.choice(files)
    print(d)
    img = Image.open(path + '\\' + d)
    img.show()



def appreciation():
    if random.random() > 0.8:
        robotik_speak("Thank you. It's a great pleasure to be useful.")
    else:
        robotik_speak("Thank you. I am just your creation.")

robotik_speak(TURN_ON_TEXT)