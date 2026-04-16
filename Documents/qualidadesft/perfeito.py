"""Módulo de teste para validar a aprovação no pipeline de CI com Pylint."""

def exibir_mensagem_sucesso(nome_usuario):
    """Exibe uma mensagem confirmando que o código está no padrão."""
    mensagem = f"Parabéns, {nome_usuario}! O Pylint aprovou este código com nota 10."
    print(mensagem)

if __name__ == "__main__":
    exibir_mensagem_sucesso("Dev")
