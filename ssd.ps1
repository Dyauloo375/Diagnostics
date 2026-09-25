Get-CimInstance Win32_LogicalDisk -Filter "DriveType=3" | Select-Object DeviceID, VolumeName, 
@{Name="Size (GB)";Expression={[math]::Round($_.Size/1GB,2)}}, 
@{Name="FreeSpace (GB)";Expression={[math]::Round($_.FreeSpace/1GB,2)}},
@{Name="Free (%)";Expression={[math]::Round(($_.FreeSpace/$_.Size)*100,2)}}