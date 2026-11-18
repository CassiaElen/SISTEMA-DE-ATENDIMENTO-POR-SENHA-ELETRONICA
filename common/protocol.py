import json
import os
import socket
from datetime import datetime

# ==============================================================================
# CONFIGURAÇÕES E CONSTANTES DE REDE
# ==============================================================================
# Lê do ambiente (SASE_HOST / SASE_PORT) ou assume os padrões 127.0.0.1:5000
HOST = os.environ.get("SASE_HOST", "127.0.0.1")
PORT = int(os.environ.get("SASE_PORT", 5000))
TIMEOUT = 5.0  # Timeout em segundos para conexões curtas de requisição

# ==============================================================================
# CONSTANTES DE TIPOS DE MENSAGEM DO PROTOCOLO SASE
# ==============================================================================
# Ninguém digita string solta nos outros arquivos; todos importam daqui
NOVA_SEA = "NOVA_SEA"          # TS -> SRV (Gera nova senha)
ACK = "ACK"                    # SRV -> TS (Confirmação de recebimento)
PROXIMA_SEA = "PROXIMA_SEA"    # TA -> SRV (Solicita próxima senha)
SEA = "SEA"                    # SRV -> TA/TV (Informa a senha que deve ser atendida)
SEM_SEA = "SEM_SEA"            # SRV -> TA (Informa que não há senhas na fila)
REGISTRAR_TV = "REGISTRAR_TV"  # TV -> SRV (Registra a TV para escutar chamadas)
ERRO = "ERRO"                  # SRV -> Cliente (Mensagem de erro genérica)

def agora() -> str:
    """Devolve a hora atual no formato exato HH:MM:SS.mmm (usado nos logs e mensagens)."""
    now = datetime.now()
    return now.strftime("%H:%M:%S.") + f"{now.microsecond // 1000:03d}"

def enviar(sock: socket.socket, msg: dict) -> None:
    """
    Converte o dicionário em JSON, adiciona a quebra de linha '\n' como delimitador
    e envia via socket usando sendall() em UTF-8.
    O '\n' é fundamental pois o TCP é um fluxo contínuo de bytes.
    """
    payload = json.dumps(msg) + "\n"
    sock.sendall(payload.encode("utf-8"))

def ler(arquivo) -> dict | None:
    """
    Lê uma linha de um objeto arquivo criado via sock.makefile("r", encoding="utf-8")
    e converte de JSON para dicionário Python.
    Se a linha vier vazia, significa que a conexão foi encerrada e devolve None.
    """
    linha = arquivo.readline()
    if not linha:
        return None
    return json.loads(linha.strip())

def requisicao(msg: dict, host: str = None, porta: int = None) -> dict:
    """
    Abre uma conexão TCP curta com o servidor, envia a mensagem, aguarda a resposta,
    fecha o socket e devolve o dicionário recebido.
    Se a conexão falhar ou o servidor não responder, levanta ConnectionError.
    Função utilizada diretamente pelos terminais TS e TA.
    """
    dest_host = host if host is not None else HOST
    dest_porta = porta if porta is not None else PORT

    try:
        with socket.create_connection((dest_host, dest_porta), timeout=TIMEOUT) as sock:
            enviar(sock, msg)
            with sock.makefile("r", encoding="utf-8") as arq:
                resposta = ler(arq)
                if resposta is None:
                    raise ConnectionError("Servidor encerrou a conexão sem enviar resposta.")
                return resposta
    except (OSError, ValueError) as err:
        raise ConnectionError(f"Falha na comunicação com o servidor SASE ({dest_host}:{dest_porta}): {err}")
