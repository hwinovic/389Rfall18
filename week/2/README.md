OSINT (Open Source Intelligence)
======

## Assignment details

This assignment has two parts. It is due by Thursday, September 13 at 11:59 PM.

To submit your homework, please follow the guidelines posted under the grading section of the syllabus.

**There will be a late penalty of 5% off per day late! Submissions received more than 3 days late will receive a 0!**

### Part 1

In class you were given an online usertag: `kruegster1990`

NOTE: "briefly describe" = 2-3 sentences (and/or include screenshot(s))

Use OSINT techniques to learn as much as you can about `kruegster1990` and answer the following questions:

1. What is `kruegster1990`'s real name?
  Fred Krueger
2. List all personal information (including social media accounts) you can find about him. For each, briefly detail how you discovered them.
    Reddit - google searched `kruegster1990` and found 'u/kruegster1990' account
    stwity.com - google searched `kruegster1990` and found his location is in Silver Spring, MD, he has 4 tweets, he has one follower and is following one person, his account was created on 12/8/2018, the ID associated with the account is 1028770124772397061,
    cornerstoneairlines.co - googled this website that is on the stwity website and got to the cornerstone airline's website where Fred Krueger is the owner and his email is listed as kruegster1990@tutanota.com
    Instagram - kruester1990 (looked it up on instagram)
    Twitter - kruegster1990 (looked it up on twitter)
3. What is the IP address of the webserver hosting his company's site? How did you discover this?
  I typed 'nslookup www.cornerstoneairlines' into my terminal and the ip address comes up as 142.93.118.186.
4. List any hidden files or directories you found on this website. Did you find any flags?
  <!-- CMSC389R-{h1dden_fl4g_in_s0urce} -->
5. Did you find any other IP addresses associated with this website? What do they link to, or where did you find them?
  Site24x7 also shows the same ip address as above
  142.93.117.193 is the ip address in the source code for the admin page
  view-source:http://cornerstoneairlines.co/index.html
6. If you found any associated server(s), where are they located? How did you discover this?
  By doing an nmap scan on the IP address of the admin page, I found that port 80 is open, "80/tcp   open   http".
  on the IP address 142.93.118.186. 22 is also an open port
  I also found that 2222 was open and 1337 was open.
7. Which operating system is running on the associated server(s)? How did you discover this?
    I searched the Ip address of the admin page on onyphe and got that the server is "Apache/2.4.18 (Ubuntu)"
8. **BONUS:** Did you find any other flags on your OSINT mission? (Up to 9 pts!)
    <!-- CMSC389R-{h1dden_fl4g_in_s0urce} -->


### Part 2

Use the provided python stub code [('stub.py')](stub.py) or write your own program in another language to gain access to the Cornerstone Airlines administrator server via an open port that you should have found in Part 1.

Once you have gained access to the Cornerstone Airlines administrator portal with the correct login credentials, you will have access to a system shell.

Use your knowledge of Linux and OSINT techniques to locate a specific flight record, read it, and submit the flag inside.

Your response here should briefly document how you approached and solved this part of the assignment. You should also push your bruteforce program to the "week/2/writeup" folder of your GitHub repository.

Note: If you choose to write your own program in another language, please include instructions on how to execute your program, including what version of the language you are using. You will **NOT** receive credit if the TAs cannot run your program.

If you are stuck on this part of the assignment, let us know! The facilitator staff is here to help and teach, and we are open to releasing hints as time goes on!

  For this part of the assignment, I ran the command "nmap -p 1-65535 -sV -sS -T4 142.93.117.193" and tried to run all of the open ports which were 80,1337 and 2222 and the host 1337 worked to bring up the prompt "username:". I then wrote the code for the bruteforce program and ran it against the rockyou.txt file. I got the username as kruegster from his email on his website and then the password was pokemon. Once I had the server open I cd'd into home and then flight records and then I did the command "cat AAC27670" because it was on his Instagram. The flag is "CMSC389R-{c0rn3rstone-air-27670}".
### Format
In the "week/2/writeup" directory of our repository there is a README.md file for you to edit and submit your homework in. Use this as a template and directly edit it with your answers. Complete your bruteforce program in this directory as well. When you've finished the assignment, [Push it](https://github.com/UMD-CS-STICs/389Rfall18/blob/master/HW_Submit_Instructions.md) up to your personal GitHub for us to grade.

Your responses to every prompt in this assignment should include answers to any specific questions along with a brief explanation of your thought process and how you obtained the answer.

### Scoring

Part 1 is worth 45 points, and part 2 is worth 55 points.

### Tips

Reference the slides from lecture 2 to help you effectively utilize available OSINT techniques.
