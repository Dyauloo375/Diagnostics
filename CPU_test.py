#clock speed, core count, cache size, thermal design power
#throughput [MT/s "megatransfers per second"]

#CPU determines the write and read speed to the RAM
import numpy as np
import time

def RAM_write_speed_test():
    SIZE = 4*(1024*1024*1024)  #  GB
    data = np.empty(SIZE, dtype=np.uint8)
    start = time.perf_counter()
    data[:] = 0xAA
    elapsed = time.perf_counter() - start
    speed = SIZE / elapsed / (1024 ** 3)
    return elapsed, speed

samples = int(input("How many samples of data do you want on this test?:"))
write_times = []
write_speeds = []

for i in range(samples):
    elapsed, speed = RAM_write_speed_test()
    write_times.append(elapsed)
    write_speeds.append(speed)

avg_write_time = sum(write_times) / len(write_times)
avg_write_speed = sum(write_speeds) / len(write_speeds)

print(f"Average write time: {avg_write_time:.3f} seconds")
print(f"Average write speed: {avg_write_speed:.2f} GB/s")




