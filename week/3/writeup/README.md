Writeup 3 - OSINT II, OpSec and RE
======

Name: Hope Winovich
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Hope Winovich

## Assignment 3 Writeup

### Part 1 (100 pts)
Vulnerability 1: Weak password

  The first vulnerability of Fred Krueger's company web server is his password. He chose to
go with a common password that is in the rockyou.txt file containing the most commonly used
passwords. Further, his personal Instagram account was full of pictures of Pokemon and
his password was "pokemon". It may even be a hacker's first guess after finding his Instagram.
I strongly suggest not using any dictionary words such as common words, words spelled backwards,
names in your family (kids, spouses, pets), simple number sequences or using the same
password for more than one site. Cornerstone airlines should have a unique and difficult to guess password. Strong passwords include capital letters, lower case letters, numbers and symbols.
An example of a strong password may be "$6e_Y~MDuH@Z6"{:" because there are no common words,
multiple random symbols, a big number of characters, both capital and lower case letters and
a random number. Algorithms can be easily written by hackers to crack common passwords so it
is extremely important to come up with a strong password and make sure to never stay logged in
on your computer and never tell someone the password.

Vulnerability 2: Open Ports

  Another vulnerability that www.cornerstoneairlines.co had was its multiple open ports.
Although it is normal to have a few open ports due to programs listening on those ports,
it is not safe to have unused ports open especially when there is no firewall. I suggest
that Cornerstone Airline's website should have a firewall that would cover all open ports
and close any unused open ports. On windows, according to thewindowsclub.com, you can
manually open and close ports with new rules within the windows firewall. This may be
a handy tip to close some of the ports that were opened. I was able to hack in through
port 1337 so that would be where Fred Krueger should start with closing that port through
the firewall.


Vulnerability 3: Professional Email Address

  One last vulnerability for Cornerstone Airlines is the use of Fred Krueger's personal
email as his contact information for the company. A more professional and low security
risk email address would be something along the lines of "cornerstoneairlines@gmail.com".
The reason that his email address, "kruegster1990", is a security concern is because of
the information that is gives away to a hacker. First, 1990 is most likely the year that
he was born or another significant life event happened, which gives away personal
information to the hacker. Second, the nickname, "kruegster", corresponds to
Fred Krueger's stwity account, twitter account and instagram account. His handles
on instagram and twitter correspond directly to his email address listed on his
company's website, "kruegster1990". This allows a hacker to easily find personal
information on Fred Krueger, like his love for Pokemon on his instagram. It also
is bad professionalism to have a personal email listed on a company's website as
well as it being the same handle for his twitter in which he complains about another
airline.
