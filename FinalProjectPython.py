import random
import time

class Lobster:
    def __init__(self, id, length, value):
        self.id = id
        self.length = length
        self.value = value

def valuePerUnit(Lobster):
    return Lobster.value / (Lobster.length * 1.0)

def sortLobsters(Lobsters):
    Lobsters.sort(key=valuePerUnit, reverse=True)

def allocateLobsters(Lobsters, NetSize):
    currentNetSize = NetSize
    valueNet = 0.0

    for Lobster in Lobsters:
        if Lobster.length <= currentNetSize:
            print(f"\nThe lobster no.{Lobster.id} has been chosen, with the value of {Lobster.value} and the length of {Lobster.length}")
            valueNet += Lobster.value
            currentNetSize -= Lobster.length

    print(f"\nThe maximum value obtained is: {valueNet}")

def generareLobsters(noLobsters):
    Lobsters = []
    for i in range(noLobsters):
        id = i
        length = random.randint(1, 500)
        value = random.randint(1, 500)
        Lobsters.append(Lobster(id, length, value))
    return Lobsters

def generateNumbers():
    return random.randint(1, 10000)

def main():
    random.seed(time.time())
    start_time = time.time()
    
    noLobsters = generateNumbers()
    NetSize = generateNumbers()
    
    Lobsters = generareLobsters(noLobsters)

    print(f"  Number of lobsters: {noLobsters}\n  Net size: {NetSize}")
    print("\n------Selected lobsters------")
    
    sortLobsters(Lobsters)
    allocateLobsters(Lobsters, NetSize)
    
    elapsed_time = time.time() - start_time
    print(f"\nElapsed: {elapsed_time} seconds")

if __name__ == "__main__":
    main()
