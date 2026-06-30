
import cabeça
cabeça. SistemaAprendiz
"""
SISTEMA DE APRENDIZADO - VERSÃO CORRIGIDA
Com tratamento de erros e mais estável!
"""

class SistemaAprendiz2:
    def __init__(self, nome="Sistema"):
        self.nome = nome
        self.exemplos = []
        self.pesos = []
        self.operacao = "geral"
        self.erro_medio = 0
        self.historico = []
    
    def ensinar(self, entrada, saida):
        self.exemplos.append((entrada.copy(), saida))
        self._treinar()
    
    def _treinar(self):
        if len(self.exemplos) < 2:
            n_features = len(self.exemplos[0][0]) if self.exemplos else 1
            self.pesos = [0.0] * (n_features + 1)
            return
        
        n_features = len(self.exemplos[0][0])
        
        if len(self.pesos) != n_features + 1:
            self.pesos = [0.0] * (n_features + 1)
        
        taxa_aprendizado = 0.001
        epocas = 2000
        
        for _ in range(epocas):
            for entrada, saida_real in self.exemplos:
                previsao = self._prever(entrada)
                erro = saida_real - previsao
                
                for i in range(n_features):
                    self.pesos[i] += taxa_aprendizado * erro * entrada[i]
                self.pesos[-1] += taxa_aprendizado * erro
    
    def _prever(self, entrada):
        if not self.pesos:
            return 0
        
        resultado = self.pesos[-1]
        for i, valor in enumerate(entrada):
            if i < len(self.pesos) - 1:
                resultado += self.pesos[i] * valor
        return resultado
    
    def prever(self, entrada):
        if not self.pesos:
            return 0
        return self._prever(entrada)
    
    def perguntar(self, pergunta):
        """Processa uma pergunta do usuário com TRATAMENTO DE ERROS"""
        pergunta = pergunta.strip()
        
        # Remove espaços extras
        pergunta = pergunta.replace(" ", "")
        
        # Se estiver vazio, retorna mensagem
        if not pergunta:
            return "❌ Digite algo! Ex: 2+3"
        
        try:
            # Verifica se tem operador
            operador = None
            if '+' in pergunta:
                operador = '+'
                partes = pergunta.split('+')
            elif '*' in pergunta:
                operador = '*'
                partes = pergunta.split('*')
            elif 'x' in pergunta:
                operador = 'x'
                partes = pergunta.split('x')
            elif '-' in pergunta:
                operador = '-'
                partes = pergunta.split('-')
            elif '/' in pergunta:
                operador = '/'
                partes = pergunta.split('/')
            elif '**' in pergunta:
                operador = '**'
                partes = pergunta.split('**')
            elif '^' in pergunta:
                operador = '^'
                partes = pergunta.split('^')
            else:
                return f"❌ Não entendi: {pergunta}\nUse: 2+3, 5*4, 10-3, 8/2, 3**2"
            
            # Verifica se tem 2 partes
            if len(partes) != 2:
                return f"❌ Use apenas 2 números! Ex: 2+3"
            
            # Converte para números
            try:
                a = float(partes[0].strip())
                b = float(partes[1].strip())
            except ValueError:
                return f"❌ Digite números válidos! Ex: 2+3"
            
            # Verifica divisão por zero
            if operador == '/' and b == 0:
                return "❌ Erro: Divisão por zero!"
            
            # Faz a previsão
            if operador in ['**', '^']:
                # Para potência, usa só o primeiro número
                resultado = self.prever([a])
                self.historico.append((pergunta, resultado))
                return f"{a} ^ {b} = {resultado:.4f} (aproximado)"
            else:
                resultado = self.prever([a, b])
                self.historico.append((pergunta, resultado))
                
                # Escolhe o símbolo correto
                simbolo = operador
                if operador == 'x':
                    simbolo = '*'
                
                return f"{a} {simbolo} {b} = {resultado:.4f}"
        
        except Exception as e:
            return f"❌ Erro: {e}\nUse: 2+3, 5*4, 10-3, 8/2, 3**2"
    
    def mostrar_historico(self):
        if not self.historico:
            print("\n📝 Nenhuma pergunta ainda!")
            return
        
        print("\n" + "="*50)
        print("📝 HISTÓRICO DE PERGUNTAS")
        print("="*50)
        for i, (pergunta, resposta) in enumerate(self.historico, 1):
            print(f"{i}: {pergunta} -> {resposta}")
        print("="*50)
    
    def mostrar_exemplos(self):
        print("\n" + "="*50)
        print("📚 EXEMPLOS APRENDIDOS")
        print("="*50)
        for i, (entrada, saida) in enumerate(self.exemplos):
            pred = self.prever(entrada)
            print(f"{i+1}: {entrada} -> {saida:.2f} | Previsto: {pred:.4f}")
        print("="*50)


