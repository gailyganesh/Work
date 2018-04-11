from example_env.example_env import Example_env,check_state_free
from player import Player

class Oppenent(Example_env):
    _no_of_coin_oppenent = 0

    def __new__(cls, *kargs, **kwargs):
        Oppenent._no_of_coin_oppenent += 1
        if Oppenent._no_of_coin_oppenent < 4:
            obj = super(Oppenent, cls).__new__(cls)
            return obj
        else:
            raise Exception('only three object is possible')

    def __init__(self, state):
        self.action = 'first'
        Example_env.__init__(self)
        Example_env.oppenent_list.append(self)
        self.state = state
        check_state_free(self)
        pass


def creating_oppenent(state):
    if Player._no_of_coin_player > Oppenent._no_of_coin_oppenent:
        obj = Oppenent(state)
        return (obj)
    else:
        raise Exception('Oppenent turn!!!')
