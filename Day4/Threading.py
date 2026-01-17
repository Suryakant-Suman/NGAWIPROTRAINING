import threading

def task(name):
    print(f"{name} is working")

t1 = threading.Thread(target=task, args=("Ravi",))
t2 = threading.Thread(target=task, args=("Raju",))

t1, t2 = t1.start(), t2.start()
