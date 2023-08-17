import os


class Position(object):
    def __init__(self):
        self.position = [] # start(), start()
        
    def change_user_position(self, new_pos) -> None:
        self.position[0] = self.position[1]
        self.position[1] = new_pos
        # [room_1  new_pos]
        return None

    def check_past_user_position(self):
        return self.position[0]()
    
    def check_present_user_position(self):
        # return self.position[1] # self.main - сылка на функцию
        return self.position[1]() # self.main() - сама функция 


class Inventory(object):

    def __init__(self):
        self.inventory = [] # атрибут

    def check_inventory(self) -> None:
        print('Ваш инвентарь:', end='\n\n')
        
        for i in self.inventory:
            print(i, end=' ') # 1, 2, 3,
        
    def add_item_in_inventory(self, item: str) -> None:
        self.inventory.append(item)
        print(f'Предмет {item} добавлен в инвентарь.\n\n')
        return None


class History(Inventory, Position):

    def __init__(self):
        self.inv = Inventory()
        self.pos = Position()

        self.inventory = self.inv.inventory
        self.pos.position.append(self.start)
        self.pos.position.append(self.start)

        
    def start(self):
        history = '\n\nУправление: \'i\' - инвентарь, \'b\' - назад\n\n' \
                  'Перед вами 4 двери, какую вы выберите ?:\n\n' \
                  '\"Room 1\", \"Room 2\", \"Room 3\", \"Room 4\"\n\n'

        var: str = input(history).lower()
        if isinstance(var, str) == False: self.start()

        match var:
            case 'room 1': self.room_1()
            case 'room 2': self.room_2()
            case 'room 3': self.room_3()
            case 'room 4': self.room_4()
            case 'i':      self.inv.check_inventory()
            case 'b':      self.pos.check_past_user_position()


    def room_1(self):
        self.pos.change_user_position(new_pos=self.room_1)
        history = '\n\nBoy (Вы) next door заходит into the Room 1\n' \
                  'и видит перед собой книгу с надписью \"Подними меня\"\n\n' \
                  'Что будете делать: \"Взять\"  или \"Оставить\" ?\n\n'
        var: str = input(history).lower()
        
        match var:
            case 'взять': self.room_1_1()
            case 'оставить': self.room_1_2()
            case 'i':      self.inv.check_inventory()
            case 'b':      self.pos.check_past_user_position()

    def room_1_1(self):
        self.pos.change_user_position(new_pos=self.room_1_1)
        self.inv.add_item_in_inventory('Странная книга')
        history =   '\nBoy next door роздивляється кімнату, в цій кімнаті є телефон біля книги, яку він підібрав \n' \
                    'В кінці кімнати є Комп°ютер,який виглядає ніби ним нікто і не користувався\n\n' \
                    'Що ви зробите перейдете в іншу \"Room 2\" або скористаєтесь предметом \"Странная книга\"\n\n'
        
        var = input(history).lower()
        match var:
            case 'Room 2' : self.room_2()
            case 'Странная книга' : self.room_1_1_1()
            case 'i':      self.inv.check_inventory()
            case 'b':      self.pos.check_past_user_position()

    def room_1_1_1(self):
        self.pos.change_user_position(new_pos=self.room_1_1_1)
        history =   '\nBoy next door відкриває книгу на першій сторінці написано: \n'  \
                    '"Welcome to the club body! вітаю тебе в підпільному укрнаціалістичному Gym для істенних козаків.\n'  \
                    'Якщо в тебе будуть питання, використай персонал ,або загугли на комп°ютері."\n' \
                    '(З книги випала брошура) \n\n' \
                    'Що ви зробите?:  \"Комп°ютер\"  \"Брошура\"\n\n'
        
        var = input(history).lower()
        match var:
            case 'i':      self.inv.check_inventory()
            case 'b':      self.pos.check_past_user_position()



    def room_1_2(self):
        self.pos.change_user_position(new_pos=self.room_1_2)
        history = '\n Біля книги є телефон ви можете подзвонити Billy та  Van\n' \
        ''
        
        match var:
            case 'i':      self.inv.check_inventory()
            case 'b':      self.pos.check_past_user_position()

        
        var = input(history).lower()

    def room_2(self):
        self.pos.change_user_position(new_pos=self.room_2)
        pass

    def room_3(self):
        self.pos.change_user_position(new_pos=self.room_3)
        pass

    def room_4(self):
        self.pos.change_user_position(new_pos=self.room_4)
        pass

    
if __name__ == '__main__':
    h = History()
    
    while 1:
        h.pos.check_present_user_position()
