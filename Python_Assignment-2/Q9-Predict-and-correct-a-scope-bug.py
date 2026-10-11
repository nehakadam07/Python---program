#score = 50
#def update():
    #print(score)
    #score = score + 10
#update()
#print(score)

# Q9: Correct the scope bug using global

score = 50

def update():
    global score  # Use the global variable

    print(score)  # Print the current score
    score = score + 10  # Increase the global score

update()

print(score)  # Print the updated score