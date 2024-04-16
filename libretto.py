from _ast import operator


class Voto:
    def __init__(self, nome_esame, cfu, punteggio, lode, data):
        self.nome_esame = nome_esame
        self.cfu = cfu
        self.__punteggio = 0
        self.lode = False
        self.data = data

        if self.lode and punteggio != 30:
            raise ValueError("Lode non applicabile")
        else:
            self.__punteggio = punteggio
            self.lode = lode

    @property
    def punteggio(self):
        return self.__punteggio

    @punteggio.setter
    def punteggio(self, punteggio):
        if punteggio >= 18 and punteggio <= 30:
            self.__punteggio = punteggio
        else:
            raise ValueError("Punteggio esame errato (punteggio compreso tra 18 e 30 )")

    def __lt__(self, other):
        """
        per considerare un voto minore di un altro valutiamo il punteggio, lode inclusa, e i cfu.
        Il metodo presuppone la consistenza di punteggio e lode.

        :param other: voto da valutare con self
        :return: True se self < other
     """
        punteggioSelf = 31 if self.lode else self.punteggio
        punteggioOther = 31 if other.lode else other.punteggio
        punteggioSelf *= self.cfu
        punteggioOther *= other.cfu

        return punteggioSelf < punteggioOther

    def __str__(self):
        return f"{self.nome_esame} ({self.cfu}): voto = {self.str_punteggio()} data: {self.data}"

    def __repr__(self):
        return f"Voto('{self.nome_esame}', {self.cfu}, {self.punteggio}, {self.lode}, '{self.data}')"

    def str_punteggio(self):
        """
        Costrusce la stringa in base al punteggio tenendo conto della lode
        :return: stringa rappresentativa del punteggio

        """
        return f"30 e lode" if self.punteggio == 30 and self.lode else f"{self.punteggio}"

    def copy(self):
        return Voto(self.nome_esame, self.cfu, self.punteggio, self.lode, self.data)


class Libretto:
    def __init__(self):
        self.voti = []

    def clona(self):
        nuovo = Libretto()
        # nuovo.voti = copy.deepcopy(self.voti)
        for v in self.voti:
            nuovo.append(v.copy())

        return nuovo

    def stampa(self):
        str_libretto = f""

        if len(self.voti) != 0:
            for v in self.voti:
                str_libretto += f"{v.nome_esame} cfu: {v.cfu} voto: {v.str_punteggio()} data:{v.data}\n"
        else:
            str_libretto += f"Non ci sono esami\n"
        return str_libretto

    def libretto_miglioratao(self):
        """
        produce un libretto 'migliorato' secondo le specifiche
        della domanda n.7.
        Si utilizza il metodo clona per avere una deepcopy dellibretto
        :return: deepcopy del libretto con i voti migliorati
        """
        nuovo = self.clona()
        for v in nuovo.voti:
            if (18 <= v.punteggio <= 23) or v.punteggio == 29:
                v.punteggio += 1
            elif 24 <= v.punteggio <= 28:
                v.punteggio += 2
        return nuovo

    def append(self, voto):
        """
        La funzione controlla:
            se il voto è presente (has_voto) -> viene sollevata un'eccezione
            se vi sono conflitti (has_conflitto) -> viene sollevata un'eccezione

        :param voto: oggetto voto da inserire nella lista
        :return: None
        """

        if self.has_voto(voto):
            raise ValueError("Voto già presente")
        if self.has_conflitto(voto):
            raise ValueError("Voto in conflitto")
        self.voti.append(voto)

        for vv in self.voti:
            if vv.nome_esame == voto.nome_esame:
                presente = True
                break
        if not presente:
            self.voti.append(voto)
        return not presente

    def findByPunteggio(self, punteggio, lode):
        """
        Ricerca degli esami che hanno il punteggio e la lode passati come parametri.
        Si controlla la compatibilità tra punteggio e lode; se esiste incompatibilità
        si restituisce una lista vuota
        :param punteggio: intero punteggio da cercare
        :param lode: booleano
        :return: lista degli oggetti Voto che soddisfano la richiesta (lista vuota in caso contrario)
        """

        if punteggio != 30 and lode:
            votiTrovati = []
        else:
            votiTrovati = [voto for voto in self.voti if voto.punteggio == punteggio and voto.lode == lode]
        return votiTrovati

    def has_voto(self, voto):
        """

        nomeEsame, punteggio, lode
        Ricerca nella lista voti se esiste un voto con nome esame, punteggio e lode
         uguali a quelli dell'oggetto passsato come parametro.
        Non si controlla la consistenza dell' punteggio.
        :param voto: oggetto Voto da cercare nella lista voti
        :return: True se si è trovata corrispondenza
        """

        trovato = False
        for v in self.voti:
            if v.nome_esame == voto.nome_esame and v.punteggio == voto.punteggio and v.lode == voto.lode:
                trovato = True
                break

        return trovato

    def has_conflitto(self, voto):
        """
        Ricerca nella lista voti se esiste un voto con nome esame uguale a quello
        del parametro ma con punteggio diverso
        Non si controlla la consistenza dell' punteggio.
        :param voto: oggetto Voto da confrontare  nella lista voti
        :return: True se esiste conflitto
        """

        conflitto = False
        for v in self.voti:
            if v.nome_esame == voto.nome_esame and (v.punteggio != voto.punteggio or v.lode != voto.lode):
                conflitto = True
                break

        return conflitto

    def findNomeEsame(self, nomeEsame):
        """
        Ricerca il nome dell'esame nella lista degli esami se viene trovato restituisce l'oggetto voto
        corrispondente. In caso contrario la funzione solleva un'eccezione
        :param nomeEsame: stringa nome esame da cercare
        :return: oggetto voto
        """
        trovato = False
        n = len(self.voti)
        for i in range(n - 1):
            if self.voti[i].nome_esame == nomeEsame:
                trovato = True
                break
        if not trovato:
            raise ValueError("Nome esame non trovato")

        return self.voti[i]

    def media(self):
        if len(self.voti) == 0:
            raise ValueError("Elenco voti vuoto")
        somma_cfu = 0
        somma_punteggi = 0
        for v in self.voti:
            punto = 31 if v.lode else v.punteggio
            punto *= v.cfu
            somma_punteggi += punto
            somma_cfu += v.cfu

        return somma_punteggi / somma_cfu

    def crea_libretto_ordinato_per_nome(self):
        nuovo = self.clona()
        # ordina i voti per nome
        nuovo.ordina_per_nome()

        return nuovo

    def crea_libretto_ordinato_per_voto_desc(self):
        nuovo = self.clona()
        # ordina i voti per nome
        nuovo.ordina_per_voto_desc()

        return nuovo

    def ordina_per_nome(self):
        self.voti.sort(key=operator.attrgetter('esame'))

    def ordina_per_voto_desc(self):
        self.voti.sort(reverse=True)

    def cancella_inferioriA(self, punteggio):
        nuovi = []
        for v in self.voti:
            if v.punteggio >= punteggio:
                nuovi.append(v)
        self.voti = nuovi