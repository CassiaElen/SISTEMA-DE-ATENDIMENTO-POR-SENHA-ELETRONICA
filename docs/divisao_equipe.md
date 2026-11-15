# Divisão de Funções (7 integrantes)

| # | Função | Responsável | Arquivos principais |
|---|---|---|---|
| 1 | Dev do Servidor (SRV) | _Matheus Soares_ | `server/srv.py`, `server/filas.py` |
| 2 | Dev do Terminal de Senhas (TS) | _Cássia Elen_ | `terminals/ts.py` |
| 3 | Dev do Terminal de Atendimento (TA) | _Mário Italo_ | `terminals/ta.py` |
| 4 | Dev do Terminal de Visualização (TV) | _Carla Mariana_ | `terminals/tv.py` |
| 5 | Redes e Integração | _Iruan_ | `common/protocol.py`, `docs/protocolo.md` |
| 6 | QA / Testes | _Holdacianne_ | `tests/`, `docs/plano_de_testes.md` |
| 7 | Documentação | _Clerveson_ | `docs/relatorio_tecnico.md` |

## Fluxo de trabalho sugerido (Git)

- Branch `main` protegida; cada pessoa trabalha em `feature/<modulo>`.
- Contrato entre módulos = `docs/protocolo.md`. Mudou o protocolo? Avise o responsável pelo item 5 e todos.
- Merge via Pull Request revisado por pelo menos 1 colega.
