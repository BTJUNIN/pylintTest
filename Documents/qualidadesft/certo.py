"""Módulo de validação de qualidade de software para o projeto Pylint."""

def calcular_soma(primeiro_valor, segundo_valor):
    """
    Realiza a soma de dois números e retorna o resultado.
    
    Args:
        primeiro_valor (int/float): O primeiro número.
        segundo_valor (int/float): O segundo número.
    """
    return primeiro_valor + segundo_valor

if __name__ == "__main__":
    RESULTADO_SOMA = calcular_soma(15, 25)
    print(f"A soma dos valores é: {RESULTADO_SOMA}")