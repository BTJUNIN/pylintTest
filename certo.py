"""Módulo principal para testar a aprovação no pipeline do GitHub Actions."""

def saudacao_personalizada(nome, idade):
    """
    Gera e exibe uma mensagem de saudação validada pelo Pylint.

    Args:
        nome (str): O nome do usuário.
        idade (int): A idade do usuário.
    """
    mensagem = f"Olá, {nome}! Você tem {idade} anos. Código validado com sucesso!"
    print(mensagem)

if __name__ == "__main__":
    saudacao_personalizada("Dev", 25)