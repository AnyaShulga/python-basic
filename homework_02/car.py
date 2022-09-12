from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):
    engine = None

    def set_engine(self, engine_instance: Engine):
        self.engine = engine_instance
        return self.engine
