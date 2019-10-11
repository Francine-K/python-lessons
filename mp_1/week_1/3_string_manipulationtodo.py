"""
Personality questionnaire
"""
# write a program that asks a user 6 unique questions about them and see if it works!
# use input functions however you would like

print("What is your favorite sport?")
sport = input()
animal = input("What is your favorite animal? ")
sport_output = "Favorite sport: " + sport
animal_output = "Favortie animal: " + animal

print(sport_output)
print(animal_output)

color = input("What is your favorite color?")
college_graduation = input("Where did you graduate college?")
childhood_movie = input("What is your favorite childhood movie?")
food = input("What is your favorite food?")
tv_show = input("What is your favorite tv show?")
city = input("What is your favorite city?")

print("My favorite color is" + color + "I graduated college" + college_graduation + "My favorite movie is" + childhood_movie + "My favorite food" + food + "My favorite tv show is" + tv_show + "My favorite city is" + city)
