import shutil


def copia_arq (nome_arquivo):
    shutil.copy(nome_arquivo, 'C:/Projetos/globallabs/')


def move_arq (nome_arquivo):
    shutil.copy(nome_arquivo, 'C:/Projetos/globallabs/notas_aluno')