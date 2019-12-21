
from __future__ import print_function

# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, speech, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': speech
        },
        'card': {
            'type': 'Standard',
            'title': title,
            'text': output,
            'image': {
                'smallImageUrl': "https://alexaskillstatetreasures.s3-ap-northeast-1.amazonaws.com/smallmap.png",
                'largeImageUrl': "https://alexaskillstatetreasures.s3-ap-northeast-1.amazonaws.com/bigmap.png"
            }
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText', 
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }

def buyhelp():
    return {
        'version': '1.0',
        'response': {
            "directives": [
                {
                    "type": "Connections.SendRequest",
                    "name": "Buy",
                    "payload": {
                        "InSkillProduct": {
                            "productId": "amzn1.adg.product.d485db2c-7dbc-4cf3-ad3e-16662cae457e"
                        }
                    },
                    "token": "correlationToken"
                }
            ]
        },
        'shouldEndSession': True
    }

def buyresponse(intent_request, session):
    status = intent_request['payload']['purchaseResult']
    if status == "ALREADY_PURCHASED":
        data.accept_no=2
        return accept()
    elif status == "ACCEPTED":
        data.accept_no=1
        return accept()
    elif status == "DECLINED":
        return decline()
    elif status == "ERROR":
        return error()    


def get_welcome_response():
    data.repeat_no=1
    data.help_no=1
    session_attributes = {}
    card_title = "STATE TREASURE"
    card_content = "Your locked in a room."
    speech_output =  "<speak>"\
                     "welcome to the mission commander. You have accepted the mission, and you have the mission's protocol in your hand."\
                     "<audio src='https://alexaskillstatetreasures.s3-ap-northeast-1.amazonaws.com/Map.mp3'/>"\
                     "<audio src='https://alexaskillstatetreasures.s3-ap-northeast-1.amazonaws.com/Map.mp3'/>"\
                     "<audio src='https://alexaskillstatetreasures.s3-ap-northeast-1.amazonaws.com/Fight.mp3'/>"\
                     "You are gently opening your eyes with a little pain in your head, and swelling in your face, "\
                     "trying to remember what happened last night. <break time= '0.5s'/>"\
                     "but all you remember is reading the mission protocol and packing the bag with a knife and map. <break time= '0.5s'/>"\
                     "your slowly getting up with your bag, "\
                     "and you come to know that you have been locked in a room. "\
                     "what would you do? "\
                     "in this mission, you can say repeat, to repeat the content, "\
                     "help me, to get hints, or check my bag, to know the things you have. "\
                     "</speak>"
    reprompt_text =  "start playing by saying, help me or repeat. "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content , speech_output, reprompt_text, should_end_session))
      
def menu():
    return load_game()

def load_game():
    if(data.load_game==0):
        data.repeat_no=0
        session_attributes = {}
        card_title = "STATE TREASURE"
        card_content = "Get back the treasure and\r\n Start your mission Commander."
        speech_output = "<speak>"\
                        "<audio src='https://alexaskillstatetreasures.s3-ap-northeast-1.amazonaws.com/stranger-things-theme-song22.mp3'/>"\
                        "Welcome to state treasures.  "\
                        "Your state's valuable treasure has been stolen. "\
                        "As a Commander of the state, you need to get back the treasures.  "\
                        "The intelligence have sent you the mission's protocal.<break time='1s'/> "\
                        "To start your mission just say, start mission. "\
                        "you can reset your mission by saying reset mission. "\
                        "Good luck commander. "\
                        "</speak>"
        reprompt_text = "commander, say start mission. "
        should_end_session = False
        return build_response(session_attributes, build_speechlet_response(
            card_title, card_content , speech_output, reprompt_text, should_end_session))

    elif(data.load_game==1):
        card_title = "STATE TREASURE"
        card_content = "Elevator lock"
        session_attributes = {}
        should_end_session = False
        data.repeat_no=48
        data.help_no=16
        data.lift_no=0
        data.secret_no=1
        data.key_no=2
        data.knife_no=1
        data.bag_no=1
        speech_output = "<speak>"\
                        "<audio src='https://alexaskillstatetreasures.s3-ap-northeast-1.amazonaws.com/stranger-things-theme-song22.mp3'/>"\
                        "hey commander, happy to have you back. "\
                        "find your state's treasure soon. "\
                        "You are standing infront of the elevator. "\
                        "the second floor's button is missing. "\
                        "You can only go to first floor. "\
                        "you can reset your mission by saying reset mission."\
                        "</speak>"
        reprompt_text = "you can go and explore things."
        return build_response(session_attributes, build_speechlet_response(
            card_title, card_content, speech_output, reprompt_text, should_end_session))
    elif(data.load_game==2):
        card_title = "STATE TREASURE"
        card_content = "Password lock"
        session_attributes = {}
        should_end_session = False
        data.repeat_no=35
        data.help_no=19
        data.room_no=2
        data.lift_no=0
        data.first_no=1      
        data.verify_no=3
        data.secret_no=1
        data.key_no=2
        data.knife_no=1
        data.second_no=1
        data.mag_no=2
        data.bag_no=1
        speech_output = "<speak>"\
                        "<audio src='https://alexaskillstatetreasures.s3-ap-northeast-1.amazonaws.com/stranger-things-theme-song22.mp3'/>"\
                        "welcome back commander. "\
                        "You fight the gaurd, "\
                        "and put his dress as a disguise. "\
                        "You dont find anything in the first floor. "\
                        "you are in the elevator and you have fixed the missing button. "\
                        "what would you do ? "\
                        "you can reset your mission by saying reset mission."\
                        "</speak>"
        reprompt_text = "Say, Go to second floor. "
        return build_response(session_attributes, build_speechlet_response(
            card_title, card_content, speech_output, reprompt_text, should_end_session))
    elif(data.load_game==3):
        card_title = "STATE TREASURE"
        card_content = "Two digit lock"
        session_attributes = {}
        should_end_session = False
        data.repeat_no=41
        data.help_no=25
        data.room_no=2
        data.lift_no=0
        data.first_no=1      
        data.verify_no=4
        data.secret_no=1
        data.key_no=2
        data.knife_no=1
        data.second_no=1
        data.mag_no=2
        speech_output = "<speak>"\
                        "<audio src='https://alexaskillstatetreasures.s3-ap-northeast-1.amazonaws.com/stranger-things-theme-song22.mp3'/>"\
                        "hey commander, you are almost there. "\
                        "You are in the ground floor with the disguise. "\
                        "there, you see a huge dialpad in the floor, "\
                        "and you need to enter a phone number, "\
                        "to go into the secret room. "\
                        "so that, other gaurds believe you. "\
                        "You need to enter the 10 digit phone number. "\
                        "By Saying, the phone number is. "\
                        "</speak>"
        reprompt_text = "Say, the phone number is. "
        return build_response(session_attributes, build_speechlet_response(
            card_title, card_content, speech_output, reprompt_text, should_end_session))
        
