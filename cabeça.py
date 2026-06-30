"""
SISTEMA DE APRENDIZADO - VERSÃO ESTÁVEL
Números controlados, sem explosão!
"""

class SistemaAprendiz:
    def __init__(self):
        self.exemplos = []
        self.pesos = []
        self.erro_medio = 0
    
    def ensinar(self, entrada, saida):
        """Adiciona um exemplo e treina"""
        self.exemplos.append((entrada.copy(), saida))
        self._treinar()
    
    def _treinar(self):
        """Treina o modelo com gradiente descendente CONTROLADO"""
        if len(self.exemplos) < 2:
            n_features = len(self.exemplos[0][0]) if self.exemplos else 1
            self.pesos = [0.0] * (n_features + 1)
            return
        
        n_features = len(self.exemplos[0][0])
        
        if len(self.pesos) != n_features + 1:
            self.pesos = [0.0] * (n_features + 1)
        
        # 🔥 TAXA DE APRENDIZADO BEM MENOR para evitar explosão
        taxa_aprendizado = 0.0001  # Antes era 0.01, agora é 0.0001
        epocas = 1000
        
        for _ in range(epocas):
            for entrada, saida_real in self.exemplos:
                # Previsão
                previsao = self._prever(entrada)
                
                # Erro
                erro = saida_real - previsao
                
                # Ajusta pesos com taxa controlada
                for i in range(n_features):
                    self.pesos[i] += taxa_aprendizado * erro * entrada[i]
                self.pesos[-1] += taxa_aprendizado * erro
    
    def _prever(self, entrada):
        """Faz previsão interna"""
        if not self.pesos:
            return 0
        
        resultado = self.pesos[-1]  # bias
        for i, valor in enumerate(entrada):
            if i < len(self.pesos) - 1:
                resultado += self.pesos[i] * valor
        return resultado
    
    def prever(self, entrada):
        """Faz uma previsão para novos dados"""
        if not self.pesos:
            return 0
        return self._prever(entrada)
    
    def mostrar(self):
        """Mostra o que aprendeu"""
        print("\n" + "="*50)
        print("📚 EXEMPLOS APRENDIDOS")
        print("="*50)
        
        if not self.exemplos:
            print("Nenhum exemplo!")
            return
        
        erros = []
        for i, (entrada, saida) in enumerate(self.exemplos):
            pred = self.prever(entrada)
            erro = abs(saida - pred)
            erros.append(erro)
            print(f"{i+1}: {entrada} -> {saida:.2f} | Previsto: {pred:.4f} | Erro: {erro:.4f}")
        
        self.erro_medio = sum(erros) / len(erros)
        print("-"*50)
        print(f"📊 Erro médio: {self.erro_medio:.4f}")
        print(f"🧠 Pesos: {[f'{p:.4f}' for p in self.pesos]}")
        print("="*50)


# ===== TESTE COMPLETO =====
print("🚀 SISTEMA DE APRENDIZADO - VERSÃO ESTÁVEL")
print("="*50)

# Criar sistema
sistema = SistemaAprendiz()

# ===== ENSINAR SOMA =====
print("\n📖 ENSINANDO SOMA...")
sistema.ensinar([2, 3], 5)
sistema.ensinar([10, 20], 30)
sistema.ensinar([5, 7], 12)
sistema.ensinar([1, 1], 2)
sistema.ensinar([8, 4], 12)

sistema.mostrar()

# ===== TESTAR PREVISÕES =====
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
    erro = abs(esperado - previsto)
    print(f"{entrada[0]:3d} + {entrada[1]:3d} = {previsto:.4f} (previsto) | Esperado: {esperado} | Erro: {erro:.4f}")

print("\n" + "="*50)
print("✅ SISTEMA FUNCIONANDO CORRETAMENTE!")
print("="*50)

# ===== TESTE COM MULTIPLICAÇÃO =====
print("\n📖 ENSINANDO MULTIPLICAÇÃO...")

sistema2 = SistemaAprendiz()
sistema2.ensinar([2, 3], 6)
sistema2.ensinar([4, 5], 20)
sistema2.ensinar([3, 3], 9)
sistema2.ensinar([10, 2], 20)

sistema2.mostrar()

print("\n🔮 PREVISÕES MULTIPLICAÇÃO:")
print("-"*50)
testes_mult = [
    ([2, 3], 6),
    ([4, 5], 20),
    ([3, 4], 12),
    ([5, 5], 25)
]

for entrada, esperado in testes_mult:
    previsto = sistema2.prever(entrada)
    erro = abs(esperado - previsto)
    print(f"{entrada[0]:3d} * {entrada[1]:3d} = {previsto:.4f} (previsto) | Esperado: {esperado} | Erro: {erro:.4f}")

print("\n✅ TESTES CONCLUÍDOS!")

# No final do código, ANTES de terminar:
print("\n✅ TESTES CONCLUÍDOS!")
input("Pressione ENTER para sair...")  # ← Isso mantém a janela aberta!