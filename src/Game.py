class Game:
    def to_move(self, state=None):
        if state is None:
            return self._to_move_no_arg()
        else:
            return self._to_move_with_state(state)

    def _to_move_with_state(self, state):
        return state.to_move

    def play_game(game, strategies: dict, verbose=False):
        """Play a turn-taking game. `strategies` is a {player_name: function} dict,
        where function(state, game) is used to get the player's move."""
        state = game.initial
        while not game.is_terminal(state):
            player = state.to_move
            move = strategies[player](game, state)
            state = game.result(state, move)
            if verbose:
                print('Player', player, 'move:', move)
                print(state)
        return state