def help_me():
    session_attributes = {}
    card_title = "STATE TREASURE"
    card_content = "Help"
    if(data.help_no==1):
        data.repeat_no=2
        speech_output = "<speak>"\
                        "with the help of your radio phone, you try contacting your co-workers. "\
                        "<audio src='https://alexaskillstatetreasures.s3-ap-northeast-1.amazonaws.com/WalkieTalkie.mp3'/>"\
                        "<voice name='Brian'><lang xml:lang='en-GB'>this is tony stark commander, i will be helping you throughout this mission. "\
                        "Explore, and use, are the two words we will be using to make progress in this mission. "\
                        "you must have a knife and a map in your bag. "\
                        "whenever your in need of hints, just say help me. "\
                        "now you can just say, explore map or use knife. "\
                        "thank you.</lang></voice>"\
                        "</speak>"
    elif(data.help_no==2):
        data.repeat_no=2
        speech_output = "<speak>"\
                        "<voice name='Brian'><lang xml:lang='en-GB'>Explore the room by Saying, Explore Room.</lang></voice>"\
                        "</speak>"
    elif(data.help_no==3):
        data.repeat_no=2
        speech_output = "<speak><voice name='Brian'><lang xml:lang='en-GB'> Say, Explore map commander.</lang></voice> </speak>"    
    elif(data.help_no==4):
        data.repeat_no=2
        speech_output = "<speak>"\
                        "<voice name='Brian'><lang xml:lang='en-GB'>try Exploring the things in the room. "\
                        "you might find some clues to escape the room. "\
                        "to explore,you can say the word explore with the thing name.  "\
                        "for example, you can say explore inverted painting. </lang></voice> "\
                        "</speak>"
    elif(data.help_no==5):
        data.repeat_no=2
        speech_output = "<speak>"\
                        "<voice name='Brian'><lang xml:lang='en-GB'> Think about the number lock.</lang></voice> "\
                        "</speak>"
    elif(data.help_no==6):
        data.repeat_no=2
        speech_output = "<speak>"\
                        "<voice name='Brian'><lang xml:lang='en-GB'>try to you get some clue from the painting commander. </lang></voice>"\
                        "</speak>"
    elif(data.help_no==7):
        data.repeat_no=2
        if(data.secret_no==0):
            speech_output = "<speak>"\
                            "<voice name='Brian'><lang xml:lang='en-GB'>Find a written letter to get some clues. </lang></voice>"\
                            "</speak>"
        elif(data.secret_no==1):
            speech_output = "<speak>"\
                            "<voice name='Brian'><lang xml:lang='en-GB'>Every beginning make up to something. </lang></voice>"\
                            "</speak>"
    elif(data.help_no==8):
        data.repeat_no=2
        speech_output = "<speak><voice name='Brian'><lang xml:lang='en-GB'> say, use key. </lang></voice></speak>"
    elif(data.help_no==9):
        data.repeat_no=2
        speech_output = "<speak><voice name='Brian'><lang xml:lang='en-GB'>get your clues from the letter.</lang></voice></speak> "   
    elif(data.help_no==10):
        data.repeat_no=2
        speech_output = "<speak><voice name='Brian'><lang xml:lang='en-GB'>The clue is in the painting.</lang></voice></speak> "          
    elif(data.help_no==11):
        data.repeat_no=2
        speech_output = "<speak><voice name='Brian'><lang xml:lang='en-GB'>Use them to find, fingerprints in the lockers.</lang></voice></speak> "
    elif(data.help_no==12):
        data.repeat_no=2
        speech_output = "<speak><voice name='Brian'><lang xml:lang='en-GB'>Use letter as a clue in the word lock.</lang></voice></speak> "
    elif(data.help_no==13):
        data.repeat_no=2
        speech_output = "<speak><voice name='Brian'><lang xml:lang='en-GB'>There is no need of magnifying glass here.</lang></voice></speak> "
    elif(data.help_no==14):
        data.repeat_no=2
        speech_output = "<speak><voice name='Brian'><lang xml:lang='en-GB'>Use the key to escape the room commander.</lang></voice></speak> "   
    elif(data.help_no==15):
        data.repeat_no=2
        speech_output = "<speak><voice name='Brian'><lang xml:lang='en-GB'>When alphabets becomes numbers.</lang></voice></speak> "    
    elif(data.help_no==16):
        data.repeat_no=2
        speech_output = "<speak><voice name='Brian'><lang xml:lang='en-GB'>Just say, go to second or first floor.</lang></voice></speak> " 
    elif(data.help_no==17):
        data.repeat_no=2
        speech_output = "<speak><voice name='Brian'><lang xml:lang='en-GB'>Check your bag.</lang></voice></speak> "    
    elif(data.accept_no==1 or data.accept_no==2):
        if(data.help_no==18):
            data.repeat_no=2
            if(data.room_no==0):
                speech_output = "<speak><voice name='Brian'><lang xml:lang='en-GB'>"\
                                "Think about the things you have. "\
                                "</lang></voice></speak>"
            elif(data.room_no==1):
                speech_output = "<speak><voice name='Brian'><lang xml:lang='en-GB'>"\
                                "The olden people never know, "\
                                "how to make a signature."\
                                "</lang></voice></speak>"
            elif(data.room_no==2):
                speech_output = "<speak><voice name='Brian'><lang xml:lang='en-GB'>Explore some other things.</lang></voice></speak> "
        elif(data.help_no==19):
            data.repeat_no=2
            speech_output = "<speak><voice name='Brian'><lang xml:lang='en-GB'>Think about the second floor.</lang></voice></speak> "
        elif(data.help_no==20):
            data.repeat_no=2
            speech_output = "<speak><voice name='Brian'><lang xml:lang='en-GB'>"\
                            "You know the starting number as seven, "\
                            "Make operations on the previous number locks."\
                            "</lang></voice></speak>"
        elif(data.help_no==21):
            data.repeat_no=2
            speech_output = "<speak><voice name='Brian'><lang xml:lang='en-GB'>Explore the things in the room to get some clue."\
                            " you can say, explore book.</lang></voice></speak> "                    
        elif(data.help_no==22):
            data.repeat_no=2
            speech_output = "<speak><voice name='Brian'><lang xml:lang='en-GB'>note these pattern for future use.</lang></voice></speak> " 
        elif(data.help_no==23):
            data.repeat_no=2
            speech_output = "<speak><voice name='Brian'><lang xml:lang='en-GB'>Have you ever played connections word game?</lang></voice></speak> "     
        elif(data.help_no==24):
            data.repeat_no=2
            speech_output = "<speak><voice name='Brian'><lang xml:lang='en-GB'>"\
                            "play connections with the paintings, and "\
                            "find the two numbers. "\
                            "</lang></voice></speak>"
        elif(data.help_no==25):
            data.repeat_no=2
            speech_output = "<speak><voice name='Brian'><lang xml:lang='en-GB'>"\
                            "Page numbers will help you to find the Phone number. "\
                            "note that you need to have ten digits for the phone number. "\
                            "</lang></voice></speak>"
        elif(data.help_no==26):
            data.repeat_no=2
            speech_output = "<speak><voice name='Brian'><lang xml:lang='en-GB'>darker the sky, brighter the moon is. </lang></voice></speak> "  
        elif(data.help_no==27):
            data.repeat_no=2
            speech_output = "<speak><voice name='Brian'><lang xml:lang='en-GB'>Try checking your bag.</lang></voice></speak> "
        elif(data.help_no==28):
            data.repeat_no=2
            speech_output = "<speak><voice name='Brian'><lang xml:lang='en-GB'>say, go to first floor.</lang></voice></speak> "
        elif(data.help_no==29):
            data.repeat_no=2
            speech_output = "<speak><voice name='Brian'><lang xml:lang='en-GB'>"\
                            "Guess the password. "\
                            "Find the relation between "\
                            "the previous lock passwords. "\
                            "</lang></voice></speak>"
        elif(data.help_no==30):
            data.repeat_no=2
            speech_output = "<speak><voice name='Brian'><lang xml:lang='en-GB'>"\
                            "The final sentence contains four words, that are hidden in the message ! "\
                            "Find it to get the treasure commander. "\
                            "</lang></voice></speak>"
        elif(data.help_no==31):
            data.repeat_no=2
            speech_output = "<speak><voice name='Brian'><lang xml:lang='en-GB'>try to explore the room lock.</lang></voice></speak>"
    elif(data.buy_help==1):
        data.repeat_no=2
        speech_output = "<speak><voice name='Brian'><lang xml:lang='en-GB'>you can get more hints, "\
                        " by saying, buy hints, or buy help </lang></voice></speak>"
        
    reprompt_text = "Think something and escape commander. "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))   
        
