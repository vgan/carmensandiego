from random import choice, random
from re import sub
from mastodon import Mastodon

basedir = "/home/vgan/carmensandiego/"

mastodon = Mastodon(
        api_base_url='https://botsin.space',
        client_id = basedir + 'carmensandiego_clientcred.txt',
        access_token = basedir + 'carmensandiego_usercred.txt'
)

women = [ "Sally","Susan","Maureen","Melinda","Brenda","Lisa","Bridget","Laura","Cindy","Louise","Marsha","Nora","Beth","Belinda","Terry","Patty","Penelope","Betty","Gertrude","Nancy","Julia","Mindy","Mandy" ]
woman = choice(women)
men = [ "Mike","Dave","Ron","Gary","Allen","Peter","Brent","Brad","Dennis","Barry","Terry","Gordan","Jerome","Phil","Steve","Seth","Jerry","Angus","Skyler","Zane","Kevin","Bart","Waldo","Ralph","Drew","Larry","Lester","Marcus" ]
man = choice(men)

chance_of_jorts = 0.05 # 1 in 20
genders = [ 0,1 ]
gender = choice(genders)
if gender == 0:
        name = man
else:
        name = woman
relations = [[ "nephew", "niece" ],["brother","sister"],["uncle","auntie"]]
niece = relations[0][gender]
sister = relations[1][gender]
auntie = relations[2][gender]
relation = choice([niece,sister,auntie])
animals = [ "porg","dolphin","echidna","rhino","llama","alpaca","penguin","border collie","aardvark","antelope","buffalo","jack russel terrier","cocker spaniel","german shepherd","beagle","basset hound","dalmation","dingo","emu","great dane","kangaroo","pit bull","hairless cat","siamese cat", "hippo","shetland pony","labrador", "chihuahua", "golden retriever", "pomeranian", "gorilla", "wiener dog", "anteater", "capybara", "pigeon", "toucan", "polar bear","corgi","chinchilla","pug","salamander","hamster","hedgehog","iguana","koala","boa constrictor", "tarantula","armadillo", "shiba inu", "spider monkey", "duck", "donkey", "elephant", "badger", "zebra", "fruit bat", "sugar glider", "sloth", "bald eagle","labradoodle" ]
animal = choice(animals)
cities = ["Addis Ababa", "Boston", "Brooklyn", "Bronx", "Cairo", "Chicago", "Dallas", "Djibouti", "Edinburgh", "Glasgow", "Hong Kong", "Johannesburg", "New York", "London", "Los Angeles", "Manhattan", "Paris", "Queens", "San Francisco", "Shanghai", "Timbuktu", "Tulsa"]

periodical_topic = [choice(animals).title(), choice(cities), "Astronomical", "Geographic", "Global", "Historical", "Local", "Martian", "Planetary"]
periodical_type = ["Analysis", "Examinations", "Investigations", "Journal", "Meta-Analysis", "Observations", "Review"]
periodical_time = ["Daily", "Weekly", "Monthly", "Quarterly"]
periodical = " ".join([choice(periodical_topic), choice(periodical_type), choice(periodical_time)])

newspaper_brand = ["Globe", "World", "Times", "Tribune", "Post", "Dispatch", "Journal"]
newspaper = " ".join(["The", choice(cities), choice(periodical_topic)])

stuffcarmensteals = [
"your " + relation + " " + name,
"your " + relation + " " + name,
"your " + relation + " " + name,
"your " + relation + " " + name,
"your 9/11 edition of " + newspaper,
"your copy of " + periodical,
"your copy of today\'s " + newspaper,
"your ambition",
"your beanie baby collection",
"your beach cruiser",
"your boyfriend",
"your car",
"your dignity",
"your favorite hat",
"your favorite jacket",
"your favorite pants",
"your favorite shirt",
"your favorite sweater",
"your friends",
"your gas",
"your girlfriend",
"your heart",
"your homework",
"your house",
"your idea for a blockchain startup",
"your idea for a new cryptocurrency",
"your identity",
"your job",
"your last beer",
"your last hot pocket",
"your last ice cube",
"your lawnmower",
"your leftovers",
"your mech",
"your mojo",
"your moped",
"your motivation",
"your pants",
"your parking spot",
"your prized copy of " + periodical,
"your " + animal,
"your " + animal,
"your " + animal,
"your " + animal,
"your " + animal,
"your rare edition of " + periodical,
"your sanity",
"your scotch",
"your seat",
"your sense of humor",
"your shorts",
"your sight",
"your signed Toto Africa 7\"",
"your social security number",
"your soul",
"your spot in line for coffee",
"your subscription to " + newspaper,
"your vape pen",
"your wallet",
"your watch",
"your will to live",
]

thing_stolen = choice(stuffcarmensteals)

if random() < chance_of_jorts:
    thing_stolen = sub('^your ([bcdfghk-np-tv-z][bcdfghj-np-tv-z]?|)(?!j)(\w+)$',
                       'your j\\2 (jean \\1\\2)',
                       thing_stolen)

toot_text = "OH NO! CARMEN SANDIEGO HAS STOLEN " + thing_stolen + "!"

status = mastodon.status_post(toot_text)                                                                               
