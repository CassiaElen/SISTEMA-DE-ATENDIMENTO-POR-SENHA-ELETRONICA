# Plano de Testes (QA)

Rodar automatizados: `python -m unittest discover -s tests -t .`

| ID | Cenário | Esperado | Tipo |
|---|---|---|---|
| T1 | 4 N + 2 P na fila | Ordem N1,N2,P1,N3,N4,P2 | auto |
| T2 | Só senhas N | Ordem crescente normal | auto |
| T3 | Só senhas P | P1, P2 em sequência | auto |
| T4 | Fila vazia | TA recebe `SEM_SEA` | auto |
| T5 | TV recebe a mesma SEA que o TA | SEA idêntica | auto |
| T6 | 2 TAs pedindo ao mesmo tempo | Nenhuma senha duplicada/perdida | auto |
| T7 | SRV fora do ar ao gerar senha (TS) | Mensagem de erro; contador não avança | manual |
| T8 | TV iniciada antes do SRV | Reconecta sozinha | manual |
| T9 | TV cai e volta durante atendimento | Volta a receber chamadas | manual |
| T10 | Logs do SRV | Instantes de recebimento e envio impressos | manual |