def repeat():
    if(data.repeat_no==0):
        return menu()
    elif(data.repeat_no==1):
        return get_welcome_response()
    elif(data.repeat_no==2):
        return help_me()
    elif(data.repeat_no==3):
        return explore_map()
    elif(data.repeat_no==5):
        return explore_knife()
    elif(data.repeat_no==7):
        return explore_room()    
    elif(data.repeat_no==9):
        return explore_invimg() 
    elif(data.repeat_no==11):
        return explore_numlock()   
    elif(data.repeat_no==13):
        return explore_wordlock()   
    elif(data.repeat_no==15):
        return explore_maindoor()   
    elif(data.repeat_no==17):
        card_title = "STATE TREASURE"
        card_content = "Number Lock"
        session_attributes = {}
        should_end_session = False
        speech_output = "<speak>"\
                        "8 0 6 1,is the correct key and the lock is opened. " \
                        "You find, a magnifying glass, and a letter."\
                        "</speak>"
        reprompt_text = "you can explore these things."
        
        return build_response(session_attributes, build_speechlet_response(
            card_title, card_content, speech_output, reprompt_text, should_end_session)) 
    elif(data.repeat_no==18):
        card_title = "STATE TREASURE"
        card_content = "Number Lock"
        session_attributes = {}
        should_end_session = False 
        speech_output = "<speak>"\
                        "The key is incorrect. "\
                        "Please try again."\
                        "</speak>"
        reprompt_text = "Say, the four digits are. "
        return build_response(session_attributes, build_speechlet_response(
            card_title, card_content, speech_output, reprompt_text, should_end_session)) 
    elif(data.repeat_no==21):
        return explore_magglass()
    elif(data.repeat_no==23):
        return explore_letter()        
    elif(data.repeat_no==25):
        return use_mag() 
    elif(data.repeat_no==27):
        card_title = "STATE TREASURE"
        card_content = "Number Lock"
        session_attributes = {}
        should_end_session = False
        speech_output = "<speak>"\
                        "The word is correct. "\
                        "You find a key to open the main door, "\
                        "and a code as P, U, N "\
                        "</speak>"
        reprompt_text = "use the clues properly."
        
        return build_response(session_attributes, build_speechlet_response(
            card_title, card_content, speech_output, reprompt_text, should_end_session)) 
    elif(data.repeat_no==28):
        card_title = "STATE TREASURE"
        card_content = "Number Lock"
        session_attributes = {}
        should_end_session = False 
        speech_output = "<speak>"\
                        "The word is incorrect. "\
                        "Please try again."\
                        "</speak>"
        reprompt_text = "Say, the word is. "
        
        return build_response(session_attributes, build_speechlet_response(
            card_title, card_content, speech_output, reprompt_text, should_end_session))
    elif(data.repeat_no==30):
        return use_key() 
    elif(data.repeat_no==31):
        card_title = "STATE TREASURE"
        card_content = "Elevator lock"
        session_attributes = {}
        should_end_session = False
        speech_output = "<speak>"\
                        "<audio src='https://alexaskillstatetreasures.s3-ap-northeast-1.amazonaws.com/Ding.mp3'/>"\
                        "7 3 5, "\
                        "You are inside the elevator and you find "\
                        "that the button which leads you to the second floor is missing. "\
                        "You can only go to the first floor, "\
                        "And Your mission progress is saved commander."\
                        "</speak>"
        reprompt_text = "you can go and explore things."                
        return build_response(session_attributes, build_speechlet_response(
            card_title, card_content, speech_output, reprompt_text, should_end_session))
    elif(data.repeat_no==32):
        card_title = "STATE TREASURE"
        card_content = "Elevator lock"
        session_attributes = {}
        should_end_session = False
        speech_output = "<speak>"\
                        "The key is incorrect. "\
                        "Please try again."\
                        "</speak>"
        reprompt_text = "Say, the four digits are. "
        return build_response(session_attributes, build_speechlet_response(
            card_title, card_content, speech_output, reprompt_text, should_end_session))
    elif(data.repeat_no==33):
        return first_floor()     
    elif(data.repeat_no==34):
        return explore_room_lock() 
    elif(data.repeat_no==35):
        card_title = "STATE TREASURE"
        card_content = "Password lock"
        session_attributes = {}
        should_end_session = False
        speech_output = "<speak>"\
                        "7 3 2 6, is the correct key ! " \
                        "<audio src='https://alexaskillstatetreasures.s3-ap-northeast-1.amazonaws.com/Punch.mp3'/>"\
                        "You fight the gaurd, "\
                        "and put his dress as a disguise. "\
                        "You dont find anything in the first floor. "\
                        "you are in the elevator and you have fixed the missing button. "\
                        "what would you do ? "\
                        "your game progress is saved. "\
                        "</speak>"
        reprompt_text = "Say,Go to second floor. "
        return build_response(session_attributes, build_speechlet_response(
            card_title, card_content, speech_output, reprompt_text, should_end_session))
    elif(data.repeat_no==36):
        card_title = "STATE TREASURE"
        card_content = "Password lock"
        session_attributes = {}
        should_end_session = False
        speech_output = "<speak>"\
                        "The password is incorrect. "\
                        "Please try again."\
                        "</speak>"
        reprompt_text = "Say, the four digits are. "
        return build_response(session_attributes, build_speechlet_response(
            card_title, card_content, speech_output, reprompt_text, should_end_session))
    elif(data.repeat_no==37):
        return second_floor()         
    elif(data.repeat_no==38):
        return explore_book()     
    elif(data.repeat_no==39):
        return wall_paint()     
    elif(data.repeat_no==40):
        return explore_closet() 
    elif(data.repeat_no==41):
        card_title = "STATE TREASURE"
        card_content = "Two digit lock"
        session_attributes = {}
        should_end_session = False
        speech_output = "<speak>"\
                        "The key is correct and you are in the ground "\
                        "floor with the gaurds costume. "\
                        "there, you see a huge dialpad in the floor, "\
                        "and you need to enter a phone number, "\
                        "to go into the secret room. "\
                        "so that, other gaurds believe you. "\
                        "You need to enter the 10 digit phone number. "\
                        "By Saying, the phone number is. "\
                        "</speak>"
        reprompt_text = "Say, the phone number is. "
        return build_response(session_attributes, build_speechlet_response(
            card_title, card_content, speech_output, reprompt_text, should_end_session))
    elif(data.repeat_no==42):
        card_title = "STATE TREASURE"
        card_content = "Two digit lock"
        session_attributes = {}
        should_end_session = False
        speech_output = "<speak>"\
                        "<audio src='https://alexaskillstatetreasures.s3-ap-northeast-1.amazonaws.com/PhoneDial.mp3'/>"\
                        "The phone rings, and the officer opens the gate for you. "\
                        "now, You find yourself inside a secret room, "\
                        "completely empty "\
                        "with just a single paper on the floor. "\
                        "you find, the paper has nothing written on it. "\
                        "What would you do? "\
                        "</speak>"
        reprompt_text = "Say something. "
        return build_response(session_attributes, build_speechlet_response(
            card_title, card_content, speech_output, reprompt_text, should_end_session)) 
    elif(data.repeat_no==43): 
        card_title = "STATE TREASURE"
        card_content = "Two digit lock"
        session_attributes = {}
        should_end_session = False
        speech_output = "<speak>"\
                        "The number is incorrect. "\
                        "Please try again."\
                        "</speak>"
        reprompt_text = "Say, the phone number is. "
        return build_response(session_attributes, build_speechlet_response(
            card_title, card_content, speech_output, reprompt_text, should_end_session))
    elif(data.repeat_no==44):
        return explore_elevator()
    elif(data.repeat_no==45):
        return light_off()
    elif(data.repeat_no==46):
        return explore_paper()
    elif(data.repeat_no==47):
        return explore_bag()  
    elif(data.repeat_no==48):
        card_title = "STATE TREASURE"
        card_content = "Elevator lock"
        session_attributes = {}
        should_end_session = False
        speech_output = "<speak>"\
                        "<audio src='https://alexaskillstatetreasures.s3-ap-northeast-1.amazonaws.com/stranger-things-theme-song22.mp3'/>"\
                        "<voice name='Brian'><lang xml:lang='en-GB'>hey commander, happy to have you back. "\
                        "find your state's treasure soon. "\
                        "You are standing infront of the elevator. "\
                        "the second floor's button is missing. "\
                        "You can only go to first floor. "\
                        "you can reset your mission by saying reset mission."\
                        "</lang></voice></speak>"
        reprompt_text = "you can go and explore things."
        return build_response(session_attributes, build_speechlet_response(
            card_title, card_content, speech_output, reprompt_text, should_end_session))
        
        
