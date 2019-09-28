import webbrowser, os

continue_program = True
print("\n\n\nA web browsing script that doesn't require opening a browser!\n\n\n\n")

#new = 2 #opens a tab
#webbrowser.open('https://www.instagram.com/cybunayog')
while continue_program:

    webDir = input("Enter in a URL: (ex: google.com) -> ").lower()
    hasHTTP = 'http://'
    levelDomain = ['.com', '.org', '.net', '.gov', '.edu']
    browser = ['chrome', 'firefox', 'edge', 'safari']
    websiteURL = hasHTTP + webDir

    print("Website typed:", websiteURL, "\n")

    user_browser = input("Would you like to use Google [Chrome], Mozilla [Firefox], Apple [Safari], or Microsoft [Edge]?").lower()

    if user_browser == browser[0]:
        path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    elif user_browser == browser[1]:
        path = "C:/Program Files/Mozilla Firefox/firefox.exe %s"
    elif user_browser == browser[3]:
        #path = "insert Safari's location here"
        print("Windows doesn't have safari installed. Try again.")
        continue #skipping this
    elif user_browser == browser[2]:
        #Edge won't open for some odd reason
        path = "C:/Windows/SystemApps/Microsoft.MicrosoftEdge_8wekyb3d8bbwe/MicrosoftEdge.exe %s"
    else:
        print("\nInvalid browser, use another one.\n")

    if any(ext in websiteURL for ext in levelDomain):
        #ext is just an empty variable
        #opens the URL that contains any if the level domains in the list
        #chromePath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(path).open(websiteURL)
        print("\nSuccess!\n")
        continue_program = False
        break
    else:
        print("\nInvalid URL path, try again.\n")
        continue_program = True

    #if hasHTTP in webDir:
        #opens the url if it contains an HTTPS
        #webbrowser.open(webDir)
        #break #exit loop
    #else:
        #rint("Invalid output, try again.")
