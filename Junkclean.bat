@Echo off
del "C:\Windows\Temp" /s /f /q
@RD /s /q "C:\Windows\Temp"

@Echo off
del "%UserProfile%\AppData\Local\Temp" /s /f /q
@RD /s /q "%UserProfile%\AppData\Local\Temp"

@Echo off
del "C:\Windows\prefetch" /s /f /q
@RD /s /q "C:\Windows\prefetch"
