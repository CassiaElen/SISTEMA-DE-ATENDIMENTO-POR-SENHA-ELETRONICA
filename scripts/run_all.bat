@echo off
REM Sobe SRV, TV, TS e dois TAs (Windows). Rode a partir da raiz do projeto.
start "SRV" python -m server.srv
timeout /t 1 >nul
start "TV" python -m terminals.tv
start "TS" python -m terminals.ts
start "TA1" python -m terminals.ta TA1
start "TA2" python -m terminals.ta TA2
