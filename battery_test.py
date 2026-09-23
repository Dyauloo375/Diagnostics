import subprocess
import time

#1: Print initial battery %
def get_battery():
    result = subprocess.run(
        ["powershell", "-Command",
        "(Get-CimInstance Win32_Battery).EstimatedChargeRemaining"],
        capture_output=True,
        text=True
    )
    battery = int(result.stdout.strip())
    return battery

battery1 = get_battery()
print("Initial battery:",battery1,"%")


#2: Run test to drain battery
print("How many minutes should the test run for? The longer the better, but it's up to you:")
test_duration = input()
test_duration = int(test_duration)
test_duration = test_duration * 60  

try:
    def cpu_workload():
        total = 0
        for i in range(1, 10000000):
            #print(total)
            total += i * i
        return total

    print("Starting battery test...")
    print(f"Duration: {test_duration} seconds")
    print("Now just wait...")
    time.sleep(2)
    start_time = time.time()
    while (time.time() - start_time) < test_duration:
        cpu_workload()


except KeyboardInterrupt:
    print("Oops, test was interrupted")


#3: Print test results
elapsed = time.time() - start_time
print("\nCPU test finished!")
print(f"Elapsed time: {elapsed:.2f} seconds")
battery2 = get_battery()
print(f"Initial battery: {battery1}%")
print(f"Fnal battery: {battery2}%")
battery_used = battery2 - battery1
print(f"Battery consumed: {battery_used}%")

