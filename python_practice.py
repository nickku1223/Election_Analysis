counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

counties_dict = {}

counties_dict["Aparahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438

print(counties_dict)

for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

voting_data = [{"county":"Aparahoe", "registered_voters":422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}] 


for county_dict in voting_data:
    print (county_dict)

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")