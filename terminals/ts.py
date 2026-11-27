import tkinter as tk
from tkinter import messagebox

from common import protocol as p


class TS:
    def __init__(self, root):
        self.root = root
        root.title("SASE - Terminal de Senhas")
        self.contador = {"N": 0, "P": 0}
        tk.Label(root, text="Retire sua senha", font=("Arial", 20, "bold")).pack(pady=10)
        tk.Button(root, text="Atendimento Normal", font=("Arial", 16), width=22, height=2,
                  command=lambda: self.gerar("N")).pack(padx=20, pady=5)
        tk.Button(root, text="Atendimento Prioritário", font=("Arial", 16), width=22, height=2,
                  command=lambda: self.gerar("P")).pack(padx=20, pady=5)
        self.lbl = tk.Label(root, text="---", font=("Arial", 40, "bold"), fg="#c00")
        self.lbl.pack(pady=15)
        self.info = tk.Label(root, text="", font=("Arial", 10))
        self.info.pack(pady=(0, 10))

    def gerar(self, tipo):
        sea = f"{tipo}{self.contador[tipo] + 1}"
        try:
            resp = p.requisicao({"type": p.NOVA_SEA, "sea": sea, "tipo": tipo})
        except OSError as e:
            messagebox.showerror("Erro de conexão", f"Não foi possível falar com o servidor.\n{e}")
            return 
        self.contador[tipo] += 1
        self.lbl.config(text=sea)
        self.info.config(text=f"Registrada no servidor às {resp.get('timestamp')}")


if __name__ == "__main__":
    root = tk.Tk()
    TS(root)
    root.mainloop()
