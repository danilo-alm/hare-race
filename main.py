import threading
from hare import Hare
from semaphore import Semaphore


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
            semaphore.release()

        hare.rest()


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

threads = []

for i in range(HARE_NUMBER):
    hare = Hare(hare_names.get(i, '???'))
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
