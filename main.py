from playsound import playsound
import webbrowser                                        # dependencies
from os import system, name
from time import sleep


def clear():
    if name == 'nt':                                                                    
        _ = system('cls')                        # clear function
    else:
        _ = system('clear')


clear()




print("\t\t\t\t \033[1;31;40m   ------Ivy your personal assistant------")
playsound("assets/Sounds/IVY.mp3")                                            # welcome message
sleep(0.5)

print("\n\n \033[1;37;40m   Type 'help' to get a list of all available commands")
playsound("assets/Sounds/help-notify.mp3")                                            # help notification

sleep(0.5)


def commandparse():                                          # command parser function
    
    playsound("assets/Sounds/command.mp3")
    command = input("\n>>> ")
    
    if command == "help":
             print("Available commands:\n")
             print("* sing a song\n")
             print("* web Browser\n")
             print("* Youtube\n")
             print("* facebook\n")
             print("* instagram\n")
             print("* github\n")
             print("* twitter\n")
             print("* linkedin\n")
             print("* soundcloud\n")
             print("* imdb\n")
             print("* netflix\n")
             print("* amazon\n")
             print("* ebay\n")
             print("* weather\n")
             print("* quora\n")
             print("* google meet\n")
             print("* gmail")
             print("* tell me a story\n")
             print("* clear\n")
             print("* about\n")
             print("* exit\n")
             sleep(0.5)
             commandparse()

    elif command == "sing a song":
        playsound("assets/Sounds/song.mp3")
        sleep(0.5)
        commandparse()

    elif command == "web browser":
        playsound("assets/Sounds/opening.mp3")
        webbrowser.open('https://www.google.com/', new=2)
        sleep(5)
        commandparse()

    elif command == "exit":
        clear()
        exit(0)

    elif command == "youtube":
        playsound("assets/Sounds/opening.mp3")
        webbrowser.open('https://www.youtube.com/', new=2)
        sleep(0.5)
        commandparse()

    elif command == "facebook":
        playsound("assets/Sounds/opening.mp3")
        webbrowser.open('https://www.facebook.com/', new=2)
        sleep(0.5)
        commandparse()

    elif command == "github":
        playsound("assets/Sounds/opening.mp3")
        webbrowser.open('https://www.github.com/', new=2)
        sleep(0.5)
        commandparse()

    elif command == "twitter":
        playsound("assets/Sounds/opening.mp3")
        webbrowser.open('https://www.twitter.com/', new=2)
        sleep(0.5)
        commandparse()

    elif command == "instagram":
        playsound("assets/Sounds/opening.mp3")
        webbrowser.open('https://www.instagram.com/', new=2)
        sleep(0.5)
        commandparse()

    elif command == "about":
        print("Name:IVY\nVersion:1.0.0.1\n")
        print("Author:https://github.com/Adityan-compile \n ")
        sleep(0.5)
        commandparse()
    elif command == "clear":
        clear()
        sleep(0.5)
        commandparse()

    elif command == "tell me a story":
        playsound("assets/Sounds/story.mp3")
        sleep(1)
        commandparse()

    elif command == "linkedin":
        playsound("assets/Sounds/opening.mp3")
        webbrowser.open('https://www.linkedin.com/', new=2)
        sleep(0.5)
        commandparse()
        
    elif command == "gmail":
        playsound("assets/Sounds/opening.mp3")
        webbrowser.open('https://www.gmail.com/', new=2)
        sleep(0.5)
        commandparse()  
    
    elif command == "netflix":
        playsound("assets/Sounds/opening.mp3")
        webbrowser.open('https://www.netflix.com/', new=2)
        sleep(0.5)
        commandparse()
        
    elif command == "soundcloud":
        playsound("assets/Sounds/opening.mp3")
        webbrowser.open('https://www.soundcloud.com/', new=2)
        sleep(0.5)
        commandparse()
        
    elif command == "imdb":
        playsound("assets/Sounds/opening.mp3")
        webbrowser.open('https://www.imdb.com/', new=2)
        sleep(0.5)
        commandparse()
        
    elif command == "amazon":
        playsound("assets/Sounds/opening.mp3")
        webbrowser.open('https://www.amazon.com/', new=2)
        sleep(0.5)
        commandparse()
        
    elif command == "ebay":
        playsound("assets/Sounds/opening.mp3")
        webbrowser.open('https://www.ebay.com/', new=2) 
        sleep(0.5)
        commandparse()
        
    elif command == "weather":
        playsound("assets/Sounds/opening.mp3")
        webbrowser.open('https://www.weather.com/', new=2)
        sleep(0.5)
        commandparse()  
        
    elif command == "quora":
        playsound("assets/Sounds/opening.mp3")
        webbrowser.open('https://www.quora.com/', new=2)
        sleep(0.5)
        commandparse()  
        
    elif command == "google meet":
        playsound("assets/Sounds/opening.mp3")
        webbrowser.open('https://www.meet.google.com/', new=2)
        sleep(0.5)
        commandparse()   
    
    else:
        print("Command not found")
        playsound("assets/Sounds/commandnotfound.mp3")
        sleep(0.5)
        commandparse()


sleep(0.5)
commandparse()
