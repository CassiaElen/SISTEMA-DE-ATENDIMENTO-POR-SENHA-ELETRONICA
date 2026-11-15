# SISTEMA-DE-ATENDIMENTO-POR-SENHA-ELETRONICA

Projeto da disciplina de Sistemas Distribuídos. Python 3.9+, sockets TCP, Tkinter. Sem dependências externas.

## Estrutura

```text
sase/
├── common/protocol.py      # constantes, envio/leitura JSON, requisição curta
├── server/
│   ├── srv.py              # SRV: sockets, threads, difusão para TVs
│   └── filas.py            # regra 2N:1P
├── terminals/
│   ├── ts.py               # Terminal de Senhas
│   ├── ta.py               # Terminal de Atendimento
│   └── tv.py               # Terminal de Visualização
├── tests/                  # unitários e de integração
├── docs/                   # protocolo, divisão da equipe, plano de testes, relatório
└── scripts/run_all.sh|bat  # sobe tudo de uma vez
```

## Como executar (a partir da raiz do projeto)

Terminais separados, nesta ordem:

```shell
python -m server.srv
python -m terminals.tv
python -m terminals.ts
python -m terminals.ta TA1
python -m terminals.ta TA2      # opcional
```

Ou tudo de uma vez: `scripts/run_all.sh` (Linux/macOS) / `scripts\run_all.bat` (Windows).

Em máquinas diferentes: `SASE_HOST=<ip do servidor>` (e `SASE_PORT`) nos terminais.
No Linux, se faltar o Tkinter: `sudo apt install python3-tk`.

## Testes

```shell
python -m unittest discover -s tests -t .
```
