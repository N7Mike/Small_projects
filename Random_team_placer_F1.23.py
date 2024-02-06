import random as ran

teams_list = ['Merc', 'Farrari', 'Mclaren', 'Aston martin', 'Apline',
         'red bull', 'aplha tauri', 'aplha remao', 'Haas', 'Wiliams']

people = [] # list of people
num = 1
for i in range(20):
    user = input(f'Racer Name {num}: ')
    num += 1
    people.append(user)
    print(people)

ran.shuffle(people)

team_num = 0
people_num = 0

for i in range(10):

    print(f'{people[people_num:people_num + 1]} and {people[people_num + 1:people_num + 2]} is in {teams_list[team_num]}')
    team_num += 1
    people_num += 2