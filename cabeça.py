"""
SISTEMA DE APRENDIZADO SIMPLES - SEM BIBLIOTECAS EXTERNAS
Funciona em qualquer Python, sem instalação!
"""

class SistemaAprendiz:
    def __init__(self):
        self.exemplos = []  # Armazena (entrada, saida)
        self.pesos = []     # Pesos do modelo
    
    def ensinar(self, entrada, saida):
        """
        Ensina um novo exemplo ao sistema
        entrada: lista de números [x1, x2, x3, ...]
        saida: número (resultado esperado)
        """
        self.exemplos.append((entrada.copy(), saida))
        self._treinar()
    
    def _treinar(self):
        """Treina o modelo usando regressão linear com gradiente descendente"""
        if len(self.exemplos) < 2:
            # Inicializa pesos com valores pequenos
            n_features = len(self.exemplos[0][0]) if self.exemplos else 1
            self.pesos = [0.1] * (n_features + 1)  # +1 para o bias
            return
        
        # Número de características (entradas)
        n_features = len(self.exemplos[0][0])
        
        # Inicializa pesos se necessário
        if len(self.pesos) != n_features + 1:
            self.pesos = [0.1] * (n_features + 1)
        
        # Gradiente descendente
        taxa_aprendizado = 0.01
        epocas = 500
        
        for _ in range(epocas):
            for entrada, saida_real in self.exemplos:
                # Previsão: soma(pesos[i] * entrada[i]) + bias
                previsao = self._prever_interno(entrada)
                
                # Erro
                erro = saida_real - previsao
                
                # Atualiza pesos
                for i in range(n_features):
                    self.pesos[i] += taxa_aprendizado * erro * entrada[i]
                self.pesos[-1] += taxa_aprendizado * erro * 1.0  # bias
    
    def _prever_interno(self, entrada):
        """Faz previsão interna (sem verificação)"""
        if not self.pesos:
            return 0
        resultado = self.pesos[-1]  # bias
        for i, valor in enumerate(entrada):
            if i < len(self.pesos) - 1:
                resultado += self.pesos[i] * valor
        return resultado
    
    def prever(self, entrada):
        """Faz uma previsão para novos dados"""
        if not self.exemplos:
            return 0
        
        # Verifica se entrada tem o mesmo tamanho dos exemplos
        if len(entrada) != len(self.exemplos[0][0]):
            print(f"⚠️ Entrada deve ter {len(self.exemplos[0][0])} números")
            return 0
        
        return self._prever_interno(entrada)
    
    def mostrar_exemplos(self):
        """Mostra todos os exemplos aprendidos"""
        print("\n" + "="*50)
        print("📚 EXEMPLOS APRENDIDOS")
        print("="*50)
        for i, (entrada, saida) in enumerate(self.exemplos):
            pred = self._prever_interno(entrada)
            erro = abs(saida - pred)
            print(f"Exemplo {i+1}: {entrada} -> {saida}")
            print(f"           Previsto: {pred:.3f} | Erro: {erro:.3f}")
        print("-"*50)
        
        if self.pesos:
            print("🧠 PESOS DO MODELO:")
            for i, peso in enumerate(self.pesos[:-1]):
                print(f"   Peso {i+1}: {peso:.4f}")
            print(f"   Bias: {self.pesos[-1]:.4f}")
        print("="*50)
    
    def avaliar(self, testes):
        """Avalia o sistema com dados de teste"""
        print("\n📊 AVALIAÇÃO")
        print("-"*50)
        erros = []
        for entrada, saida_esperada in testes:
            saida_prevista = self.prever(entrada)
            erro = abs(saida_esperada - saida_prevista)
            erros.append(erro)
            print(f"Entrada: {entrada}")
            print(f"  Esperado: {saida_esperada:.3f}")
            print(f"  Previsto: {saida_prevista:.3f}")
            print(f"  Erro: {erro:.3f}")
            print()
        
        erro_medio = sum(erros) / len(erros)
        print(f"✅ ERRO MÉDIO: {erro_medio:.4f}")
        print(f"✅ ACURÁCIA: {max(0, 100 - erro_medio*10):.1f}%")
        print("="*50)


# ====================================================
# TESTANDO O SISTEMA
# ====================================================

print("🚀 SISTEMA DE APRENDIZADO MATEMÁTICO")
print("="*50)

# Criar sistema
sistema = SistemaAprendiz()

# ===== TESTE 1: APRENDER SOMA =====
print("\n📖 ENSINANDO SOMA (a + b = c)")
print("-"*50)

# Ensinar exemplos de soma
sistema.ensinar([2, 3], 5)      # 2 + 3 = 5
sistema.ensinar([10, 20], 30)   # 10 + 20 = 30
sistema.ensinar([5, 7], 12)     # 5 + 7 = 12
sistema.ensinar([1, 1], 2)      # 1 + 1 = 2
sistema.ensinar([8, 4], 12)     # 8 + 4 = 12

sistema.mostrar_exemplos()

# Testar previsões
print("\n🔮 PREVISÕES:")
print("-"*50)
testes = [
    ([4, 6], 10),
    ([100, 50], 150),
    ([3, 4], 7),
    ([8, 2], 10),
    ([0, 5], 5)
]

for entrada, esperado in testes:
    previsto = sistema.prever(entrada)
    print(f"{entrada[0]} + {entrada[1]} = {previsto:.2f} (previsto) | Esperado: {esperado} | Erro: {abs(esperado-previsto):.2f}")

# ===== TESTE 2: APRENDER MULTIPLICAÇÃO =====
print("\n\n📖 ENSINANDO MULTIPLICAÇÃO (a * b = c)")
print("-"*50)

sistema2 = SistemaAprendiz()
sistema2.ensinar([2, 3], 6)
sistema2.ensinar([4, 5], 20)
sistema2.ensinar([3, 3], 9)
sistema2.ensinar([10, 2], 20)
sistema2.ensinar([5, 6], 30)

sistema2.mostrar_exemplos()

print("\n🔮 PREVISÕES:")
print("-"*50)
testes_mult = [
    ([2, 3], 6),
    ([4, 5], 20),
    ([3, 4], 12),
    ([5, 5], 25),
    ([10, 10], 100)
]

for entrada, esperado in testes_mult:
    previsto = sistema2.prever(entrada)
    print(f"{entrada[0]} * {entrada[1]} = {previsto:.2f} (previsto) | Esperado: {esperado} | Erro: {abs(esperado-previsto):.2f}")

# ===== TESTE 3: APRENDER FUNÇÃO QUADRÁTICA =====
print("\n\n📖 ENSINANDO FUNÇÃO QUADRÁTICA (x²)")
print("-"*50)

sistema3 = SistemaAprendiz()
sistema3.ensinar([1], 1)
sistema3.ensinar([2], 4)
sistema3.ensinar([3], 9)
sistema3.ensinar([4], 16)
sistema3.ensinar([5], 25)

sistema3.mostrar_exemplos()

print("\n🔮 PREVISÕES:")
print("-"*50)
for x in [1.5, 2.5, 3.5, 6]:
    previsto = sistema3.prever([x])
    esperado = x**2
    print(f"x = {x} -> {previsto:.2f} (previsto) | Esperado: {esperado:.2f} | Erro: {abs(esperado-previsto):.2f}")

print("\n✅ SISTEMA FUNCIONANDO SEM BIBLIOTECAS EXTERNAS!")
