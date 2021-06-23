import time
import threading
import queue
import random
class sensor_data1(threading.Thread):
    def __init__(self, queue, lock, isLoop):
        threading.Thread.__init__(self)
        self.queue = queue
        self.lock = lock
        self.isLoop = isLoop
    def run(self):
        print("[INFO] Start the sensor data1")
        while self.isLoop[0]:
 # get sensor data
            val = random.uniform(10.0, 19.0)
 
 # get lock
            self.lock.acquire()
            self.queue.put(val)
 
            time.sleep(1.0)
 
 #release lock
            self.lock.release()
 
def sensor_data2(data_key, queue, lock, isLoop):
    print("[INFO] Start the sensor data2")
    while isLoop[1]:
 # get sensor data
        val = random.uniform(30.0, 39.0)
 
        data = {data_key:val}
 
 # get lock
        lock.acquire()
        queue.put(data)
 
        time.sleep(1.0)
 
 #release lock
        lock.release()
 
 
def read_kb_key(queue):
    print("[INFO] Start monitor keyborad key input")
    while True:
        cmd = input()
        print(cmd)
        if cmd == 'q':
            queue.put(cmd)
            break
 
 
 
def main():
    lock = threading.Lock()
    sensor_queue = queue.Queue()
    input_queue = queue.Queue()
    isLoop = [True, True]
 
    sensor_key2 = "temperature"
    sensor1_worker = sensor_data1(sensor_queue, lock, isLoop)
    sensor2_worker = threading.Thread(target=sensor_data2, args=(sensor_key2,sensor_queue, lock, isLoop,))
    monitor_kb_key = threading.Thread(target=read_kb_key, args=(input_queue,))
    
    sensor1_worker.start()
    sensor2_worker.start()
    monitor_kb_key.start()
    
    
    print("Main Loop start")
    while True:
        if sensor_queue.qsize() == 0:
            continue
 
        val = sensor_queue.get()
        print(f"the sensor data is {val}")

        time.sleep(1.0)
        if input_queue.qsize() > 0 and input_queue.get() == 'q':
            isLoop[0] = False
            isLoop[1] = False
            break


    monitor_kb_key.join()
    sensor2_worker.join()
    sensor1_worker.join()

    print("Done") 

if __name__ == '__main__':
    main()