def explore_map():
    data.repeat_no=3
    session_attributes = {}
    card_title = "STATE TREASURE"
    card_content = "Map"
    if(data.verify_no==0):
        data.help_no=2
        speech_output = "<speak>"\
                        "<audio src='https://alexaskillstatetreasures.s3-ap-northeast-1.amazonaws.com/Map.mp3'/>"\
                        "<voice name='Justin'><lang xml:lang='en-US'> hi, i am map. "\
                        "yes, i can speak to you. "\
                        "i will tell your location, and also sometimes "\
                        "i will help you to make the next move. "\
                        "you are locked in the third floor, "\
                        "and the treasure you need to find, is in the ground floor. "\
                        "try to Get out of the room by finding clues. "\
                        "say explore map, to hear me again. "\
                        "now, start exploring the room.</lang></voice>"\
                        "</speak>"
    elif(data.verify_no==1):
        speech_output = "<speak>"\
                        "<audio src='https://alexaskillstatetreasures.s3-ap-northeast-1.amazonaws.com/Map.mp3'/>"\
                        "<voice name='Justin'><lang xml:lang='en-US'>hey commander. did you really escape the room. "\
                        "now, You are in front of the lift. "\
                        "go to first or second floor. "\
                        "bye commander.</lang></voice> "\
                        "</speak>"
    elif(data.verify_no==2):
        speech_output = "<speak>"\
                        "<audio src='https://alexaskillstatetreasures.s3-ap-northeast-1.amazonaws.com/Map.mp3'/>"\
                        "<voice name='Justin'><lang xml:lang='en-US'>hey commander. you are in the first floor. "\
                        "and your hands are tied, "\
                        "get out of the room and "\
                        "go to second floor. "\
                        "bye commander. love you. </lang></voice> "\
                        "</speak>"                    
    elif(data.verify_no==3):
        speech_output = "<speak>"\
                        "<audio src='https://alexaskillstatetreasures.s3-ap-northeast-1.amazonaws.com/Map.mp3'/>"\
                        "<voice name='Justin'><lang xml:lang='en-US'>hey commander, your in the second floor, "\
                        "the closet in this room will lead you to the treasure. "\
                        "but you need to find clues to escape."\
                        "</lang></voice></speak>"
    else:
        speech_output = "<speak>"\
                        "<audio src='https://alexaskillstatetreasures.s3-ap-northeast-1.amazonaws.com/Map.mp3'/>"\
                        "<voice name='Justin'><lang xml:lang='en-US'>"\
                        "i dont know where you are commander. "\
                        "</lang></voice></speak>"
        
    reprompt_text = "Say something."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content , speech_output, reprompt_text, should_end_session))

def explore_bag():
    data.repeat_no=47
    session_attributes = {}
    card_title = "STATE TREASURE"
    card_content = "Bag"
    if(data.bag_no==0):
        speech_output = "<speak><audio src='https://alexaskillstatetreasures.s3-ap-northeast-1.amazonaws.com/BagSound.mp3'/>You have a knife and a map.</speak>"
    elif(data.bag_no==1):
        speech_output = "<speak><audio src='https://alexaskillstatetreasures.s3-ap-northeast-1.amazonaws.com/BagSound.mp3'/>you have a knife, map, magnifying glass and a letter.</speak> "
    elif(data.bag_no==2):
        speech_output = "<speak>"\
                        "<audio src='https://alexaskillstatetreasures.s3-ap-northeast-1.amazonaws.com/BagSound.mp3'/>"\
                        "you have a knife, map, magnifying glass, "\
                        "paper and a letter. "\
                        "</speak>"
    else:
        return help_me()
    reprompt_text = "Use these things when needed. "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))        

def explore_knife():
    data.repeat_no=5
    session_attributes = {}
    card_title = "STATE TREASURE"
    card_content = "Knife"
    if(data.knife_no==0):
        speech_output = "<speak>"\
                        "<audio src='https://alexaskillstatetreasures.s3-ap-northeast-1.amazonaws.com/Knife.mp3'/>"\
                        "it seems to be a normal steel knife. "\
                        "use them, when needed."\
                        "</speak>"
    elif(data.knife_no==1):
        speech_output = "<speak>"\
                        "You cannot use the knife right now. "\
                        "Try some time later. "\
                        "</speak>"
    elif(data.knife_no==2):
        data.help_no=31
        data.password_no=2
        speech_output = "<speak>"\
                        "<audio src='https://alexaskillstatetreasures.s3-ap-northeast-1.amazonaws.com/Knife.mp3'/>"\
                        "<audio src='https://alexaskillstatetreasures.s3-ap-northeast-1.amazonaws.com/ropecut.mp3'/>"\
                        "you have cut the rope successfully. "\
                        "now you are searching for the button all around the room, "\
                        "and you finally find the second floor's on the side of the cupboard. "\
                        "but, your still locked inside the room. "\
                        "</speak>"
        data.lift_no=3                
        data.second_no=1
        data.room_no=1
    else:
        speech_output = "<speak>"\
                        "You cannot use the knife right now. "\
                        "Try some time later. "\
                        "</speak>"
    reprompt_text = "Explore something or ask help. "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))
        
