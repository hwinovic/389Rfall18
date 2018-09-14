Writeup 2 - OSINT (Open Source Intelligence)
======

Name: Hope Winovich
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Hope Winovich

## Assignment 2 writeup

### Part 1 (45 pts)

1.   Fred Krueger

2. Reddit - google searched `kruegster1990` and found 'u/kruegster1990' account
stwity.com - google searched `kruegster1990` and found his location is in Silver Spring, MD, he has 4 tweets, he has one follower and is following one person, his account was created on 12/8/2018, the ID associated with the account is 1028770124772397061,
cornerstoneairlines.co - googled this website that is on the stwity website and got to the cornerstone airline's website where Fred Krueger is the owner and his email is listed as kruegster1990@tutanota.com
Instagram - kruester1990 (looked it up on instagram)
Twitter - kruegster1990 (looked it up on twitter)

3.   I typed 'nslookup www.cornerstoneairlines' into my terminal and the ip address comes up as 142.93.118.186.

4.   !-- CMSC389R-{h1dden_fl4g_in_s0urce} --

5.   Site24x7 also shows the same ip address as above
  142.93.117.193 is the ip address in the source code for the admin page
  view-source:http://cornerstoneairlines.co/index.html

6. By doing an nmap scan on the IP address of the admin page, I found that port 80 is open, "80/tcp   open   http".
on the IP address 142.93.118.186. 22 is also an open port
I also found that 2222 was open and 1337 was open.

7.   I searched the Ip address of the admin page on onyphe and got that the server is "Apache/2.4.18 (Ubuntu)"

8. *(BONUS)*

### Part 2 (55 pts)

  For this part of the assignment, I ran the command "nmap -p 1-65535 -sV -sS -T4 142.93.117.193" and tried to run all of the open ports which were 80,1337 and 2222 and the host 1337 worked to bring up the prompt "username:". I then wrote the code for the bruteforce program and ran it against the rockyou.txt file. I got the username as kruegster from his email on his website and then the password was pokemon. Once I had the server open I cd'd into home and then flight records and then I did the command "cat AAC27670" because it was on his Instagram. The flag is "CMSC389R-{c0rn3rstone-air-27670}".
