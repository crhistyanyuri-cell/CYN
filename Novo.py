import cabeça
"""
SISTEMA DE APRENDIZADO - VERSÃO FUNCIONAL
"""

print("="*60)
print("🧠 SISTEMA DE APRENDIZADO")
print("="*60)

# Dicionário para guardar os exemplos
exemplos = []

# Ensinar exemplos de soma
print("\n📖 Ensinando exemplos básicos...")
exemplos.append((1, 1, 2))
exemplos.append((1, 2, 3))
exemplos.append((2, 1, 3))
exemplos.append((2, 2, 4))
exemplos.append((1, 3, 4))
exemplos.append((3, 1, 4))
exemplos.append((3, 2, 5))
exemplos.append((4, 1, 5))
exemplos.append((1, 4, 5))
exemplos.append((3, 3, 6))
exemplos.append((2, 4, 6))
exemplos.append((4, 2, 6))
exemplos.append((5, 1, 6))
exemplos.append((5, 2, 7))
exemplos.append((2, 5, 7))
exemplos.append((3, 4, 7))
exemplos.append((4, 3, 7))
exemplos.append((7, 7, 14))
exemplos.append((4, 4, 8))
exemplos.append((7, 1, 8))
exemplos.append((5, 3, 8))
exemplos.append((6, 2, 8))
exemplos.append((7, 1, 8))
exemplos.append((3, 5, 8))
exemplos.append((1, 7, 8))
exemplos.append((8, 8, 16))
exemplos.append((8, 1, 9))
exemplos.append((1, 8, 9))
exemplos.append((5, 4, 9))
exemplos.append((4, 5, 9))
exemplos.append((6, 3, 9))
exemplos.append((3, 6, 9))
exemplos.append((7, 2, 9))
exemplos.append((2, 7, 9))
exemplos.append((5, 4, 9))
exemplos.append((4, 5, 9))
exemplos.append((9, 9, 18))
exemplos.append((9, 1, 10))
exemplos.append((1, 9, 10))
exemplos.append((8, 2, 10))
exemplos.append((2, 8, 10))
exemplos.append((7, 3, 10))
exemplos.append((3, 7, 10))
exemplos.append((6, 4, 10))
exemplos.append((4, 6, 10))
exemplos.append((5, 5, 10))
exemplos.append((6, 5, 11))
exemplos.append((5, 6, 11))
exemplos.append((7, 4, 11))
exemplos.append((4, 7, 11))
exemplos.append((8, 3, 11))
exemplos.append((3, 8, 11))
exemplos.append((9, 2, 11))
exemplos.append((2, 9, 11))
exemplos.append((10, 1, 11))
exemplos.append((1, 10, 11))
exemplos.append((10, 2, 12))
exemplos.append((2, 10, 12))
exemplos.append((9, 3, 12))
exemplos.append((3, 9, 12))
exemplos.append((10, 3, 13))
exemplos.append((3, 10, 13))
exemplos.append((9, 4, 13))
exemplos.append((4, 9, 13))
exemplos.append((8, 5, 13))
exemplos.append((5, 8, 13))
exemplos.append((7, 6, 13))
exemplos.append((6, 7, 13))
exemplos.append((8, 5, 13))
exemplos.append((5, 8, 13))
exemplos.append((7, 6, 13))
exemplos.append((6, 7, 13))
exemplos.append((13, 1, 14))
exemplos.append((1, 13, 14))
exemplos.append((12, 2, 14))
exemplos.append((2, 12, 14))
exemplos.append((10, 4, 14))
exemplos.append((4, 10, 14))
exemplos.append((9, 5, 14))
exemplos.append((5, 9, 14))
exemplos.append((6, 8, 14))
exemplos.append((8, 6, 14))
exemplos.append((14, 1, 15))
exemplos.append((1, 14, 15))
exemplos.append((12, 3, 15))
exemplos.append((3, 12, 15))
exemplos.append((15, 0, 15))
exemplos.append((0, 15, 15))
exemplos.append((7, 8, 15))
exemplos.append((8, 7, 15))
exemplos.append((15, 15, 30))
exemplos.append((6, 9, 15))
exemplos.append((9, 6, 15))
exemplos.append((10, 6, 16))
exemplos.append((6, 10, 16))
exemplos.append((15, 1, 16))
exemplos.append((1, 15, 16))
exemplos.append((12, 4, 16))
exemplos.append((4, 12, 16))
exemplos.append((13, 3, 16))
exemplos.append((3, 13, 16))
exemplos.append((14, 2, 16))
exemplos.append((2, 14, 16))
exemplos.append((11, 5, 16))
exemplos.append((5, 11, 16))
exemplos.append((11, 6, 17))
exemplos.append((6, 11, 17))
exemplos.append((10, 7, 17))
exemplos.append((7, 10, 17))
exemplos.append((2, 15, 17))
exemplos.append((15, 2, 17))
exemplos.append((4, 13, 17))
exemplos.append((13, 4, 17))
exemplos.append((14, 3, 17))
exemplos.append((3, 14, 17))
exemplos.append((9, 8, 17))
exemplos.append((8, 9, 17))
exemplos.append((17, 0, 17))
exemplos.append((0, 17, 17))
exemplos.append((17, 1, 18))
exemplos.append((1, 17, 18))
exemplos.append((15, 3, 18))
exemplos.append((3, 15, 18))
exemplos.append((14, 4, 18))
exemplos.append((4, 14, 18))
exemplos.append((13, 5, 18))
exemplos.append((5, 13, 18))
exemplos.append((12, 6, 18))
exemplos.append((6, 12, 18))
exemplos.append((7, 11, 18))
exemplos.append((11, 7, 18))
exemplos.append((18, 1, 19))
exemplos.append((1, 18, 19))
exemplos.append((17, 2, 19))
exemplos.append((2, 17, 19))
exemplos.append((3, 16, 19))
exemplos.append((16, 3, 19))
exemplos.append((15, 4, 19))
exemplos.append((4, 15, 19))
exemplos.append((16, 2, 18))
exemplos.append((2, 16, 18))
exemplos.append((17, 17, 34))
exemplos.append((11, 11, 22))
exemplos.append((10, 10, 20))
exemplos.append((10, 20, 30))
exemplos.append((20, 10, 30))
exemplos.append((5, 7, 12))
exemplos.append((7, 5, 12))
exemplos.append((6, 6, 12))
exemplos.append((8, 4, 12))
exemplos.append((4, 8, 12))