def explore_room():
    data.repeat_no=7
    session_attributes = {}
    card_title = "STATE TREASURE"
    card_content = "Explore Room"
    if(data.verify_no==0):
        data.help_no=4
        data.knife_no=1
        speech_output = "<speak>"\
                        "By exploring the room, "\
                        "You find an inverted painting on the wall, "\
                        "A word lock and a number lock in the table. "\
                        "and a main door to escape the room. "\
                        "What would you do? "\
                        "</speak>"
    elif(data.verify_no==1):
        data.help_no=27
        speech_output = "<speak>you are already out of the First room.</speak>"
        data.knife_no=2
    elif(data.verify_no==2):
        data.help_no=27
        speech_output = "<speak>The room is totally empty, you just find a room lock in the door.</speak>"
        data.knife_no=2    
    elif(data.verify_no==3):
        speech_output = "<speak>"\
                        "In this floor, you find a room, "\
                        "which will directly lead you to the ground floor, "\
                        "where you can find the state's treasure and escape. "\
                        "you walk around and find that, the room has a book, two wall paintings, and a closet. "\
                        "You can explore any of these things! "\
                        "</speak>"
    else:
        speech_output = "<speak>you are already out of the First room.</speak>"
    reprompt_text = "start Exploring things around you."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))

def explore_invimg():
    data.repeat_no=9
    session_attributes = {}
    card_title = "STATE TREASURE"
    card_content = "Explore Inverted Image"
    if(data.verify_no==0):
        data.help_no=5
        speech_output = "<speak>"\
                        "you find that, "\
                        "the year it was painted as 1908. "\
                        "</speak>"
    elif(data.verify_no==1):
        data.help_no=27
        speech_output = "<speak>You don't find any inverted painting.</speak>"
    elif(data.verify_no==2):
        data.help_no=27
        speech_output = "<speak>You don't find any inverted painting.</speak>"
    elif(data.verify_no==3):
        return wall_paint()
    else:
        speech_output = "<speak>You don't find any inverted painting.</speak>"
    reprompt_text = "Use this as a clue."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))       
        
def explore_numlock():
    data.repeat_no=11
    session_attributes = {}
    card_title = "STATE TREASURE"
    card_content = "Explore Number lock"
    if(data.verify_no==0):
        data.help_no=6
        speech_output = "<speak>tell me a four digit number to unlock.</speak> "
    elif(data.verify_no==1):
        data.help_no=27
        speech_output = "<speak>You don't find any number lock.</speak> "
    else:
        speech_output = "<speak>You don't find any number lock.</speak> "
    reprompt_text = "say, the four digit are."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))
        
def explore_wordlock():
    data.repeat_no=13
    session_attributes = {}
    card_title = "STATE TREASURE"
    card_content = "Explore Word lock"
    if(data.verify_no==0):
        data.help_no=7
        speech_output = "<speak>"\
                        "pronounce a single word to unlock. say the command, "\
                        "the secret word is. "\
                        "</speak>"
    elif(data.verify_no==1):
        data.help_no=27
        speech_output = "<speak>You don't find any word lock.</speak>"
    else:
        speech_output = "<speak>You don't find any word lock.</speak>"
    reprompt_text = "say,the word is. "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))  
        
def explore_maindoor():
    data.repeat_no=15
    session_attributes = {}
    card_title = "STATE TREASURE"
    card_content = "Explore Main door"
    if(data.verify_no==0):
        data.help_no=8
        speech_output = "<speak>Use key to open the door.</speak> "
    elif(data.verify_no==1):
        data.help_no=27
        speech_output = "<speak>You don't find any main door.</speak>"
    else:
        speech_output = "<speak>You don't find any main door.</speak>"
    reprompt_text = "find the key "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))  

def explore_magglass():
    data.repeat_no=21
    data.help_no=11
    session_attributes = {}
    card_title = "STATE TREASURE"
    card_content = "Magnifying Glass"
    speech_output = "<speak>"\
                    "A normal magnifying glass, "\
                    "Use them when needed."\
                    "</speak>"
    reprompt_text = "Use them to find fingerprints. "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session)) 

def explore_letter():
    data.repeat_no=23
    session_attributes = {}
    card_title = "STATE TREASURE"
    card_content = "Explore Letter"
    if(data.verify_no==0):
        data.help_no=12
        data.secret_no=1
        speech_output = "<speak>"\
                        "<audio src='https://alexaskillstatetreasures.s3-ap-northeast-1.amazonaws.com/Letteropen.mp3'/>"\
                        "you open the letter, and you find this sentence, "\
                        "Hello, i totally surrender. "\
                        "</speak>"
    elif(data.verify_no==1):
        data.help_no=27
        speech_output = "<speak>You don't find a letter.</speak> "
    else:
        speech_output = "<speak>You don't find a letter.</speak> "
    reprompt_text = "Use these as clues. "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session)) 
        
def use_mag():
    data.repeat_no=25
    session_attributes = {}
    card_title = "STATE TREASURE"
    card_content = "Magnifying glass"
    if(data.mag_no==0):
        speech_output = "<speak>You cannot use the magnifying glass now.</speak> "
    elif(data.mag_no==1):
        speech_output = "<speak>you can use</speak>"
    elif(data.mag_no==2):
        data.help_no=29
        speech_output = "<speak>you examine the digital lock with the magnifying glass,"\
                        "and find the fingerprint in the numbers, 6, 3, 7 and 2 .</speak>"
    else:
        return help_me()
    reprompt_text = "Use them in right situation"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session)) 

def explore_room_lock():
    data.repeat_no=34
    data.help_no=18
    session_attributes = {}
    card_title = "STATE TREASURE"
    card_content = "Room lock"
    if(data.room_no==0):
        speech_output = "<speak>Your tied commander. Try doing something else.</speak> "
        reprompt_text = "You are tied."
    elif(data.room_no==1):
        data.knife_no=1 
        speech_output = "<speak>"\
                        "you find it as a four digit digital lock. "\
                        "tell the four digits to escape the room. "\
                        "what will you do to find the numbers ?"\
                        "</speak>"
        data.mag_no=2
        reprompt_text = "Think to find the three numbers."
    elif(data.room_no==2):
        speech_output = "<speak>There is no room lock.</speak> "
        reprompt_text = "Think something."
    else:
        speech_output = "<speak>There is no room lock.</speak> "
        reprompt_text = "Think something."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session)) 
            
        
