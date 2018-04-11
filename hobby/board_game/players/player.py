from example_env.example_env import Example_env,check_state_free
from oppenent import Oppenent

class Player(Example_env):
    _no_of_coin_player = 0

    def __new__(cls, *kargs, **kwargs):
        Player._no_of_coin_player += 1
        if Player._no_of_coin_player < 4:
            obj = super(Player, cls).__new__(cls)
            return obj
        else:
            raise Exception('only three object is possible')

    def __init__(self, state):
        self.action = 'first'
        Example_env.__init__(self)
        Example_env.player_list.append(self)
        self.state = state
        check_state_free(self)
        pass


def creating_player(state):
    if Player._no_of_coin_player == Oppenent._no_of_coin_oppenent:
        obj = Player(state)
        return (obj)
    else:
        raise Exception('Oppenent turn!!!')
