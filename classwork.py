class Room():
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        self.doors = []
        self.windows = []

    def check_room(self, doors, windows):
        if room.width <= 1 or room.length <= 2 or room.height < 2.5:
            return 'Такой комнаты не существует. Параметры комнаты некорретные'

        for i in doors:
            d = 0
            d = d + i.width + i.height
            if i.height >= room.height or i.width >= room.width:
                return 'Такой комнаты не существует. Параметры двери некорректные'
                break

        for i in windows:
            w = 0
            w = w + i.width + i.height
            if i.height + i.delta >= room.height or i.width >= room.width:
                return 'Такой комнаты не существует. Параметры окна некорректные'
                break

        if (w + d) * 2 >= 2 * (self.length + self.width) * self.height:
            return 'Такой комнаты не существует'

    def wallpaper(self, doors, windows):
        all_room = 2 * (self.length + self.width) * self.height
        for i in windows:
            all_room = all_room - i.width * i.height
        for i in doors:
            if i.secret_room == 0:
                all_room = all_room - i.width * i.height
            else:
                pass
        return 'Необходимая площадь обоев', all_room

    def room_light(self, windows):
        w = 0
        for i in windows:
            w = w + i.height * i.width
        return 'Коэф освещенности комнаты', w / 2 * (self.length + self.width) * self.height

    def square_room(self):
        return self.length * self.width

    def add_window(self, window):
        self.windows.append(window)

    def add_door(self, door):
        self.doors.append(door)


class Frame:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def square(self):
        return (self.width * self.height)


class Door(Frame):
    def __init__(self, width, height, secret_room):
        Frame.__init__(self, width, height)
        self.secret_room = secret_room


class Window(Frame):
    def __init__(self, width, height, delta):
        Frame.__init__(self, width, height)
        self.delta = delta
room=Room(5,8,3)
door1=Door(0.5,2,0)
door2=Door(0.5,2,1)
window1=Window(0.5,1.5,0.5)
window2=Window(0.5,1.5,0.5)

room.add_window(window1)
room.add_door(door1)
room.add_door(door2)

print(room.check_room(room.doors,room.windows))
print(room.wallpaper(room.doors,room.windows))
print(room.room_light(room.windows))