def first_floor():
    data.repeat_no=33
    session_attributes = {}
    card_title = "STATE TREASURE"
    card_content = "First floor"
    if(data.lift_no==3):
        speech_output = "<speak>You are not in the elevator!</speak> "
        reprompt_text = "Think! "
    elif(data.first_no==0):
        data.help_no=17
        data.knife_no=2
        data.verify_no=2
        speech_output = "<speak>"\
                        "<audio src='https://alexaskillstatetreasures.s3-ap-northeast-1.amazonaws.com/Ding.mp3'/>"\
                        "A six feet tall guy walking there, notices you and "\
                        "ties you with a thick rope. Then he drags you in the floor and locks you in the store room. "\
                        "with your hands tied, you slowly crawl the floor, and hear the starting number in the room lock as. "\
                        "<amazon:effect name='whispered'> Seven.</amazon:effect> "\
                        "What will you do? "\
                        "</speak>"
        reprompt_text = "Think think."                
        
    elif(data.first_no==1):
        data.help_no=19
        speech_output = "<speak>"\
                        "<audio src='https://alexaskillstatetreasures.s3-ap-northeast-1.amazonaws.com/Ding.mp3'/>"\
                        "You find nothing in the first floor. "\
                        "your again inside the elevator. "\
                        "</speak>"
    
        reprompt_text = "Try second floor."
    else:
        return help_me()
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))  
        
def second_floor():
    data.repeat_no=37
    session_attributes = {}
    card_title = "STATE TREASURE"
    card_content = "Second floor"
    if(data.lift_no==3):
        speech_output = "<speak>You are not in the elevator!</speak> "
        reprompt_text = "Think! "
    elif(data.second_no==0):
        data.help_no=28
        speech_output = "<speak>second floor's button is missing. you cannot go to the second floor. find the button commander</speak> "
        reprompt_text = "What do you explore?"
    elif(data.second_no==1):
        data.help_no=21
        data.verify_no=3
        speech_output = "<speak>"\
                        "<audio src='https://alexaskillstatetreasures.s3-ap-northeast-1.amazonaws.com/Ding.mp3'/>"\
                        "In this floor, you find a room, "\
                        "which will directly lead you to the ground floor, "\
                        "where you can find the state's treasure and escape. "\
                        "you walk around and find that, the room has a book, two wall paintings, and a closet. "\
                        "You can explore any of these things! "\
                        "</speak>"
        reprompt_text = "start exploring. "                
    else:
        return help_me()
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session)) 
        
def explore_book():
    data.repeat_no=38
    session_attributes = {}
    card_title = "STATE TREASURE"
    card_content = "Explore Book"
    if(data.verify_no==3):
        data.help_no=22
        speech_output = "<speak>"\
                        "<audio src='https://alexaskillstatetreasures.s3-ap-northeast-1.amazonaws.com/Book.mp3'/>"\
                        "the book name is, In search of lost time, "\
                        "and you find the page numbers "\
                        "as, 18, 24, 26, 32, 35, 40, 43, 51, 56. "\
                        "</speak>"
        reprompt_text = "Note the patterns. "
    elif(data.verify_no==4):
        speech_output = "<speak>You dont have a book!</speak> "
        reprompt_text = "Try something else. "
    else:
        speech_output = "<speak>You dont have a book!</speak> "
        reprompt_text = "Try something else. "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session)) 
        
def wall_paint():
    data.repeat_no=39
    session_attributes = {}
    card_title = "STATE TREASURE"
    card_content = "Explore Wall painting"
    if(data.verify_no==3):
        data.help_no=23
        speech_output = "<speak>"\
                        "You see a painting of an yellow "\
                        " Auto on the left portion of the wall, "\
                        "and painting of an iphone on the right side. "\
                        "what would you do?"\
                        "</speak>"
        reprompt_text = "Try to get a single word. "
    elif(data.verify_no==4):
        speech_output = "<speak>There is no wall painting.</speak> "
        reprompt_text = "Try something else. "
    else:
        speech_output = "<speak>There is no wall painting.</speak> "
        reprompt_text = "Try something else. "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))        
        
def explore_closet():
    data.repeat_no=40
    session_attributes = {}
    card_title = "STATE TREASURE"
    card_content = "Explore Closet"
    if(data.verify_no==3):
        data.help_no=24
        data.password_no=3
        speech_output = "<speak>"\
                        "<audio src='https://alexaskillstatetreasures.s3-ap-northeast-1.amazonaws.com/CupBoard.mp3'/>"\
                        "You find alot of cloths, "\
                        "beside which you find a secret door, "\
                        "which will lead you to the ground floor directly. "\
                        "But it has a two digit password. "\
                        "tell the two digit to unlock."\
                        "</speak>"
                
        reprompt_text = "say, the two digits are. "
    elif(data.verify_no==4):
        speech_output = "<speak>No closet found.</speak> "
        reprompt_text = "Try something else. "
    else:
        speech_output = "<speak>No closet found.</speak> "
        reprompt_text = "Try something else. "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))         

def use_key():
    data.repeat_no=30
    session_attributes = {}
    card_title="STATE TREASURE"
    card_content = "Use Key"
    if(data.key_no==0):
        data.help_no=15
        speech_output = "<speak>you dont have the key.</speak> "
    elif(data.key_no==1):
        data.help_no=15
        data.verify_no=1
        data.password_no=1
        speech_output = "<speak>"\
        "<audio src='https://alexaskillstatetreasures.s3-ap-northeast-1.amazonaws.com/DoorEffects.mp3'/>"\
        "You have escaped the room commander.<break time='1s'/> "\
        "Now, you find an old elevator locked, "\
        "with three digits. "\
        "tell the three digits to unlock. "\
        "</speak>"
    elif(data.key_no==2):
        speech_output = "<speak>you cannot use the key.</speak> "
    else:
        speech_output = "<speak>you cannot use the key.</speak> "
    reprompt_text = "Use them in right situation"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))
        
def explore_elevator():
    data.repeat_no=44
    data.help_no=15
    session_attributes = {}
    card_title="STATE TREASURE"
    card_content = "Explore Elevator"
    speech_output = "<speak>"\
                    "You find a elevator, locked. "\
                    "with a three digit number. "\
                    "say, the elevator lock is. "\
                    "</speak>"
    reprompt_text = "Use them in right situation"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))   
        
def light_off():
    data.repeat_no=45
    if(data.light_no==0):
        data.help_no=30
        session_attributes = {}
        card_title = "STATE TREASURE"
        card_content = "Light...??"
        speech_output = "<speak>"\
                        "Cannot recognize it. "\
                        "</speak>"
        reprompt_text = "something else. "
        should_end_session = False
        return build_response(session_attributes, build_speechlet_response(
            card_title, card_content, speech_output, reprompt_text, should_end_session))
    elif(data.light_no==1):
        data.help_no=30
        session_attributes = {}
        card_title = "STATE TREASURE"
        card_content = "Turn off Light"
        speech_output = "<speak>"\
                    "<say-as interpret-as='interjection'>abracadabra!</say-as>"\
                    "The lights are turned off. "\
                    "The secret message in the paper slowly appears to be, "\
                    "<voice name='Raveena'><lang xml:lang='en-IN'>"\
                    "Obviously, a man will slip the coolest beer ! "\
                    "</lang></voice>"\
                    "now you have to say the final words and get the treasure."\
                    "</speak>"
        reprompt_text = "Say the final words. "
        should_end_session = False
        return build_response(session_attributes, build_speechlet_response(
            card_title, card_content, speech_output, reprompt_text, should_end_session))
 
     
        
def handle_session_end_request():
    card_title = "STATE TREASURE"
    card_content = "Session Ended"
    speech_output = "<speak>"\
                    "Thank you for the mission commander. Have a nice day."\
                    "</speak>"
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, card_content, speech_output, None, should_end_session))

        
        
