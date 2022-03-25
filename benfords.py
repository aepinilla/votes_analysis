
from benfordslaw import benfordslaw
from read_data import read_data

bl = benfordslaw(alpha=0.05)

senado_df = read_data()

usable_data = senado_df[['Departamento', 'Municipio', 'Zona', 'Puesto', 'NumMesa', 'Circunscripción', 'Nom_Partido', 'Candidato', 'Votos']].reset_index(drop=True)
usable_data = usable_data.dropna()

partidos = list(usable_data.Nom_Partido.unique())

benfords_test = {}
for p in partidos:
    X = usable_data['Votos'].loc[usable_data['Nom_Partido'] == p].values
    results = bl.fit(X)
    benfords_test[p] = results

print(benfords_test)