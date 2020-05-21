from pandas import read_csv

def main():
    print('>> Lendo e tratando dataset!')
    
    df = (
        read_csv('data/us-counties-covid-19-dataset.csv')
        .loc[:,['county','cases','deaths']]
        .groupby(['county'],as_index=False)
        .sum()
        .reset_index(drop=True)
    )

    df.to_csv('data/meu_dataset.csv',index=False)
    
    print(f">> Dataset criado em 'data/meu_dataset.csv'\n>> O Dataset possui {df.shape[0]} linhas e {df.shape[1]} colunas.")
    
if __name__ == "__main__":
    main()