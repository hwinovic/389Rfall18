Writeup 3 - Pentesting I
======

Name: Hope Winovich
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Hope Winovich

## Assignment 4 Writeup

### Part 1 (45 pts)
My assignment was to find the vulnerability with a Command Injection attack on Fred Krueger's new uptime system for Cornerstone Airlines. In part 1, I started by researching what kind of command injection would allow me to get into a ping command. I also ran 'nc cornerstoneairlines.co 45' to see that the prompt asks for an ip address. Then, I found that you can do multiple commands in one command line by using a semicolon. The example I found was "ping -c 5 127.0.0.1; id" on netsparker.com. I then looked at the screenshot that was posted about where the flag.txt file was located. I knew that for a ping function I could start with an IP address so I chose 8.8.8.8. I then followed the instruction that we should put it to sleep for 2 seconds so I used "sleep 2s". I then began to play around with the cd commands because I was not sure if I was supposed to do it just as I would in the terminal, but it worked when I did "cd home" and "cat flag.txt" to get into the actual file. My full command to get to the flag was "8.8.8.8; sleep 2s; cd home; cat flag.txt;\n". The flag I found was "CMSC389R- {p1ng_as_a_$erv1c3}". To find the script that Fred uses to check the uptime on Cornerstone Airline's website, I cd'd into opt and then used "ls" to see that there is a file called container_startup.sh. That file contains the prompt for an ip address, reads the input, and then has the ping command for the input. There is a huge vulnerability that exists here because anyone that can get through to the server can see this file and type in the ip address along with any other command to actually change things within the server. Here, hiding the file does not do much because a user just has to use ls to find it once they get in. However, in this script Fred could use a regex that only accepts a maximum of 3 digits followed by a "." and repeat that 3 times. The regex would look something like
'if $input = ""^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$""' depending what language you are using. Then, no user that gets into the server can type anything but an ip address.


### Part 2 (55 pts)
For part 2, I made an interactive shell so that I could get back into Fred Krueger's server. First, I changed the code from stub.py to make an interactive shell. I found this to be rather difficult because I was not even fully aware what a shell was before this assignment so I used some helpful websites to teach myself about shells and how I could implement one. I printed the $ sign to make it seem like the user could type commands, like in terminal and then sent in the ip address like I did in part 1. From there, I found out on a website that you can send in data as input by using raw_input(). So after sending in that command with the ip address, I sent in the raw_input so that every command that I type would be sent as a command. This, essentially, allowed me to "ls" into the server and also let me bring up the help menu and quit. However, I had a lot of extra data that was present such as the "PING" command and other statistics about time so I used echo to get rid of some of that extra data that was not necessary. My code for this part is in stub.py

I would love to see more help in the slides on possible commands that we can use for our homework because when I look for resources relating specifically to our homework on the slides, there are not any that are useful. I have not had any experience with hacking before so more resources or an entire document of the best websites for beginners would be very helpful!
