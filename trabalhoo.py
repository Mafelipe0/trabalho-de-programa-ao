biblioteca = {}
#eu e minha equipe vamos criar uma biblioteca nem intuitiva com 7 opções para o usuário 

# a primeira opção é para o usuário adicionar o livro a biblioteca 

def adicionar_livro(titulo, autor, ano_publicacao, disponibilidade):
    biblioteca[titulo] = {  
        'autor': autor,
        'ano_publicacao': ano_publicacao,
        'disponibilidade': disponibilidade
    }
    print(f'O livro "{titulo}" foi adicionado com sucesso.')

# a função de atualizar e para o usuário fazer mudanças no titulo,autor ou a data de lançamento 

def atualizar_livro(titulo, autor=None, ano_publicacao=None, disponibilidade=None):
    if titulo in biblioteca:  
        if autor:  
            biblioteca[titulo]['autor'] = autor
        if ano_publicacao:  
            biblioteca[titulo]['ano_publicacao'] = ano_publicacao
        if disponibilidade:  
            biblioteca[titulo]['disponibilidade'] = disponibilidade
        print(f'Informações do livro "{titulo}" foram atualizadas com sucesso.')
    else:
        print(f'O livro "{titulo}" não foi encontrado na biblioteca.')
# a opção de remover e para o usuário tirar um livro da sua biblioteca 
def remover_livro(titulo):
    if titulo in biblioteca:  
        del biblioteca[titulo]  
        print(f'O livro "{titulo}" foi removido da biblioteca.')
    else:
        print(f'O livro "{titulo}" não foi encontrado na biblioteca.')

# essa opção é para exibir todos os livros que tem na biblioteca 

def exibir_livros():
    if len(biblioteca) == 0:  
        Print('A biblioteca está vazia.')
    else:
        for titulo, info in biblioteca.items():  
            print(f'Título: {titulo}')
            print(f'Autor: {info["autor"]}')
            print(f'Ano de Publicação: {info["ano_publicacao"]}')
            print(f'Disponibilidade: {"Disponível" if info["disponibilidade"] else "Indisponível"}')
            print('---')
#sabemos que todos os leitores fazer avaliações para os seus livros e fizermos uma Função onde o usuário pode avaliar o livro que leu 

def adicionar_avaliacao(titulo, avaliacao):
    if titulo in biblioteca:
        if 'avaliacoes' not in biblioteca[titulo]:
            biblioteca[titulo]['avaliacoes'] = []
        biblioteca[titulo]['avaliacoes'].append(avaliacao)
        print(f'Avaliação adicionada ao livro "{titulo}"')
    else:
        print(f'O livro "{titulo}" não foi encontrado na biblioteca.')

#essa Função e para ver as avaliações dos livros que tem na sua biblioteca 

def exibir_avaliacoes(titulo):
    if titulo in biblioteca and 'avaliacoes' in biblioteca[titulo]:
        print(f'Avaliações do livro "{titulo}":')
        for avaliacao in biblioteca[titulo]['avaliacoes']:
            print(f'- {avaliacao}')
    else:
        print(f'O livro "{titulo}" não possui avaliações.')

#fizemos um menu bem simples e prático de usar

while True:
    print('1 - Adicionar livro')
    print('2 - Atualizar livro')
    print('3 - Remover livro')
    print('4 - Exibir livros')
    print('5 - Adicionar avaliação')
    print('6 - Exibir avaliações')
    print('7 - Sair')

    opcao = input('Escolha uma opção: ')  

    if opcao == '1':
        titulo = input('Digite o título do livro: ')
        autor = input('Digite o nome do autor: ')
        ano = input('Digite o ano de publicação: ')
        disponibilidade = input('O livro está disponível? (S/N): ')
        adicionar_livro(titulo, autor, ano, disponibilidade.upper() == 'S')

    elif opcao == '2':
        titulo = input('Digite o título do livro que deseja atualizar: ')
        autor = input('Digite o novo autor (ou pressione Enter para manter o atual): ')
        ano = input('Digite o novo ano de publicação (ou pressione Enter para manter o atual): ')
        disponibilidade = input('O livro está disponível? (S/N - ou pressione Enter para manter o atual): ')
        atualizar_livro(titulo, autor if autor else None, ano if ano else None, disponibilidade.upper() == 'S' if disponibilidade else None)

    elif opcao == '3':
        titulo = input('Digite o título do livro que deseja remover: ')
        remover_livro(titulo)

    elif opcao == '4':
        exibir_livros()

    elif opcao == '5':
        titulo = input('Digite o título do livro para adicionar a avaliação: ')
        avaliacao = input('Digite a avaliação: ')
        adicionar_avaliacao(titulo, avaliacao)

    elif opcao == '6':
        titulo = input('Digite o título do livro para exibir as avaliações: ')
        exibir_avaliacoes(titulo)

    elif opcao == '7':
        print('Saindo...')
        break

    else:
        print('Opção inválida. Por favor, escolha uma opção válida.')