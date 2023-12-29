import abc

class AbsParameter(abc.ABC):
    @abc.abstractmethod
    def description(self):
        pass

    @abc.abstractmethod
    def simulation(self):
        pass
