import subprocess

with open("output.txt", "w+") as x:
    print("subprocess started...")
    
    try:
        result = subprocess.run(
            ["powershell", "-File", "test3.ps1"],
            stdout=x,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )

    #Note: this is linked to the "check=True" parameter
    except subprocess.CalledProcessError as e:
        print("PowerShell program failed!")
        print("Error message:\nYo mama fat ash twin")
        

    print("subprocess ended")