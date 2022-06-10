import os

# Working directory
d = os.path.dirname(os.getcwd())

# Senado files
senado_files = list(range(1,7))

# For filtering?
year = 2022

# Camara o congreso?
corporacion = 'senado'

# Repeated columns
repeated_cols_dict = {
    'boletin': ['Boletín', 'Boletin', 'boletin'],
    'circunscripcion': ['Cicunscripción', 'Circuncscripción', 'Circunscripción'],
    'code_candidato': ['Code_CANDI', 'Code_Candi', 'Code_candidato'],
    'code_circunscripcion': ['CodCircuns', 'Code_Circunscripción', 'Code_CIRCUNSCRIPCIÓN', 'Code_CIRC'],
    'code_citrep': ['CodCITREP', 'Code_CITREP'],
    'code_muni': ['Code_MUNI', 'CodMunicipio'],
    'code_parti': ['Code_PARTI', 'Code_Parti', 'CodPartido'],
    'code_parti_candi': ['Code_PArtiCandi', 'Code_PartiCandi'],
    'comple': ['Compl', 'Comple', 'COMPL'],
    'depto': ['Departamenti', 'Departamento', 'departamento'],
    'municipio': ['Municipiio', 'Municipio'],
    'mesa': ['NumMesa', 'mesa', 'Mesa'],
    'partido': ['Partido', 'partido', 'Nom_Partido'],
    'votos': ['Votos', 'votos']
}

new_names_dict = {
    'boletin': 'numero_boletin',
    'circunscripcion': 'circunscripcion',
    'code_candidato': 'code_candidato',
    'code_circunscripcion': 'code_circunscripcion',
    'code_citrep': 'code_citrep',
    'code_muni': 'codigo_municipio',
    'code_parti': 'code_parti',
    'code_parti_candi': 'code_parti_candi',
    'comple': 'comple',
    'depto': 'depto',
    'municipio': 'municipio',
    'mesa': 'num_mesa',
    'partido': 'nombre_partido',
    'votos': 'numero_votos'
}

incomplete_columns = ['Code_MUNI.1', 'Code_DANE']
base_columns = ['Code_REGIS', 'Zona', 'Puesto', 'Candidato']

