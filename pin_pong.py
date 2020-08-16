from multiprocessing import Process, Pipe, Lock
from time import sleep
from random import randint


def ponger(receiver, sender, proc_name, response, lock=Lock()):
    sender.send(f'{response}')
    print(f'Player {proc_name} ready')
    while True:
        lock.acquire()
        sleep(randint(0, 2))
        print(f'Player {proc_name} caught : {receiver.recv()}')
        sender.send(f'{response}')
        lock.release()


if __name__ == "__main__":
    receiver_ping, sender_ping = Pipe()
    receiver_pong, sender_pong = Pipe()
    response_ping = 'ping'
    response_pong = 'pong'
    proc_ping_name = "Right racket"
    proc_pong_name = "Left racket"
    proc_ping = Process(target=ponger, args=(sender_ping, receiver_pong, proc_ping_name, response_ping))
    proc_pong = Process(target=ponger, args=(sender_pong, receiver_ping, proc_pong_name, response_pong))
    proc_ping.start()
    proc_pong.start()
