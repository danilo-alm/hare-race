import threading
import time
import os
import sys
from hare import Hare
from semaphore import Semaphore
from values import (
    HARE_NUMBER,
    RACE_DISTANCE,
    MAX_REST_SECONDS
)


def print_race_state(hares: list[Hare]):
    os.system('cls' if os.name == 'nt' else 'clear')
    state = ''
    for hare in hares:
        dist = int(hare.track_distance)
        dist = RACE_DISTANCE if dist > RACE_DISTANCE else dist
        dist_left = RACE_DISTANCE - dist
        state += f'{hare.id_normalized} - {"#" * dist}{" " * dist_left}|\n'
    print(state)


def monitor_race(hares: list[Hare], race_updated: threading.Condition):
    while any(hare.track_distance < RACE_DISTANCE for hare in hares):
        with race_updated:
            race_updated.wait(MAX_REST_SECONDS)
        print_race_state(hares)


def hare_behaviour(hare: Hare, semaphore: Semaphore, ranking: list, ranking_lock: threading.Lock, race_updated: threading.Condition):
    while hare.track_distance < RACE_DISTANCE:
        semaphore.acquire()

        try:
            hare.jump()

            if hare.track_distance >= RACE_DISTANCE:
                with ranking_lock:
                    ranking.append(hare)
                    break
        finally:
            with race_updated:
                race_updated.notify()

            semaphore.release()

        hare.rest()


def countdown():
    print(r'''
 _   _    _    ____  _____   ____      _    ____ _____ 
| | | |  / \  |  _ \| ____| |  _ \    / \  / ___| ____|
| |_| | / _ \ | |_) |  _|   | |_) |  / _ \| |   |  _|  
|  _  |/ ___ \|  _ <| |___  |  _ <  / ___ \ |___| |___ 
|_| |_/_/   \_\_| \_\_____| |_| \_\/_/   \_\____|_____|
    ''')

    for i in range(3, 0, -1):
        print(i, end='... ')
        sys.stdout.flush()
        time.sleep(1)
    print('GO!')


def create_hare_threads(hare_names, semaphore, ranking, ranking_lock, race_updated):
    hares = []
    threads = []
    for i in range(HARE_NUMBER):
        hare = Hare(hare_names.get(i, '???'))
        hares.append(hare)
        t = threading.Thread(target=hare_behaviour, args=(hare, semaphore, ranking, ranking_lock, race_updated))
        threads.append(t)
    return hares, threads


def start_and_join_threads(threads):
    for t in threads:
        t.start()
    for t in threads:
        t.join()


def display_ranking(ranking):
    position_suffixes = {1: 'st', 2: 'nd', 3: 'rd'}
    for position, hare in enumerate(ranking, start=1):
        suffix = position_suffixes.get(position, 'th')
        print(f'{position}{suffix} - {hare.id} ({hare.jumps} jumps)')


def main():
    countdown()

    ranking = []
    ranking_lock = threading.Lock()
    semaphore = Semaphore(1)
    race_updated = threading.Condition()

    hare_names = {
        0: 'Danilo',
        1: 'Marcos Paulo',
        2: 'Everton',
        3: 'Tércio',
        4: 'Programador Web'
    }

    hares, threads = create_hare_threads(hare_names, semaphore, ranking, ranking_lock, race_updated)
    
    monitor_thread = threading.Thread(target=monitor_race, args=(hares, race_updated))
    monitor_thread.start()

    start_and_join_threads(threads)
    monitor_thread.join()

    display_ranking(ranking)


if __name__ == '__main__':
    main()
