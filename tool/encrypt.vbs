' start

WScript.Sleep(1)

DIM FSO, MyFile
Set oShell = CreateObject( "WScript.Shell" )
user=oShell.ExpandEnvironmentStrings("%UserName%")

' create folder 
FSO.CreateFolder("delete\")

' move files to new folder
FSO.Movefile "DDoS.py","delete\"
FSO.Movefile "Install.py","delete\"
FSO.Movefile "JustAfile.txt","delete\"

' alert box
Orbit=MsgBox("Succsesfuly deleted main files... please delete the rest.", 0+64, "Orbit Status")

' end
