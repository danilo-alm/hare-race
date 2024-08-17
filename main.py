import threading
from hare import Hare
from semaphore import Semaphore
import time
import os


def print_race_state(hares):
    os.system('cls' if os.name == 'nt' else 'clear')
    state = ''
    for hare in hares:
        dist = int(hare.track_distance)
        dist = 20 if dist > 20 else dist
        dist_left = RACE_DISTANCE - dist
        state += f'{hare.id_normalized} - {"#" * dist}{" " * dist_left}|\n'
    print(state)
    

def hare_behaviour(hare: Hare, semaphore: Semaphore):
    while hare.track_distance < RACE_DISTANCE:
        semaphore.acquire()

        try:
            hare.jump()

            if hare.track_distance >= RACE_DISTANCE:
                with ranking_lock:
                    ranking.append(hare)
                    break
        finally:
            print_race_state(hares)
            semaphore.release()

        hare.rest()


print(r'''
  _   _    _    ____  _____   ____      _    ____ _____ 
 | | | |  / \  |  _ \| ____| |  _ \    / \  / ___| ____|
 | |_| | / _ \ | |_) |  _|   | |_) |  / _ \| |   |  _|  
 |  _  |/ ___ \|  _ <| |___  |  _ <  / ___ \ |___| |___ 
 |_| |_/_/   \_\_| \_\_____| |_| \_\/_/   \_\____|_____|
''')

for i in range(3, 0, -1):
    print(i, end='... ')
    time.sleep(1)
print('GO!')

HARE_NUMBER = 5
RACE_DISTANCE = 20

ranking = []
ranking_lock = threading.Lock()
semaphore = Semaphore(1)

hare_names = dict(enumerate([
    'Danilo',
    'Marcos Paulo',
    'Everton',
    'Tércio',
    'Programador Web'
]))

hares = []
threads = []

for i in range(HARE_NUMBER):
    hare = Hare(hare_names.get(i, '???'))
    hares.append(hare)
    t = threading.Thread(target=hare_behaviour, args=(hare, semaphore))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

position_suffixes = dict(enumerate(['st', 'nd', 'rd'], start=1))
for position, hare in enumerate(ranking, start=1):
    position = f'{position}{position_suffixes.get(position, 'th')}'
    print(f'{position} - {hare.id} ({hare.jumps} jumps)')