def numlock(intent, session):
    """ Sets the color in the session and prepares the speech to reply to the
    user.
    """
    if 'FOURNUMBER' in intent['slots']:
        if(data.password_no==0):
            card_title = "STATE TREASURE"
            card_content = "Number Lock"
            session_attributes = {}
            should_end_session = False
            sol = intent['slots']['FOURNUMBER']['value']
            if(sol=='8061'):
                data.repeat_no=17
                data.help_no=9
                data.bag_no=1
                speech_output = "<speak>"\
                                "8 0 6 1,  is the correct key and the lock is opened. "\
                                "You find, a magnifying glass, and a letter in the lock."\
                                "</speak>"
                reprompt_text = "you can explore these things."
            else:
                data.repeat_no=18
                data.help_no=10
                speech_output = "<speak>"\
                                "The key is incorrect. "\
                                "Try again."\
                                "</speak>"
                reprompt_text = "Say, the four digits are. "
            return build_response(session_attributes, build_speechlet_response(
                card_title, card_content, speech_output, reprompt_text, should_end_session))
            
        elif(data.password_no==1):
            data.key_no=2
            card_title = "STATE TREASURE"
            card_content = "Elevator Lock"
            session_attributes = {}
            should_end_session = False
            soln = intent['slots']['FOURNUMBER']['value']
            if(soln=='735'):
                data.load_game=1
                data.repeat_no=31
                data.help_no=16
                data.lift_no=0
                speech_output = "<speak>"\
                                "<audio src='https://alexaskillstatetreasures.s3-ap-northeast-1.amazonaws.com/Ding.mp3'/>"\
                                "7 3 5, "\
                                "You are inside the elevator and you find "\
                                "that the button which leads you to the second floor is missing. "\
                                "You can only go to the first floor, "\
                                "And Your mission progress is saved commander."\
                                "</speak>"
                reprompt_text = "you can go and explore things."
            else:
                data.repeat_no=32 
                data.help_no=15
                speech_output = "<speak>"\
                                "The key is incorrect. "\
                                "Please try again."\
                                "</speak>"
                reprompt_text = "Say, the four digits are. "
            return build_response(session_attributes, build_speechlet_response(
                card_title, card_content, speech_output, reprompt_text, should_end_session)) 
                
        elif(data.password_no==2):
            card_title = "STATE TREASURE"
            card_content = "Password lock"
            session_attributes = {}
            should_end_session = False
            solnt = intent['slots']['FOURNUMBER']['value']
            if(solnt=='7326'):
                data.repeat_no=35
                data.help_no=19
                data.room_no=2
                data.load_game=2
                speech_output = "<speak>"\
                                "7 3 2 6, is the correct key ! " \
                                "<audio src='https://alexaskillstatetreasures.s3-ap-northeast-1.amazonaws.com/Punch.mp3'/>"\
                                "You fight the gaurd, "\
                                "and put his dress as a disguise. "\
                                "You dont find anything in the first floor. "\
                                "you are in the elevator and you have fixed the missing button. "\
                                "what would you do ? "\
                                "your game progress is saved. "\
                                "</speak>"
                data.lift_no=0
                data.first_no=1      
                data.verify_no=3
                reprompt_text = "Say,Go to second floor. "
            else:
                data.repeat_no=36
                data.help_no=20
                speech_output = "<speak>"\
                                "The password is incorrect. "\
                                "Please try again."\
                                "</speak>"
                reprompt_text = "Say, the four digits are. "
            return build_response(session_attributes, build_speechlet_response(
                card_title, card_content, speech_output, reprompt_text, should_end_session)) 
        
        elif(data.password_no==3):
            card_title = "STATE TREASURE"
            card_content = "Two digit lock"
            session_attributes = {}
            should_end_session = False
            solnti = intent['slots']['FOURNUMBER']['value']
            if(solnti=='46'):
                data.repeat_no=41
                data.help_no=25
                data.verify_no=4
                data.load_game=3
                speech_output = "<speak>"\
                                "The key is correct, and you are in the ground floor, with the gaurds costume. "\
                                "there, you see a huge dialpad in the floor, "\
                                "and you need to enter a phone number, "\
                                "to go into the secret room. "\
                                "so that, other gaurds believe you. "\
                                "You need to enter the 10 digit phone number. "\
                                "By Saying, the phone number is. "\
                                "Your game progress is saved. "\
                                "</speak>"
                reprompt_text = "Say, the phone number is. "
            else:
                data.repeat_no=36
                data.help_no=24
                speech_output = "<speak>"\
                                "The password is incorrect. "\
                                "Please try again."\
                                "</speak>"
                reprompt_text = "Say, the two digits are. "
            return build_response(session_attributes, build_speechlet_response(
                card_title, card_content, speech_output, reprompt_text, should_end_session))
    
    elif 'phone' in intent['slots']:
        card_title = "STATE TREASURE"
        card_content = "Phone Number"
        session_attributes = {}
        should_end_session = False
        number = intent['slots']['phone']['value']
        if(number=='9685847621'):
            data.repeat_no=42
            data.help_no=26
            data.light_no=1
            data.bag_no=2
            speech_output = "<speak>"\
            "<audio src='https://alexaskillstatetreasures.s3-ap-northeast-1.amazonaws.com/PhoneDial.mp3'/>"\
            "The phone rings, and the officer opens the gate for you. "\
            "now, You find yourself inside a secret room, "\
            "completely empty "\
            "with just a single paper on the floor. "\
            "you open the paper and find that, the paper has nothing written on it. "\
            "What would you do? "\
            "</speak>"
            reprompt_text = "Say something. "
        else:
            data.repeat_no=43
            data.help_no=25
            speech_output = "<speak>"\
                            "<audio src='https://alexaskillstatetreasures.s3-ap-northeast-1.amazonaws.com/Cell.mp3'/>"\
                            "The number is incorrect. "\
                            "Please try again."\
                            "</speak>"
            reprompt_text = "Say, the phone number is. "
        return build_response(session_attributes, build_speechlet_response(
            card_title, card_content, speech_output, reprompt_text, should_end_session))
            
            
def explore_paper():
    data.help_no=26
    data.repeat_no=46
    card_title = "STATE TREASURE"
    card_content = "Explore Paper..!!"
    session_attributes = {}
    should_end_session = False
    speech_output = "<speak>"\
                    "<audio src='https://alexaskillstatetreasures.s3-ap-northeast-1.amazonaws.com/Letteropen.mp3'/>"\
                    "You find nothing in the paper. it is blank.</speak> "
    reprompt_text = "nothing much. "
    return build_response(session_attributes, build_speechlet_response(
            card_title, card_content, speech_output, reprompt_text, should_end_session))
            
def escape():
    if(data.light_no==1):
        card_title = "STATE TREASURE"
        card_content = "Escape..!!"
        session_attributes = {}
        should_end_session = True
        speech_output = "<speak>"\
            "<audio src='https://alexaskillstatetreasures.s3-ap-northeast-1.amazonaws.com/Obama.mp3'/>"\
            "<voice name='Justin'><lang xml:lang='en-US'>"\
            "Congratulations commander! "\
            "the wall slowly splits, and you see the treasure. "\
            "You have finally found the treasure. "\
            "Mission accomplished. "\
            "Thanks for playing commander. "\
            "have a nice day. "\
            "</lang></voice></speak>"
        reprompt_text = "Thank you. "
        return build_response(session_attributes, build_speechlet_response(
            card_title, card_content, speech_output, reprompt_text, should_end_session)) 
    else:
        card_title = "STATE TREASURE"
        card_content = "What..??"
        session_attributes = {}
        should_end_session = False
        speech_output = "<speak>Cannot recognize.</speak>"
        reprompt_text = "what ?"
        return build_response(session_attributes, build_speechlet_response(
            card_title, card_content, speech_output, reprompt_text, should_end_session))
        
