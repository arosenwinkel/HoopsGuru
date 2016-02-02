# utilities.py

# various functions that are used throughout the game

import random


def weighted_choice(choices):  # takes in a dictionary as an argument
    total = sum(w for c, w in choices.items())
    r = random.uniform(0, total)
    limit = 0
    for c, w in choices.items():
        if limit + w > r:
            return c
        limit += w


def height_to_feet(height):  # convert height in inches into the normal way of displaying it, e.g. 6'7"
    feet = int(height / 12)
    inches = height % 12
    return '''{}'{}"'''.format(feet, inches)


class NameGenerator:
    def __init__(self):

        self.white_first_names = ["Rick","Ashley","Robert","Chris"
			,"Alex","Aaron","Steve","Max","Evan","Daniel","Chad","Rhys"
			,"Bret","Thomas","Lucas","George","Chaz","Ace","Sergio",
			"Christian","Fernando","Micah","Matt","Wayne","A.J.","Hector","Preston",
			"Albert","Adam","Abel","Angelo","Ramon","Randall","Rami","Raj","Regis",
			"Reid","Rayne","Ray","Rider","Riley","Salvio","Salim","Zachary",
			"Devin","Jon","Harsh","Patrick","Michael","Jordy","Paul","Chris","Darko",
			"Donald","DJ","Eden","James","Jim","Steven","Adam","Rudy","Charles","Charlie",
			"Wayne","Wyatt","Tony","Adam","Niall","Hui","Chuck","Alex","Greg","George","Tom",
			"Tim","Thomas","John","Jonathan","Miles","Maxwell","Mac","Bryan","Brian","Sean",
			"Shaun","Timothy","Ryan","Kurt","Irwin","Gary","Patrick","Zach","Zack","Jake","Jacob","Jason","Steven",
			"Charlie","Harry","Aaron","Alexander","Andrew","Brian","Stewart","Peter","Chris","Michael","Ed","Edward","Eddy"
			,"Joey","Ross","Chandler","Frank","Larry","Ted","Steven","Keith","Kyle","Corey",
            "Hugh","Gary","Ross","Wayne","Josh","Jon","Mike","Micah","Paul","Al","Bill",
            "Titus","Lissiane","Timo","Yassine","Federico","Tyson","Ty","Bruno","Chris"
            ,"Chris","Mike","John","Josh", "Volcano"]

        self.white_last_names = ["James","Michaels","Rosenberg",
			"Heidi","Richards","Jordan","Wilson","Hill","Stoffels","Swanson"
			,"Corteia","Dubilai","Guadalajara","Rosenwinkel","Ayalp",
			"Rothenberg","Hanson","Alva","Diekman","Flood","Young","Zimmer","Nash",
			"Cerave","Spare","Mapa","Battia","Matheson","Olivero"
			,"Greenland","Samsoni","Lampard","Lampeire","Waker","Atlas","Ayers",
			"Myers","Atkins","O'Brien","O'Shea","Cameron","Lambert","Napolean",
			"Murphy","Antinosek","Tosie","Quebec","Towers","Torres","Wang",
			"Alba","Ferrell","Kodiak","Smith","Jones","Starr","Hart","Hazard"
			,"O'Hoolihan","Smith","Mili","Reed","Rutho","Powers","Wesleyan","Huud van Roy",
			"Rogers","Dobrey","Yamimoto","Yoshimi","Yu","Li","Nguyen",
			"Guiles","Seety","Quintes","DaSilva","DaTowas","Hyud","Ohmes","Gomez",
			"van Damme","Ruggles","Drescher","McLaughlin","Miner","Seedorf","Vela","Griezi",
			"Ponerski","Slava","Smirnov","Ivanov","Ivanovic","Lebedev","Morozov","Solovyov","Popov",
			"Kuznetsov","Kozlov","Novikov","Petrovic","Popvic","Nikolic","Jovanovic","Alfredsson",
			"Adolfsonn","Carlsson","Jonasson","Emilsson","Granberg","Bengtsson","Axelsson",
			"Johannesson","Elofsson","Holm","Westberg","Ottosson","Nilsson","Rodriguez","Perez",
			"Sanchez","Rivera","Martinez","Wilson","Davis","Williams","Smith","Brown","Garcia","Miller",
			"Smith","Wilson","Jones","Jones","Johnson","Wilson","Hosking","Gillis","Greco",
            "Prescott","Youless","Macomb","Jacobs","Smith","Young","Routledge","Clio","Snyder",
            "Vulaj","Zimmer","Caldwell","Samaras","Lovelady","Kilburn","Kennedy","Bush",
            "Goodman","Oldman","Badman","Eagel","Bruegger","McCarron","McConnell","Ponch"
            ,"Christoff","Jones","Punch","Treveleyan","Bond","Goiles","O'Doyle","Sandler",
            "DiMarzio","Shepherd","Martin","Martins","Rodriguez","Werner"]

        self.black_first_names = ["Jamal","Mike","Jameis","Idode",
			"Darnell","Malik","Trevon","Maurice","DeShawn","Caleb","Gabriel"
			,"Jayden","Josiah","Jeremiah","Jermaine","Edius","Devon","Levon","DeMarcus",
			"Bo","Jim","James","JJ","Herbert","DeVonte","Travis","Darius","Levonte",
			"Marquis","DeMario","Doran","Decovon","Dazhawn","Derick","Demondre","Kobe"
			,"Dwight","Tyrone","Grover","Marius","Ryan","Carmelo","Lou","Tarik","Luke","Cameron","Jose","Cole"
			,"LaMarcus","Leandro","Kirk","Will","William","Isaiah","Isaiah","Noah","Adam","Dante","Tim","Corey","Damien",
			"Zach","Zack","Eric","Darius","Greg","Jonah","Lazarus","Kurt","Brandan","Brandon","Branden","Travis","Darrell","Shawn",
			"Jay","DeShawn","Greg","Michael","Mike","Ben","Benjamin","Rasheed","Curtis","Golden","Joseph","Moses","Isaiah","Arthur",
			"Marcus","Izod","Austin","Marshall","Ferg","Greg","CJ","Talib","Youseff","Kirby"]

        self.black_last_names = ["El Arabi","Scott","Jackson","Brown","Jones",
			"Johnson","Williams","Scott","Adams","Davis","Montgomery"
			,"Wade","Chambers","Ferguson","Rice","Tate","Danger","Thomas","Russell","Kerobo",
			"Boyd","White","Black","Watt","Wattson","Leone","Navier","Oday"
			,"Niles","Marvin","Mendez","Naheim","Marcio","Bryant","Bogues","Toure","Bah","Okeke","Sarr","Morris",
			"Brown","Jackson","Aldridge","Barbosa","White","Agustin","Butler","Butler","Cousins","Duncan","Durand",
			"Dedmon","Frye","Ibaka","Joseph","Marion","Morris","Paul","George","Prince","Rubles","Walker","Wright",
			"Williams","Williams","Watson","Zoumia","Tucker","Scott","Jones","Derulo",
            "Success","Omeryu","Cadamuro","Brolin","Paulson","Brown","Black","White","Green"
            "Brown","Perry","Smith","Smith","Jones","Rodgers"]

    def generate_first_name(self, choice):
        if choice == 1:
            return self.white_first_names[random.randint(0,len(self.white_first_names) - 1)]
        else:
            return self.black_first_names[random.randint(0,len(self.black_first_names) - 1)]

    def generate_last_name(self, choice):
        if choice == 1:
            return self.white_last_names[random.randint(0,len(self.white_last_names) - 1)]
        else:
            return self.black_last_names[random.randint(0,len(self.black_last_names) - 1)]