#Made by Cy Bunayog
#I'm not even sure if OS is neccessary to import
import webbrowser, os

continue_program = True
print("\n\n\nA web browsing script that doesn't require opening a browser!\n\n\n\n")

#new = 2 #opens a tab
#webbrowser.open('insert URL here')
while continue_program:

    webDir = input("Enter in a URL: (ex: google.com) -> ").lower()
    hasHTTP = 'http://'
    levelDomain = ['.com', '.org', '.net', '.gov', '.edu']
    browser = ['chrome', 'firefox', 'edge', 'safari']
    websiteURL = hasHTTP + webDir

    print("Website typed:", websiteURL, "\n")

    user_browser = input("Would you like to use Google [Chrome], Mozilla [Firefox], Apple [Safari], or Microsoft [Edge]?").lower()

    #this can be cleaner
    if user_browser == browser[0]:
        path = "insert file path for chrome here %s"
    elif user_browser == browser[1]:
        path = "insert file path for firefox here %s"
    elif user_browser == browser[3]:
        #path = "insert Safari's location here"
        #I didn't have safari on my Windows computer.
        print("Windows doesn't have safari installed. Try again.")
        continue #skipping this, delete if safari is installed
    elif user_browser == browser[2]:
        #Edge won't open for some odd reason
        path = "insert file path for edge here %s"
    else:
        print("\nInvalid browser, use another one.\n")

    if any(ext in websiteURL for ext in levelDomain):
        #ext is just an empty variable
        #opens the URL that contains any if the level domains in the list
        #chromePath = "insert file path for chrome here %s"
        webbrowser.get(path).open(websiteURL)
        print("\nSuccess!\n")
        continue_program = False
        break
    else:
        print("\nInvalid URL path, try again.\n")
        continue_program = True
        
    #automatically opens default browser
    #if hasHTTP in webDir:
        #opens the url if it contains an HTTPS
        #webbrowser.open(webDir)
        #break #exit loop
    #else:
        #rint("Invalid output, try again.")