def wordlock(intent, session):
    """ Sets the color in the session and prepares the speech to reply to the
    user.
    """
    data.key_no=1
    card_title = "STATE TREASURE"
    card_content = "Word Lock"
    session_attributes = {}
    should_end_session = False
    if 'Wordlock' in intent['slots']:
        word = intent['slots']['Wordlock']['value']
        if(word=="shit"):
            data.repeat_no=27
            data.help_no=14
            speech_output = "<speak>"\
                            "The word is correct. "\
                            "You find a key to open the main door, "\
                            "and the letters, P, U, N, printed inside the locker. "\
                            "</speak>"
            reprompt_text = "use the clues properly."
        else:
            data.repeat_no=28
            data.help_no=7
            speech_output = "<speak>"\
                            "The word is incorrect. "\
                            "Please try again."\
                            "</speak>"
            reprompt_text = "Say, the word is. "
    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))



def invalid():
    card_title = "STATE TREASURE"
    card_content = "I didn't get that."
    session_attributes = {}
    should_end_session = False
    speech_output = "<speak>sorry i could not recognize that. you can say help me.</speak>"
    reprompt_text = "say help me. "
    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))
        
def accept():
    card_title = "STATE TREASURE"
    card_content = "You have got more hints."
    session_attributes = {}
    should_end_session = False
    if(data.accept_no==1):
        speech_output = "<speak><voice name='Brian'><lang xml:lang='en-GB'>you have unlocked all the hints commander. "\
                        "now you can ask for help.</lang></voice></speak>"
    elif(data.accept_no==2):
        return help_me()
    reprompt_text = "say help me."
    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))
    
def decline():
    card_title = "STATE TREASURE"
    card_content = "You don't have any hints."
    session_attributes = {}
    should_end_session = False
    speech_output = "<speak><voice name='Brian'><lang xml:lang='en-GB'>since you didn't buy the hints commander, "\
                    " i cannot help you further in this mission. </lang></voice></speak>"
    reprompt_text = "Try something and escape with the treasure. "
    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))
        
def error():
    card_title = "STATE TREASURE"
    card_content = "Error."
    session_attributes = {}
    should_end_session = False
    speech_output = "<speak><voice name='Brian'><lang xml:lang='en-GB'>it seems that you have an error commander. "\
                    " try again by saying, help me. </lang></voice></speak>"
    reprompt_text = "say, help me. "
    return build_response(session_attributes, build_speechlet_response(
        card_title, card_content, speech_output, reprompt_text, should_end_session))        



# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])

def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """
    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    data.help_no=0
    data.repeat_no=0
    data.knife_no=0
    data.mag_no=0
    data.key_no=0
    data.room_no=0
    data.first_no=0
    data.second_no=0
    data.verify_no=0
    data.secret_no=0
    data.lift_no=3
    data.light_no=0
    data.bag_no=0
    data.password_no=0
    return menu()
    
def reset_game():
    data.help_no=0
    data.repeat_no=0
    data.knife_no=0 
    data.mag_no=0
    data.key_no=0
    data.room_no=0
    data.first_no=0
    data.second_no=0
    data.verify_no=0
    data.secret_no=0
    data.lift_no=3
    data.light_no=0
    data.bag_no=0
    data.load_game=0
    data.password_no=0
    return menu()
    

class data:
    load_game=0
    help_no=0
    repeat_no=0
    knife_no=0
    mag_no=0
    key_no=0
    room_no=0
    first_no=0
    second_no=0
    verify_no=0
    secret_no=0
    lift_no=3
    light_no=0
    bag_no=0
    password_no=0
    buy_help=0
    accept_no=0


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']
    # Dispatch to your skill's intent handlers
    if intent_name == "AMAZON.HelpIntent":
        return help_me()
    elif intent_name == "BuyHelpIntent":
        return buyhelp()
    elif intent_name == "RepeatIntent":
        return repeat()
    elif intent_name == "NewGame":
        return get_welcome_response()  
    elif intent_name == "LoadGame":
        return load_game() 
    elif intent_name == "ResetIntent":
        return reset_game()     
    elif intent_name == "ExploreBag":
        return explore_bag()    
    elif intent_name == "ExploreMapIntent":
        return explore_map()    
    elif intent_name == "ExploreKnifeIntent":
        data.knife_no=0
        return explore_knife() 
    elif intent_name == "UseKnifeIntent":
        return explore_knife()    
    elif intent_name == "ExploreRoomIntent":
        return explore_room()
    elif intent_name == "ExploreInvImgIntent":
        return explore_invimg() 
    elif intent_name == "ExploreNumLockIntent":
        return explore_numlock()
    elif intent_name == "ExploreWordLockIntent":
        return explore_wordlock() 
    elif intent_name == "ExploreMainDoorIntent":
        return explore_maindoor()  
    elif intent_name == "ExploreElevator":
        return explore_elevator()     
    elif intent_name == "ExploreMagGlassIntent":
        return explore_magglass()
    elif intent_name == "ExploreLetterIntent":
        return explore_letter()
    elif intent_name == "UseMagIntent":
        return use_mag()  
    elif intent_name == "UseKeyIntent":
        return use_key()     
    elif intent_name == "FirstFloorIntent":
        return first_floor()  
    elif intent_name == "SecondFloor":
        return second_floor()      
    elif intent_name == "BookIntent":
        return explore_book()    
    elif intent_name == "ExploreCloset":
        return explore_closet() 
    elif intent_name == "LightIntent":
        return light_off()     
    elif intent_name == "WallPaintIntent":
        return wall_paint()         
    elif intent_name == "ExploreRoomLock":
        return explore_room_lock()
    elif intent_name == "EleLockIntent":
        return numlock(intent, session)
    elif intent_name == "TwoDigitIntent":
        return numlock(intent, session)    
    elif intent_name == "PassIntent":
        return numlock(intent, session)    
    elif intent_name == "NumLockIntent":
        return numlock(intent, session)   
    elif intent_name == "WordLockIntent":
        return wordlock(intent, session)     
    elif intent_name == "PhoneIntent":
        return numlock(intent, session)
    elif intent_name == "ExplorePaper":
        return explore_paper()    
    elif intent_name == "LightIntent":
        return light_off()    
    elif intent_name == "FinalEscape":
        return escape()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        return invalid()
        
    
def location(intent_request, session):
    location = intent_request['locale']
    if location == "en-IN":
        data.buy_help=0
        data.accept_no=1
    elif location == "en-AU":
        data.buy_help=0
        data.accept_no=1
    elif location == "en-CA":
        data.buy_help=0
        data.accept_no=1
    elif location == "en-US":
        data.buy_help=1
    elif location == "en-GB":
        data.buy_help=1
    elif location == "en-UK":
        data.buy_help=1    
    else:
        data.buy_help=0
    
def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        location(event['request'], event['session'])
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "Connections.Response":
        return buyresponse(event['request'], event['session'])    
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
 
