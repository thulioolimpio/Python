import pandas as pd

# Função para carregar o dataset
def load_data(file_path):
    return pd.read_csv(file_path)

# Função para encontrar os extremos de expectativa de vida
def find_extremes(data):
    min_life_exp = data['Life expectancy'].min()
    max_life_exp = data['Life expectancy'].max()
    
    min_row = data[data['Life expectancy'] == min_life_exp]
    max_row = data[data['Life expectancy'] == max_life_exp]
    
    min_info = (min_row['Year'].values[0], min_row['Country'].values[0], min_life_exp)
    max_info = (max_row['Year'].values[0], max_row['Country'].values[0], max_life_exp)
    
    return min_info, max_info

# Função para analisar o ano específico fornecido pelo usuário
def analyze_year(data, year):
    year_data = data[data['Year'] == year]
    
    if year_data.empty:
        return None, None, None
    
    avg_life_exp = year_data['Life expectancy'].mean()
    min_row = year_data[year_data['Life expectancy'] == year_data['Life expectancy'].min()]
    max_row = year_data[year_data['Life expectancy'] == year_data['Life expectancy'].max()]
    
    min_info = (min_row['Country'].values[0], min_row['Life expectancy'].values[0])
    max_info = (max_row['Country'].values[0], max_row['Life expectancy'].values[0])
    
    return avg_life_exp, min_info, max_info

def main():
    # Baixar e carregar o dataset
    file_path = 'C:/Users/Meu Computador/Downloads/life-expectancy.csv'  # Insira o caminho correto do arquivo CSV aqui
    data = load_data(file_path)
    
    # Encontrar os extremos no dataset
    min_info, max_info = find_extremes(data)
    
    print(f"A menor expectativa de vida é: {min_info[2]:.2f} de {min_info[1]} em {min_info[0]}")
    print(f"A maior expectativa de vida é: {max_info[2]:.2f} de {max_info[1]} em {max_info[0]}")
    
    # Interação com o usuário
    year = int(input("Digite o ano de interesse: "))
    avg_life_exp, min_info, max_info = analyze_year(data, year)
    
    if avg_life_exp is None:
        print(f"Não há dados disponíveis para o ano {year}.")
    else:
        print(f"Para o ano {year}:")
        print(f"A expectativa de vida média foi {avg_life_exp:.2f}")
        print(f"A menor expectativa de vida foi em {min_info[0]} com {min_info[1]:.2f}")
        print(f"A maior expectativa de vida foi em {max_info[0]} com {max_info[1]:.2f}")

if __name__ == "__main__":
    main()