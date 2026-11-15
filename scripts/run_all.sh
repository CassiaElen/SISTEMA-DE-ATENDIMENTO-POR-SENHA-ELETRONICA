#!/usr/bin/env bash
# Sobe SRV, TV, TS e dois TAs (Linux/macOS). Rode a partir da raiz do projeto.
python -m server.srv &
sleep 1
python -m terminals.tv &
python -m terminals.ts &
python -m terminals.ta TA1 &
python -m terminals.ta TA2 &
wait
