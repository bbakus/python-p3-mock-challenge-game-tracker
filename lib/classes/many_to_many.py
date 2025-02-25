


class Game:

    all = []


    def __init__(self, title):
        self.title = title
        Game.all.append(self)


    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title_value):
    
        if not isinstance(title_value, str):
            return
        if len(title_value) < 1:
            return
        if hasattr(self, '_title'):
            return
        
        self._title = title_value

    def results(self):
        return list(set([results for results in Result.all if results.game == self]))

    def players(self):
        return list(set([value.player for value in Result.all if value.game == self]))

    def average_score(self, player):
        score_list = [result.score for result in Result.all 
                  if result.player == player and result.game == self]
        return sum(score_list) / len(score_list)





class Player:

    all = []

    def __init__(self, username):
        self.username = username
        Player.all.append(self)


    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self,username_value):
        if not(type(username_value) == str):
            return
        elif not(2 <= len(username_value) <= 16):
            return
        else:
            self._username = username_value
        


    def results(self):
        return list(set([result for result in Result.all if result.player == self]))

    def games_played(self):

        return list(set([games.game for games in Result.all if games.player == self]))

    def played_game(self, game):
        if game in self.games_played():
            return True
        else:
            return False

    def num_times_played(self, game):
        return sum(1 for result in Result.all 
               if result.player == self and result.game == game)






class Result:

    all = []


    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)


    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score_value):
        if not(type(score_value) == int):
            return
        elif not(1 <= score_value <= 5000):
            return
        elif hasattr(self, '_score'):
            return
        else:
            self._score = score_value

    
    @classmethod
    def get_results_for_player(cls, player):
        return [result for result in cls._all if result.player == player]

    @classmethod
    def get_results_for_game(cls, game):
        return [result for result in cls._all if result.game == game]