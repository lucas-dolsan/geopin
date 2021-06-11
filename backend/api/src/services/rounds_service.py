from models.place import Place
from models.map import Map
from models.round import Round

class RoundsService:

    @staticmethod
    def get_players_next_round(current_round_id: str):
        current_round=Round.objects.get(id=current_round_id)
        current_map=Map.objects.get(id=current_round.map_id)
        valid_rounds_pool=[]

        for round in current_map.rounds:
            if round is not current_round:

                # this prevents the player from playing the exact same round again
                # but we should actually properly rename the models, and be more careful with our design
                # there are more caveats here 

                valid_rounds_pool.append(round)

        return random.choice(valid_rounds_pool)

    @staticmethod
    def calculate_round_score(round_id: str, guessed_place: Place) -> int:
        current_round=Round.objects.get(id=round_id)
        distance=get_distance_between_locations(current_round.place, guessed_place)

        # about a function to define the user's score:
        # we're gonna have to find a math function that returns 5000 if supplied
        # a very short distance, and 0 if supplied a very large distance
        # should be simple but i'm tired

        return random.randint(0, 5000)


