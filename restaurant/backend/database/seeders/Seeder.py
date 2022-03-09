import abc


class Seeder(abc.ABC):

    @staticmethod
    def run():
        raise NotImplementedError('You must define "run" method')
