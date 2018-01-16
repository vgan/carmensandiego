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
relation + " " + name,
relation + " " + name,
relation + " " + name,
relation + " " + name,
"9/11 edition of " + newspaper,
"copy of " + periodical,
"copy of today\'s " + newspaper,
"ambition",
"baby shoes",
"beanie baby collection",
"beach cruiser",
"boyfriend",
"car",
"dignity",
"favorite hat",
"favorite jacket",
"favorite pants",
"favorite shirt",
"favorite sweater",
"friends",
"gas",
"girlfriend",
"heart",
"homework",
"house",
"idea for a blockchain startup",
"idea for a new cryptocurrency",
"identity",
"job",
"last beer",
"last hot pocket",
"last ice cube",
"lawnmower",
"leftovers",
"meme",
"mech",
"mojo",
"moped",
"motivation",
"oats",
"pants",
"parking spot",
"pineapple",
"prized copy of " + periodical,
"pronouns",        
animal,
animal,
animal,
animal,
animal,
"rare edition of " + periodical,
"sanity",
"scotch",
"seat",
"sense of humor",
"sight",
"signed Toto Africa 7\"",
"social security number",
"soul",
"spot in line for coffee",
"subscription to " + newspaper,
"vape pen",
"wallet",
"watch",
"will to live",
]

thing_stolen = choice(stuffcarmensteals)

if random() < chance_of_jorts:
    thing_stolen = sub('^([bcdfghk-np-tv-z][bcdfghj-np-tv-z]?|)(?!j)(\w+)$',
                       'j\\2 (jean \\1\\2)',
                       thing_stolen)

toot_text = "OH NO! CARMEN SANDIEGO HAS STOLEN YOUR " + thing_stolen + "!"

status = mastodon.status_post(toot_text)                                                                               
