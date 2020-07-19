@echo off
for /l %%x in (1, 1, 10) do (
    date /t 
    time /t
    timeout /nobreak /t 2 > NUL
)