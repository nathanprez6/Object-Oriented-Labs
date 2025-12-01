# Authors: Nathan Nguyen, Tony Gianformaggio
# Date: Oct. 13, 2025
# description: A game where the user must choose a vehicle, either a Car,
# Motorcycle, or Truck and then race against the remaining choices

import Lab14.check_input as check_input
import random
from car import Car
from motorcycle import Motorcycle
from truck import Truck

def main():
    lane_len = 100
    finish = lane_len - 1

    print("Rad Racer!")
    print(
        "Choose a vehicle and race it down the track (player = 'P'). "
        "Slow down for obstacles ('0') or else you'll crash!\n"
        "1. Lightning Car - a fast car. Speed: 7. Special: Nitro Boost (1.5x speed)\n"
        "2. Swift Bike - a speedy motorcycle. Speed: 8. "
        "Special: Wheelie (2x speed but there's a chance you'll wipe out).\n"
        "3. Behemoth Truck - a heavy truck. Speed: 6. "
        "Special: Ram (2x speed and it smashes through obstacles)."
    )

    #Vehicle setup
    car = Car("Lightning Car", "C", 6)
    moto = Motorcycle("Swift Bike", "M", 7)
    truck = Truck("Behemoth Truck", "T", 5)

    vehicles = [car, moto, truck]

    #Player selection
    player_index = check_input.get_int_range("Choose your vehicle (1-3): ", 1, 3) - 1

    #Track setup
    track = [['-' for _ in range(lane_len)] for _ in range(3)]
    for lane_i in range(3):
        spots = set()
        while len(spots) < 2:
            p = random.randint(1, lane_len - 2)
            spots.add(p)
        for p in spots:
            track[lane_i][p] = '0'
    
    #stop tracking
    last_pos = {v: 0 for v in vehicles}
    stop_history = {v: set() for v in vehicles}
    finish_order = []

    #GAME LOOP
    while any(v.position < finish for v in vehicles):

        # ---------- RENDER ----------
        view = [row[:] for row in track]

        for v in vehicles:
            if isinstance(v, Car):
                lane_i = 0
            elif isinstance(v, Motorcycle):
                lane_i = 1
            else:
                lane_i = 2

            cur = int(v.position)

            # draw '*' at every stopping point except the current position
            for pos in stop_history[v]:
                if 0 <= pos < lane_len and pos != cur and view[lane_i][pos] == '-':
                    view[lane_i][pos] = '*'

            # current location
            if 0 <= cur < lane_len:
                if vehicles.index(v) == player_index:
                    mark = 'P'
                else:
                    mark = v.initial
                view[lane_i][cur] = mark

            if v.position >= finish:
                view[lane_i][finish] = v.initial
          
        print()
        for v in vehicles:
            print(v)

        # update left-hand labels (P/M/T turn into * when they move off 0)
        left_labels = ['C', 'M', 'T']
        left_labels[player_index] = 'P'
        for i, v in enumerate(vehicles):
            if int(v.position) > 0:
                left_labels[i] = '*'

        for i, row in enumerate(view):
            print(f"{left_labels[i]}{''.join(row[1:])}")

        # PLAYER ACTS FIRST
        player = vehicles[player_index]
        if player.position < finish:
            last_pos[player] = int(player.position)
            if isinstance(player, Car):
                lane_i = 0
            elif isinstance(player, Motorcycle):
                lane_i = 1
            elif isinstance(player, Truck):
                lane_i = 2
            lane = track[lane_i]
            try:
                obs_loc = lane.index('0', int(player.position) + 1)
            except ValueError:
                obs_loc = None

            action = check_input.get_int_range(
                "Choose action (1. Fast, 2. Slow, 3. Special Move): ", 1, 3
            )
            if action == 1:
                msg = player.fast(obs_loc)
            elif action == 2:
                msg = player.slow(obs_loc)
            else:
                msg = player.special_move(obs_loc)
            print(msg)

            stop_history[player].add(int(player.position))
            if last_pos[player] < finish and player.position >= finish:
                finish_order.append(player)
                print("===> YOU FINISHED!")

        # OPPONENTS ACT
        for idx, opp in enumerate(vehicles):
            if idx == player_index or opp.position >= finish:
                continue

            last_pos[opp] = int(opp.position)
            if isinstance(opp, Car):
                lane_i = 0
            elif isinstance(opp, Motorcycle):
                lane_i = 1
            else:
                lane_i = 2
            lane = track[lane_i]

            try:
                obs_loc = lane.index('0', int(opp.position) + 1)
            except ValueError:
                obs_loc = None

            if opp.energy < 5:
                choice = 's'
            else:
                r = random.random()
                choice = 's' if r < 0.40 else ('f' if r < 0.70 else 'p')
                if (choice == 'p' and opp.energy < 15) or (choice == 'f' and opp.energy < 5):
                    choice = 's'
            if choice == 'f':
                msg = opp.fast(obs_loc)
            elif choice == 's':
                msg = opp.slow(obs_loc)
            else:
                msg = opp.special_move(obs_loc)

            print(msg)
            # should not be setter/calling directly
            stop_history[opp].add(int(opp.position))
            if last_pos[opp] < finish and opp.position >= finish:
                finish_order.append(opp)
                print(f"===> {opp._name} FINISHED!")

    # --- Final Results ---
    print()
    view = [row[:] for row in track]

    for v in vehicles:
        if isinstance(v, Car):
            lane_i = 0
        elif isinstance(v, Motorcycle):
            lane_i = 1
        else:
            lane_i = 2

        cur = int(v.position)

        # draw '*' at every stopping point except the current position
        for pos in stop_history[v]:
            if 0 <= pos < lane_len and pos != cur and view[lane_i][pos] == '-':
                view[lane_i][pos] = '*'

        # current location
        if 0 <= cur < lane_len:
            if vehicles.index(v) == player_index:
                mark = 'P'
            else:
                mark = v.initial
            view[lane_i][cur] = mark

        if v.position >= finish:
            view[lane_i][finish] = v.initial

     # update left-hand labels (P/M/T turn into * when they move off 0)
    left_labels = ['C', 'M', 'T']
    left_labels[player_index] = 'P'
    for i, v in enumerate(vehicles):
        if int(v.position) > 0:
            left_labels[i] = '*'

    for i, row in enumerate(view):
        print(f"{left_labels[i]}{''.join(row[1:])}")

    print()
    print(f"1st place: {finish_order[0]}")
    print(f"2nd place: {finish_order[1]}")
    print(f"3rd place: {finish_order[2]}")

if __name__ == '__main__':
    main()