def main():
    print("="*60)
    print("🧠 SISTEMA DE APRENDIZADO INTERATIVO")
    print("="*60)
    print("\n💡 O sistema aprende com exemplos!")
    print("📖 Digite 'ajuda' para ver os comandos")
    print("🔢 Digite 'ensinar' para adicionar exemplos")
    print("❓ Digite 'sair' para encerrar")
    print("="*60)
    
    sistema = SistemaAprendiz2("Matemático")
    
    print("\n📖 Ensinando exemplos básicos...")
    sistema.ensinar([2, 3], 5)
    sistema.ensinar([10, 20], 30)
    sistema.ensinar([5, 7], 12)
    sistema.ensinar([2, 3], 6)
    sistema.ensinar([4, 5], 20)
    sistema.ensinar([3, 3], 9)
    sistema.ensinar([1], 1)
    sistema.ensinar([2], 4)
    sistema.ensinar([3], 9)
    print("✅ Exemplos básicos ensinados!\n")
    
    while True:
        try:
            pergunta = input("\n🔢 Digite sua pergunta: ").strip()
            
            if not pergunta:
                print("⚠️ Digite algo!")
                continue
            
            if pergunta.lower() == 'sair':
                print("\n👋 Até logo!")
                break
            
            elif pergunta.lower() == 'ajuda':
                print("\n" + "="*50)
                print("📖 COMANDOS DISPONÍVEIS:")
                print("="*50)
                print("  • 2 + 3      -> Soma")
                print("  • 5 * 4      -> Multiplicação")
                print("  • 10 - 3     -> Subtração")
                print("  • 8 / 2      -> Divisão")
                print("  • 3 ** 2     -> Potência")
                print("  • 2 x 3      -> Multiplicação (alternativo)")
                print("  • ensinar    -> Ensinar novo exemplo")
                print("  • exemplos   -> Ver exemplos aprendidos")
                print("  • historico  -> Ver histórico")
                print("  • limpar     -> Limpar histórico")
                print("  • sair       -> Sair")
                print("="*50)
                continue
            
            elif pergunta.lower() == 'exemplos':
                sistema.mostrar_exemplos()
                continue
            
            elif pergunta.lower() == 'historico':
                sistema.mostrar_historico()
                continue
            
            elif pergunta.lower() == 'limpar':
                sistema.historico = []
                print("🧹 Histórico limpo!")
                continue
            
            elif pergunta.lower() == 'ensinar':
                print("\n📖 Vamos ensinar um novo exemplo!")
                try:
                    entrada_str = input("  Digite os valores (ex: 2,3): ")
                    saida_str = input("  Digite o resultado (ex: 5): ")
                    
                    entrada = [float(x.strip()) for x in entrada_str.split(',')]
                    saida = float(saida_str)
                    
                    sistema.ensinar(entrada, saida)
                    print(f"✅ Exemplo {entrada} -> {saida} ensinado!")
                except ValueError:
                    print("❌ Digite números válidos! Ex: 2,3 e 5")
                except Exception as e:
                    print(f"❌ Erro: {e}")
                continue
            
            # Processa a pergunta
            resposta = sistema.perguntar(pergunta)
            print(f"\n🧠 Resposta: {resposta}")
        
        except KeyboardInterrupt:
            print("\n\n👋 Programa interrompido!")
            break
        except Exception as e:
            print(f"\n❌ Erro inesperado: {e}")
            print("💡 Tente digitar algo como: 2+3")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Programa interrompido pelo usuário!")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
    
    input("\nPressione ENTER para sair...")