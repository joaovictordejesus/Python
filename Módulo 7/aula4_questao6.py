import csv
def analisar_musicas():
    with open("spotify-2023.csv", "r", encoding='latin-1') as file:
        leitor = csv.DictReader(file)
        musicas = list(leitor)
    anos = range(2012, 2023)
    top_musicas = []

    for ano in anos:
        musicas_do_ano = [musica for musica in musicas if int(musica['released_year']) == ano]
        if musicas_do_ano:
            musica_top = max(musicas_do_ano, key=lambda x: int(x['streams']))
            top_musicas.append([
                musica_top['track_name'], 
                musica_top['artist(s)_name'], 
                musica_top['released_year'], 
                int(musica_top['streams'])
            ])
    print(top_musicas)
analisar_musicas()