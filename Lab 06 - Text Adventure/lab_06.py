class Room:
    """This is a class"""
    def __int__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
def main():
    """This is the main function"""
    # Creating empty list
    room_list = []
    current_room = 0
    next_room = 0
    done = False

    # beedroom 2 -0 ( description, north, east, south, west)
    room = Room ("you are in the second room, there is a door ro the east.", None, 1, None, None)
    room_list.append(room)

    #add rest of rooms
    while not done:
        print(room_list[current_room].description)
        direction = input("which way would you like to go? (n s e w)").lower()
        if direction [0]== 'n':
            next_room = room_list[current_room].north

            # add other directions
        else:
            print("please pick a valid direction")
            continue

            # check for valid choice
        if next_room == None:
            print ("you cant go that way!")

            # if all is well, set new room
        current_room = next_room

main()
