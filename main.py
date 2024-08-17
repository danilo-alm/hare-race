import threading
from hare import Hare
from semaphore import Semaphore
import time
import os
import sys


def print_race_state(hares):
    os.system('cls' if os.name == 'nt' else 'clear')
    state = ''
    for hare in hares:
        dist = int(hare.track_distance)
        dist = 20 if dist > 20 else dist
        dist_left = RACE_DISTANCE - dist
        state += f'{hare.id_normalized} - {"#" * dist}{" " * dist_left}|\n'
    print(state)


def monitor_race(hares):
    while any(hare.track_distance < RACE_DISTANCE for hare in hares):
        print_race_state(hares)
        time.sleep(UPDATE_FREQUENCY)
    print_race_state(hares)


def hare_behaviour(hare: Hare, semaphore: Semaphore, ranking: list, ranking_lock: threading.Lock):
    while hare.track_distance < RACE_DISTANCE:
        semaphore.acquire()

        try:
            hare.jump()

            if hare.track_distance >= RACE_DISTANCE:
                with ranking_lock:
                    ranking.append(hare)
                    break
        finally:
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


def create_hare_threads(hare_names, semaphore, ranking, ranking_lock):
    hares = []
    threads = []
    for i in range(HARE_NUMBER):
        hare = Hare(hare_names.get(i, '???'))
        hares.append(hare)
        t = threading.Thread(target=hare_behaviour, args=(hare, semaphore, ranking, ranking_lock))
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

    hare_names = {
        0: 'Danilo',
        1: 'Marcos Paulo',
        2: 'Everton',
        3: 'Tércio',
        4: 'Programador Web'
    }

    hares, threads = create_hare_threads(hare_names, semaphore, ranking, ranking_lock)
    
    monitor_thread = threading.Thread(target=monitor_race, args=(hares,))
    monitor_thread.start()

    start_and_join_threads(threads)
    monitor_thread.join()

    display_ranking(ranking)


HARE_NUMBER = 5
RACE_DISTANCE = 20
UPDATE_FREQUENCY = 0.2

if __name__ == '__main__':
    main()
