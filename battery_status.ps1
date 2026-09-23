& powercfg /batteryreport /XML /OUTPUT "batteryreport.xml"
Start-Sleep 1
[xml]$b = Get-Content batteryreport.xml

$b.BatteryReport.Batteries |
    ForEach-Object{
        [PSCustomObject]@{
            DesignCapacity = $_.Battery.DesignCapacity
            FullChargeCapacity = $_.Battery.FullChargeCapacity
            BatteryHealth = [math]::floor([int64]$_.Battery.FullChargeCapacity/[int64]$_.Battery.DesignCapacity*100)
            CycleCount = $_.Battery.CycleCount
            Id = $_.Battery.id
        }
    }

rm batteryreport.xml