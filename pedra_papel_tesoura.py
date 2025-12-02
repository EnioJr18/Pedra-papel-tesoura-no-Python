import random
import time
import os

OPCOES = {
    'pedra': '🪨',
    'papel': '📄',
    'tesoura': '✂️'
}

REGRAS_VITORIA = {
    'pedra': 'tesoura',
    'tesoura': 'papel',
    'papel': 'pedra'
}

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_placar(placar_jogador, placar_pc, empates):
    print("="*30)
    print(f"🏆 PLACAR GERAL")
    print(f"👤 Você: {placar_jogador}  |  🤖 PC: {placar_pc}  |  🤝 Empates: {empates}")
    print("="*30)

def obter_escolha_jogador():
    while True:
        print("\nEscolha sua arma:")
        for opcao, emoji in OPCOES.items():
            print(f"[{opcao}] {emoji}")
        
        escolha = input("👉 Sua jogada: ").strip().lower()
        
        if escolha in OPCOES:
            return escolha
        print("❌ Jogada inválida! Tente pedra, papel ou tesoura.")

def jogar():
    placar = {'jogador': 0, 'pc': 0, 'empates': 0}

    limpar_tela()
    print("🎮 BEM-VINDO AO JOKENPO AVANÇADO 🎮")
    
    while True:
        jogador = obter_escolha_jogador()
        computador = random.choice(list(OPCOES.keys()))

        print("\nJo...", end="", flush=True)
        time.sleep(0.8)
        print("Ken...", end="", flush=True)
        time.sleep(0.8)
        print("PÔ!\n")
        time.sleep(0.5)
        print(f"👤 Você: {OPCOES[jogador]}  X  {OPCOES[computador]} :PC 🤖")

        if jogador == computador:
            print("⚖️  EMPATE!")
            placar['empates'] += 1
        elif REGRAS_VITORIA[jogador] == computador:
            print("🎉 VOCÊ VENCEU A RODADA!")
            placar['jogador'] += 1
        else:
            print("💀 O COMPUTADOR VENCEU!")
            placar['pc'] += 1

        exibir_placar(placar['jogador'], placar['pc'], placar['empates'])

        continuar = input("Jogar novamente? (S/N): ").strip().lower()
        if continuar != 's':
            print("\nObrigado por jogar! Até a próxima.")
            break
        
        limpar_tela()

if __name__ == "__main__":
    jogar()