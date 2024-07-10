import os

file_path = 'C:/Users/Meu Computador/Downloads/life-expectancy.csv'  


if not os.path.isfile(file_path):
    print(f"File not found: {file_path}")
    exit()


with open(file_path, 'r') as file:
    data = file.readlines()


print("Header line:", data[0])


header = data[0].strip().split(',')
print("Parsed header:", header)


required_columns = ['Year', 'Entity', 'Life expectancy (years)']
missing_columns = [col for col in required_columns if col not in header]
if missing_columns:
    print(f"Missing columns in the header: {missing_columns}")
    exit()


year_idx = header.index('Year')
country_idx = header.index('Entity')
life_exp_idx = header.index('Life expectancy (years)')


overall_min_life_exp = float('inf')
overall_max_life_exp = float('-inf')
overall_min_record = {}
overall_max_record = {}


for line in data[1:]:
    parts = line.strip().split(',')
    try:
        year = int(parts[year_idx])
        country = parts[country_idx]
        life_exp = float(parts[life_exp_idx])
    except ValueError as e:
        print(f"Error parsing line: {line}")
        continue
    
    if life_exp < overall_min_life_exp:
        overall_min_life_exp = life_exp
        overall_min_record = {'year': year, 'country': country, 'life_exp': life_exp}
    
    
    if life_exp > overall_max_life_exp:
        overall_max_life_exp = life_exp
        overall_max_record = {'year': year, 'country': country, 'life_exp': life_exp}


print(f"The overall max life expectancy is: {overall_max_record['life_exp']} from {overall_max_record['country']} in {overall_max_record['year']}")
print(f"The overall min life expectancy is: {overall_min_record['life_exp']} from {overall_min_record['country']} in {overall_min_record['year']}")


try:
    year_of_interest = int(input("Enter the year of interest: "))
except ValueError:
    print("Invalid year input.")
    exit()


total_life_exp = 0
count = 0
year_min_life_exp = float('inf')
year_max_life_exp = float('-inf')
year_min_record = {}
year_max_record = {}


for line in data[1:]:
    parts = line.strip().split(',')
    try:
        year = int(parts[year_idx])
        country = parts[country_idx]
        life_exp = float(parts[life_exp_idx])
    except ValueError as e:
        print(f"Error parsing line: {line}")
        continue
    
    if year == year_of_interest:
        
        total_life_exp += life_exp
        count += 1
        
        
        if life_exp < year_min_life_exp:
            year_min_life_exp = life_exp
            year_min_record = {'country': country, 'life_exp': life_exp}
        
        
        if life_exp > year_max_life_exp:
            year_max_life_exp = life_exp
            year_max_record = {'country': country, 'life_exp': life_exp}
if count > 0:
    average_life_exp = total_life_exp / count
else:
    average_life_exp = None


print(f"For the year {year_of_interest}:")
if average_life_exp is not None:
    print(f"The average life expectancy across all countries was {average_life_exp:.2f}")
    print(f"The max life expectancy was in {year_max_record['country']} with {year_max_record['life_exp']}")
    print(f"The min life expectancy was in {year_min_record['country']} with {year_min_record['life_exp']}")
else:
    print("No data available for this year.")
