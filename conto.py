
class ContoBancario():
    def __init__(self, intestatario):
        self.intestatario = intestatario
        self.saldo = 0

    def deposita(self, importo):
        self.saldo = self.saldo + importo

    def preleva(self, importo):
        if self.saldo <importo:
            raise ValueError('Saldo non disponibile')
        self.saldo = self.saldo - importo

    def __str__(self):
        return f'Conto di {self.intestatario} saldo: {self.saldo}'


def main():
    conto = ContoBancario("Mario Rossi")
    print(conto)

    conto.deposita(200)
    conto.preleva(50)
    conto.preleva(25)
    try:
        conto.preleva(700)
    except ValueError as e:
        print(f'Operazione rifiutata: {e}')
    print(conto)


if __name__ == "__main__":
    main()
