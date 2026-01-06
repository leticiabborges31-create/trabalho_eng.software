class ListaDeTarefas:
    __instance = None

    tarefas_registradas = []

    # Garante que haja somente uma instancia da lista (Aplicação do SINGLETON)
    def __new__(cls):
        if ListaDeTarefas.__instance is None:
            ListaDeTarefas.__instance = super().__new__(cls)
        return ListaDeTarefas.__instance

    # Método para obter a lista
    def get_lista(self):
        return self.tarefas_registradas

    # Método para definir os dados da lista
    ## Aplicar o ADAPTER por aqui
    def set_lista(self, dados):
        pass