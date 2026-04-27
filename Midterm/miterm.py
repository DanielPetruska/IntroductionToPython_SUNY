import random

# the rooms and where doors go
rooms = {
    "Yellow": {"North": "Blue", "South": "Red"},
    "Red": {"North": "Yellow", "West": "Green"},
    "Green": {"East": "Red", "South": "Exit"},
    "Blue": {"South": "Yellow", "West": "White"},
    "White": {"East": "Blue"}
}

# starting values
current_room = "Yellow"
has_key = False
exit_unlocked = False
dragon_helped = False
opened_boxes = []

# sets up random boxes and dragon
rooms_list = ["Yellow", "Red", "Green", "Blue", "White"]
gold_room = random.choice(rooms_list)
rooms_list.remove(gold_room)
silver_room = random.choice(rooms_list)

# to decide which box has the key
if random.randint(0, 1) == 0:
    key_box = "Gold"
    key_room = gold_room
else:
    key_box = "Silver"
    key_room = silver_room

dragon_room = random.choice(rooms_list)

print("Welcome to ZORK game. There are 5 rooms: Green, Yellow, Red, Blue, and White.\n")

while True:
    print("You are in the " + current_room + " room.", end=" ")

    # print the doors
    exits_str = ""
    for d in rooms[current_room]:
        exits_str += "a door " + d + " and "
    print(exits_str[:-5] + ".")

    if current_room == "Green":
        if exit_unlocked:
            print("There is the EXIT South. EXIT is unlocked.")
        else:
            print("There is the EXIT South. EXIT is locked.")

    if current_room == gold_room and "Gold" not in opened_boxes:
        print("There is a Gold box.")
    if current_room == silver_room and "Silver" not in opened_boxes:
        print("There is a Silver box.")

    if current_room == dragon_room:
        print("There is a dragon here.")

    print()

    cmd = input("USER: ").strip().lower()

    if cmd.startswith("go "):
        dir = cmd[3:].capitalize()
        if dir in rooms[current_room]:
            if current_room == "Green" and dir == "South":
                if exit_unlocked:
                    print("Congratulations! You made it!")
                    break
                else:
                    print("The EXIT is locked.")
                    continue
            current_room = rooms[current_room][dir]
        else:
            print("You can't go that way.")

    elif cmd == "open box":
        opened = False
        if current_room == gold_room and "Gold" not in opened_boxes:
            print("Gold box is open")
            opened_boxes.append("Gold")
            opened = True
            if key_box == "Gold":
                print("You found the EXIT key inside!")
                has_key = True
            else:
                print("This box is empty... The other box locked permanently.")
                print("Game Over!")
                break
        if current_room == silver_room and "Silver" not in opened_boxes:
            print("Silver box is open")
            opened_boxes.append("Silver")
            opened = True
            if key_box == "Silver":
                print("You found the EXIT key inside!")
                has_key = True
            else:
                print("This box is empty... The other box locked permanently.")
                print("Game Over!")
                break
        if not opened:
            print("There is no box here.")

    elif cmd == "get key":
        if has_key:
            print("You already have the key.")
        elif current_room == key_room and key_box in opened_boxes:
            print("You have the EXIT key now")
            has_key = True
        else:
            print("There is no key here.")

    elif cmd == "unlock exit":
        if not has_key:
            print("You don't have the key, EXIT still locked")
        elif current_room != "Green":
            print("You must be in the Green room to unlock the exit.")
        else:
            exit_unlocked = True
            print("The EXIT is unlocked now")

    elif cmd == "exit":
        if current_room == "Green" and exit_unlocked:
            print("Congratulations! You made it!")
            break
        else:
            print("You can't exit yet.")

    elif cmd == "where is the key" and current_room == dragon_room and not dragon_helped:
        print("Dragon says you need to answer a question to tell you where the key is.")
        print('Type "ask me" to answer the riddle.')

    elif cmd == "ask me" and current_room == dragon_room and not dragon_helped:
        print('Dragon asks "What has to be broken before you can use it?"')
        ans = input("Your answer: ").lower().strip()
        if "egg" in ans:
            print('Dragon says "correct", the key is in the ' + key_box + ' box.')
            dragon_helped = True
        else:
            print("Dragon says 'wrong'. He won't help you anymore.")
            dragon_helped = True

    else:
        print("I don't understand that command.")