# Ensinar exemplos de multiplicação

print("✅ Exemplos ensinados!\n")

def prever(a, b):
    """Tenta prever o resultado baseado nos exemplos"""
    
    # Primeiro: verifica se tem um exemplo exato
    for x, y, r in exemplos:
        if x == a and y == b:
            return r
    
    # Se não tiver exemplo exato, faz uma média ponderada
    soma_pesos = 0
    soma_resultados = 0
    
    for x, y, r in exemplos:
        # Calcula similaridade (quanto mais próximo, maior o peso)
        distancia = abs(x - a) + abs(y - b)
        if distancia == 0:
            return r
        peso = 1 / (distancia + 1)  # +1 para evitar divisão por zero
        soma_pesos += peso
        soma_resultados += peso * r
    
    if soma_pesos == 0:
        return 0
    
    return soma_resultados / soma_pesos

# Mostrar o que aprendeu
print("📚 O que eu aprendi:")
print("-"*40)
for i, (x, y, r) in enumerate(exemplos, 1):
    print(f"{i}: {x} + {y} = {r}")
print("-"*40)

print("\n💡 Agora você pode fazer perguntas!")
print("📝 Digite 'sair' para encerrar")
print("="*60)

# Loop de perguntas
while True:
    pergunta = input("\n🔢 Digite sua pergunta (ex: 2+3): ").strip()
    
    # Verifica se quer sair
    if pergunta.lower() == 'sair':
        print("\n👋 Até logo!")
        break
    
    # Remove espaços
    pergunta = pergunta.replace(" ", "")
    
    # Verifica se tem o operador +
    if '+' not in pergunta:
        print("❌ Use o formato: 2+3")
        print("💡 Exemplos: 2+3, 10+20, 5+7")
        continue
    
    try:
        # Separa os números
        partes = pergunta.split('+')
        
        # Verifica se tem 2 números
        if len(partes) != 2:
            print("❌ Use apenas 2 números! Ex: 2+3")
            continue
        
        # Converte para números
        a = float(partes[0])
        b = float(partes[1])
        
        # Faz a previsão
        resultado = prever(a, b)
        
        # Mostra o resultado
        print(f"🧠 {a} + {b} = {resultado:.2f}")
        
    except ValueError:
        print("❌ Digite números válidos! Ex: 2+3")
    except Exception as e:
        print(f"❌ Erro: {e}")

input("\nPressione ENTER para sair...")