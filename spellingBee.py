import networkzero as nw0

#Size screen
WIDTH = 1440
HEIGHT = 750

#Initiating server
address = nw0.advertise("spellingBee")

#Variables
words = [] #Save the list of words in the text file
answers = [] #List of students and their marks
status = "" #String to display the status of the program
counter = 0 #Counter of words

#Getting the words from the document
f = open("words.txt", "r")
for w in f:
    words.append(w.lower())
f.close()

#Deleting return character "/n"
for r in range(0, len(words)):
    words[r] = words[r][0:-1]


#Sending words to spellingBee Service
nw0.send_news_to(address, "spellingBee", len(words)) #Sending words quantity

for w in words:
    nw0.send_news_to(address, "spellingBee", w)
    status = "Sending Words..."

status = "Words sended"

def draw():
    global status

    screen.clear()
    screen.draw.text(status, center = (WIDTH/2,HEIGHT/2), color = "green", fontsize = 200)

def on_key_down(key, mod, unicode):
    global status, counter, words

    if key == keys.RETURN:
        counter = counter + 1
        status = str(counter) + " word"

    if counter == len(words):
        status = "Finish!!!"

def update():
    global status

    if status == "Finish!!!":
        status = "Receiving answers"
        address = nw0.advertise("spellingBee")
        nw0.wait_for_news_from("spellingBee")

