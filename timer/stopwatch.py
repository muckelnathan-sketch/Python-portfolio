import time
#create functions to be used for the application later
def stopwatch():
    #create a start time so that we can subtract the afterwards time when the player ends the stopwatch 
    start = time.time()
    input("press enter to stop stopwatch ") #when the user submits using the input its them pretty much pressing a button
    print(f"{time.time() - start:.2f} seconds")
def timer():
    how_long = input("how many seconds to wait: ")
    time.sleep(how_long) #sleep the amount of seconds  the user wishes, perhaps i could work in a system that finds how many minutes and seconds the user wants
    print("done!")
while True: #implementing match case, also took a nap
    match input("stopwatch or timer: "):
        case 'stopwatch':stopwatch();break 
        case 'timer':break; timer();break #using semi colons for a cleaner look
    #i think tmr i will begin to clean up the code , perhaps using match/case for simpler code