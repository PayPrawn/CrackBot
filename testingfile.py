import time
while True:
    try:
        with open('wingwong.txt', 'r+') as f:
            old = f.read()
            print(old)
    except FileNotFoundError:
        time.sleep(5)
        print('trying...')