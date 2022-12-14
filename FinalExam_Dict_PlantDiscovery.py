number_of_information = int(input())
my_plants = {}

for receiving in range(number_of_information):
    information_for_plants = input().split("<->")
    plant_name = information_for_plants[0]
    rarity = information_for_plants[1]
    my_plants[plant_name] = [rarity, []]   #така се подрежда по удбно-ключ и вложен лист

exhibition = False

while not exhibition:
    commands = input()

    if commands == "Exhibition":
        exhibition = True
        break

    commands = commands.split(": ")
    current_command = commands[0]

    if current_command == "Rate":
        plant_for_rate = commands[1].split(" - ")[0]
        rating = int(commands[1].split(" - ")[1])
        if plant_for_rate in my_plants:
            my_plants[plant_for_rate][1].append(rating)
        else:
            print("error")

    elif current_command == "Update":
        plant_for_update = commands[1].split(" - ")[0]
        plant_rarity = commands[1].split(" - ")[1]
        if plant_for_update in my_plants:
            my_plants[plant_for_update][0] = plant_rarity
        else:
            print("error")

    elif current_command == "Reset":
        plant_for_reset = commands[1]
        if plant_for_reset in my_plants:
            my_plants[plant_for_reset][1] = []
        else:
            print("error")

print("Plants for the exhibition:")

for plant in my_plants:
    if len(my_plants[plant][1]) > 0:
        rating_current_plant = sum(my_plants[plant][1]) / len(my_plants[plant][1])
    else:
        rating_current_plant = 0
    print(f"- {plant}; Rarity: {my_plants[plant][0]}; Rating: {rating_current_plant:.2f}")


# МОЯ СИ НАЧИН!!!

# n = int(input())
# plants = {}
#
# for _ in range(n):
#     data = input().split("<->")
#     plants[data[0]] = {'rarity': int(data[1]), 'rating': []}
#
# command = input()
#
# while command != "Exhibition":
#     data = command.split(": ")
#     action = data[0]
#
#     if action == "Rate":
#         new_data = data[1].split(" - ")
#         flower = new_data[0]
#         rating = int(new_data[1])
#
#         if flower in plants:
#             plants[flower]['rating'].append(rating)
#
#         else:
#             print("error")
#
#     elif action == "Update":
#         new_data = data[1].split(" - ")
#         flower = new_data[0]
#         rarity = int(new_data[1])
#         if flower in plants:
#             plants[flower]['rarity'] = rarity
#         else:
#             print("error")
#
#     elif action == "Reset":
#         flower = data[1]
#         if flower in plants:
#             plants[flower]['rating'].clear()
#             plants[flower]['rating'] = [0]
#         else:
#             print("error")
#
#     command = input()
#
# print("Plants for the exhibition:")
# for flower in plants:
#     if len(plants[flower]['rating']) > 0:
#         average_rating = sum(plants[flower]['rating']) / len(plants[flower]['rating'])
#     else:
#         average_rating = 0
#     print(f"- {flower}; Rarity: {plants[flower]['rarity']}; Rating: {average_rating:.2f}")