import random

# teamplates
def template_one(number, measure_of_time, mode_of_transportation, adjective,
                adjective2, noun, color, part_of_body, verb, number2, noun2,
                noun3, part_of_body2, verb1, noun4, adjective3, silly_word, noun5):
    
    print(f'It was about {number} {measure_of_time} ago when I arrived at the hospital in a {mode_of_transportation}. The hospital is a/an {adjective} place, there are a lot of {adjective2} {noun} here. There are nurses here who have {color} {part_of_body}. If someone wants to come into my room I told them that they have to {verb1} first. I’ve decorated my room with {number2} {noun2}. Today I talked to a doctor and they were wearing a {noun3} on their {part_of_body2}. I heard that all doctors {verb} {noun4} every day for breakfast. The most {adjective3} thing about being in the hospital is the {silly_word} {noun5}!')

def template_two(person_name, noun, adjective_feeling, verb, adjective_feeling2,
                animal, verb2, color, verb_ending_in_ing, adverb_ending_in_ly,
                number, measure_of_time, color2, animal2, number2, silly_word, noun2):
    
    print(f'This weekend I am going camping with {person_name}. I packed my lantern, sleeping bag, and {noun}. I am so {adjective_feeling} to {verb} in a tent. I am {adjective_feeling2} we might see a(n) {animal}, I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {verb2}. I have heard that the {color} lake is great for {verb_ending_in_ing}. Then we will {adverb_ending_in_ly} hike through the forest for {number} {measure_of_time}. If I see a {color2} {animal2} while hiking, I am going to bring it home as a pet! At night we will tell {number2} {silly_word} stories and roast {noun2} around the campfire!')

def template_three(person_name, adjective, color, animal, place,
                  adjective2, magical_creature_plural, adjective3, magical_creature_plural2,
                  room_in_a_house, noun, noun2, noun_plural3, adjective4, noun_plural4,
                  number, measure_of_time, verb_ending_in_ing, adjective5, noun5):
    
    print(f'Dear {person_name}, I am writing to you from a {adjective} castle in an enchanted forest. I found myself here one day after going for a ride on a {color} {animal} in {place}. There are {adjective2} {magical_creature_plural} and {adjective3} {magical_creature_plural2} here! In the {room_in_a_house} there is a pool full of {noun}. I fall asleep each night on a {noun2} of {noun_plural3} and dream of {adjective4} {noun_plural4}. It feels as though I have lived here for {number} {measure_of_time}. I hope one day you can visit, although the only way to get here now is {verb_ending_in_ing} on a {adjective5} {noun5}!')


tries = 3
selected_template = None

# giving a user time until they use all tries
while tries > 0:
    template_choice = int(input("Choose a template (1, 2, or 3): "))
    
    if template_choice in [1, 2, 3]:
        selected_template = template_choice
        break

    else:
        tries -=  1
        print(f"Please choose a number from 1 to 3 (Selecting randomly after {tries} tries):")

# user consumed every try = random template
if not selected_template:
    selected_template = random.randint(1, 3)
    print(f"Out of tries. Randomly selecting template: {selected_template}.")

# getting user inputs and placing them in a story
if selected_template == 1:
    template_one(
        number = input("Input a number: "),
        measure_of_time = input("Measure of time: "),
        mode_of_transportation = input("Input a mode of transportation: "),
        adjective = input("Input an adjective: "),
        adjective2 = input("Input another adjective: "),
        noun = input("Input a noun: "),
        color = input("Input a color: "),
        part_of_body = input("Input a part of the body: "),
        verb = input("Input a verb: "),
        number2 = input("Input a number: "),
        noun2 = input("Input a noun: "),
        noun3 = input("Input another noun: "),
        part_of_body2 = input("Input a part of the body: "),
        verb1 = input("Input a verb: "),
        noun4 = input("Input a noun: "),
        adjective3 = input("Input an adjective3: "),
        silly_word = input("Input a silly word: "),
        noun5 = input("Input a noun: ")
    )

elif selected_template == 2:
    template_two(
        person_name = input("Input a Person's name: "),
        noun = input("Input a noun: "),
        adjective_feeling = input("Input an adjective(feeling): "),
        verb = input("Input a verb: "),
        adjective_feeling2 = input("Input an adjective2(feeling): "),
        animal = input("Input an animal: "),
        verb2 = input("Input a verb: "),
        color = input("Input a color: "),
        verb_ending_in_ing = input("Input a verb (ending in ing): "),
        adverb_ending_in_ly = input("Input an adverb (ending in ly): "),
        number = input("Input number: "),
        measure_of_time = input("Input a measure_of_time: "),
        color2 = input("Input a color: "),
        animal2 = input("Input another animal: "),
        number2 = input("Input another number: "),
        silly_word = input("Input silly word: "),
        noun2 = input("Input another noun: ")
    )

elif selected_template == 3:
    template_three(
        person_name = input("Input a Person's name: "),
        adjective = input("Input an adjective (feeling): "),
        color = input("Input a color: "),
        animal = input("Input an animal: "),
        place = input("Input a place: "),
        adjective2 = input("Input an adjective: "),
        magical_creature_plural = input("Input a magical creature (Plural): "),
        adjective3 = input("Input a adjective3: "),
        magical_creature_plural2 = input("Input another magical creature (Plural): "),
        room_in_a_house = input("Input a room in a house: "),
        noun = input("Input a noun: "),
        noun2 = input("Input another noun: "),
        noun_plural3 = input("Input yet another noun (plural): "),
        adjective4 = input("Input an adjective: "),
        noun_plural4 = input("Input one more noun (plural): "),
        number = input("Input a number: "),
        measure_of_time = input("Input a measure_of_time: "),
        verb_ending_in_ing = input("Input a verb: "),
        adjective5 = input("Input an adjective: "),
        noun5 = input("Input last noun: ")
    )
