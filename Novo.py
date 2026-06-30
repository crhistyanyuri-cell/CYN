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
exemplos.append((2, 3, 5))
exemplos.append((4, 1, 5))
exemplos.append((1, 4, 5))
exemplos.append((10, 20, 30))
exemplos.append((5, 7, 12))
exemplos.append((1, 1, 2))
exemplos.append((8, 4, 12))

# Ensinar exemplos de multiplicação
exemplos.append((2, 3, 6))
exemplos.append((4, 5, 20))
exemplos.append((3, 3, 9))
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