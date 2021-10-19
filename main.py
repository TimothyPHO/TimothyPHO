import random
import re

greetingOptions = ["eyy","sup","howdie"]

endingOptions = ["adios", "au revior","sayonara"]

jokeOptions = ["you come here often?","don't you have something else to do"]

def chat(text):
  
  text = text.replace(",", "")
  text = text.replace(".","")
  text = text.replace("!","")
  text = text.replace("?","")
  
  textLower = text.lower()
  
  myMatchObject = re.match("what(('s)|([\s]+is))[\s]+your[\s]+favorite[\s]+(.+)", textLower)
  if myMatchObject:
    favoriteIndex = myMatchObject.group(4)
    return "My favorite {} is {}".format(favoriteIndex, myFavorites[favoriteIndex])
 
  words = text.split(" ")
  for word in words:
    if word.lower() in greetingOptions:
      return random.choice(greetingOptions).capitalize()
  if text.lower() in endingOptions:
    return random.choice(endingOptions).capitalize() 
  if text.lower() in jokeOptions:
    return random.choice(jokeOptions).capitalize()
  else:
    return "I'm still learning.  Try saying hello."

while(True):
  userInput = input(">>> ")
  print(chat(userInput))




