# 🐇 Simulação de Corrida de Lebres com Threads e Semáforos

Este projeto simula uma corrida de lebres usando conceitos de programação concorrente, como threads e semáforos. O objetivo é demonstrar a coordenação de múltiplas threads competindo em uma corrida, enquanto o estado da corrida é monitorado e exibido em tempo real.

## 🎯 Objetivo

A simulação cria várias threads, cada uma representando uma lebre. Essas threads competem em uma corrida, com seu progresso gerenciado por semáforos e monitorado por meio de uma função dedicada. O projeto mostra como coordenar a execução de threads concorrentes para atingir um objetivo comum.

## 🛠️ Funcionalidades

- **Corrida Multithreaded**: Cada lebre é representada por uma thread que avança na corrida saltando e descansando aleatoriamente.
- **Semáforos**: Controla o número de lebres que podem saltar simultaneamente.
- **Sincronização e Consistência**: As threads são sincronizadas para garantir a consistência dos dados e a atualização correta da classificação.
- **Exibição em Tempo Real**: O progresso da corrida é exibido em tempo real no terminal, mostrando o avanço de cada lebre até a linha de chegada.

## 📁 Estrutura do Código

- **`Semaphore`**: Implementação personalizada de semáforo para controlar o acesso das threads a seções críticas.
- **`Hare`**: Classe que representa uma lebre na corrida, com métodos para saltar e descansar.
- **`hare_behaviour`**: Função que define o comportamento de cada lebre durante a corrida, incluindo saltar, descansar e atualizar a classificação.
- **`monitor_race`**: Função que monitora o estado da corrida, imprimindo o progresso das lebres em intervalos regulares.
- **`print_race_state`**: Função que exibe visualmente o progresso de cada lebre na corrida, atualizando a tela do terminal.

## 🚀 Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/danilo-alm/hare-race.git
   cd hare-race


2. Certifique-se de ter o Python instalado em sua máquina.

3. Execute a simulação:
   ```bash
   python race.py


## 📝 Exemplo de saída:

Durante a execução, o estado da corrida será exibido em tempo real no terminal. O progresso de cada lebre será mostrado por uma barra de caracteres #, indicando a distância percorrida:

```
Speedy               - ######    |
Hopper               - ####      |
Dash                 - ########  |
```

## 🔧 Configuração

Você pode ajustar alguns parâmetros da corrida, como a distância total (RACE_DISTANCE), a distância máxima de salto (JUMP_MAX_DISTANCE) e o tempo máximo de descanso (MAX_REST_SECONDS) no arquivo values.py.
