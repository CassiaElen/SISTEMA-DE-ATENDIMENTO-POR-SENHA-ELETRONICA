# Protocolo de Comunicação do SASE

**Transporte:** TCP (sockets). **Formato:** JSON, uma mensagem por linha (`\n`), UTF-8.
**Porta padrão:** 5000 (variáveis de ambiente `SASE_HOST` e `SASE_PORT`).

| Origem → Destino | `type` | Campos | Resposta |
|---|---|---|---|
| TS → SRV | `NOVA_SEA` | `sea` ("N1"), `tipo` ("N"/"P") | `ACK` com `sea`, `timestamp` |
| TA → SRV | `PROXIMA_SEA` | `ta_id` | `SEA` (`sea`, `ta_id`, `timestamp`) ou `SEM_SEA` |
| TV → SRV | `REGISTRAR_TV` | — | conexão fica aberta; SRV envia `SEA` a cada chamada de um TA |
| SRV → qualquer | `ERRO` | `mensagem` | — |

## Fluxo (Figura 1 do enunciado)

1. TS gera a SEA e envia `NOVA_SEA` ao SRV (SRV registra e loga o instante).
2. TA envia `PROXIMA_SEA`.
3. SRV escolhe a SEA (regra 2N:1P), responde ao TA (3.1) e difunde a **mesma** SEA a todas as TVs (3.2), logando o instante.

## Decisões de projeto

- TS e TA usam conexões curtas (uma requisição por conexão): simples e tolerante a quedas.
- TV mantém conexão persistente e reconecta sozinha a cada 2 s.
- Premissa: existe um único TS (a numeração crescente N1, N2... é mantida nele).
- SRV usa uma thread por conexão; as filas são protegidas por `threading.Lock`.
