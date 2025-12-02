# 🎮 Jokenpô (Pedra, Papel e Tesoura)

Uma implementação moderna e interativa do clássico jogo Jokenpô desenvolvida em Python. Este projeto vai além da lógica básica, utilizando estruturas de dados eficientes e uma interface visualmente agradável no terminal.

## ✨ Funcionalidades

* *Interface Visual*: Uso de emojis (🪨, 📄, ✂️) para tornar o jogo mais divertido. <br>
* *Placar em Tempo Real*: Monitoramento de vitórias, derrotas e empates durante a sessão. <br>
* *Tratamento de Erros*: Validação de entrada para impedir que o jogo quebre com digitação errada. <br>
* *Lógica Otimizada*: Substituição de múltiplos if/else por Dicionários Python para verificação de vitória. <br>
* *Cross-platform*: Comando de limpeza de tela compatível com Windows e Linux/Mac. <br>

## 🧠 Destaque do Código

Em vez de usar cadeias longas de condicionais '''(if jogador == 'pedra' and computador == 'tesoura' ...)''', utilizei a lógica de Dicionários para mapear as condições de vitória. Isso torna o código mais limpo e escalável.
'''text
# Mapeamento de quem ganha de quem
REGRAS_VITORIA = {
    'pedra': 'tesoura',   # Pedra ganha de Tesoura
    'tesoura': 'papel',   # Tesoura ganha de Papel
    'papel': 'pedra'      # Papel ganha de Pedra
}

# Verificação simples em uma linha
if REGRAS_VITORIA[jogador] == computador:
    print("Você venceu!")

text'''
## 🚀 Como rodar o projeto

Pré-requisitos<br>
    Python 3.x instalado.<br>

Passo a passo<br>

Clone o repositório: <br>
    git clone [https://github.com/SEU-USUARIO/NOME-DO-REPO.git](https://github.com/SEU-USUARIO/NOME-DO-REPO.git)<br>


Execute o jogo: <br>
    python pedra_papel_tesoura.py <br>


## 🛠️ Tecnologias Utilizadas

* *Python*: Linguagem principal. <br>
* *Random*: Para geração da escolha aleatória da IA. <br>
* *OS*: Para manipulação e limpeza do terminal. <br>
* *Time*: Para criar o efeito de suspense ("Jo-ken-pô"). <br>

## 👨‍💻 Autor
Desenvolvido por Enio Jr, para fins de estudo de lógica de programação e Python.

📧 Entre em contato: eniojr100@gmail.com <br>
🔗 LinkedIn: https://www.linkedin.com/in/enioeduardojr/ <br>
📷 Instagram: https://www.instagram.com/enio_juniorrr/ <br>
