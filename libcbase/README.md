# Bruteforce 
```
$ file example_vuln
example_vuln: ELF 32-bit LSB shared object, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=aaff0f9c20376d1500e125fe59966ccc27c015b7, not stripped
```

## CHECKSEC
```
gdb-peda$ checksec
CANARY    : disabled
FORTIFY   : disabled
NX        : ENABLED
PIE       : ENABLED
RELRO     : Partial
```
## ASLR
```
# cat /proc/sys/kernel/randomize_va_space
2
```
## USAGE
```
$ python exploit.py 
[!] Pwntools does not support 32-bit Python.  Use a 64-bit release.
Filename: example_vuln
Offset: 112
```
## RESULT
![screenshot](https://user-images.githubusercontent.com/16120472/31750800-e64a0876-b48a-11e7-9d51-9b46596335e8.png)
