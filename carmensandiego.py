from random import choice
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
animals = [ "dolphin","echidna","rhino","llama","alpaca","penguin","border collie","aardvark","antelope","buffalo","jack russel terrier","cocker spaniel","german shepherd","beagle","basset hound","dalmation","dingo","emu","great dane","kangaroo","pit bull","hairless cat","siamese cat", "hippo","shetland pony","labrador", "chihuahua", "golden retriever", "pomeranian", "gorilla", "weiner dog", "anteater", "capybara", "pigeon", "toucan", "polar bear","corgi","chinchilla","pug","salamander","hamster","hedgehog","iguana","koala","boa constrictor", "tarantula","armadillo", "shiba inu", "spider monkey", "duck", "donkey", "elephant", "badger", "zebra", "fruit bat", "sugar glider", "sloth", "bald eagle","labradoodle" ]
animal = choice(animals)
cities = ["Addis Ababa", "Boston", "Brooklyn", "Bronx", "Cairo", "Chicago", "Dallas", "Djibouti", "Edinburgh", "Glasgow", "Hong Kong", "Johannesburg", "New York", "London", "Los Angeles", "Manhattan", "Paris", "Queens", "San Francisco", "Shanghai", "Timbuktu", "Tulsa"]

periodical_topic = [choice(animals).capitalize(), choice(cities), "Astronomical", "Geographic", "Global", "Historical", "Local", "Martian", "Planetary"]
periodical_type = ["Analysis", "Examinations", "Investigations", "Journal", "Meta-Analysis", "Observations", "Review"]
periodical_time = ["Weekly", "Monthly", "Quarterly"]
periodical = " ".join([choice(periodical_topic), choice(periodical_type), choice(periodical_time)])

stuffcarmensteals = [
"your " + relation + " " + name,
"your " + relation + " " + name,
"your " + relation + " " + name,
"your " + relation + " " + name,
"your " + relation + " " + name,
"your copy of " + periodical,
"your ambition",
"your beanie baby collection",
"your car",
"your dignity",
"your gas",
"your heart",
"your homework",
"your idea for a new blockchain startup",
"your last beer",
"your last ice cube",
"your leftovers",
"your maid",
"your mail",
"your mojo",
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
"your sense of humor",
"your sight",
"your signed Toto Africa 7\"",
"your son",
"your soul",
"your spot in line for coffee",
"your wallet",
"your weed",
"your will to live",
]

toot_text = "OH NO! CARMEN SANDIEGO HAS STOLEN " + choice(stuffcarmensteals) + "!"

status = mastodon.status_post(toot_text)                                                                               
