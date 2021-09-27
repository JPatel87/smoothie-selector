# Smoothie Selector

Smoothie Selector is an interactive command line program which aims to help users decide on which smoothie to make. It is targeting users who are interested in making smoothies based on their nutritional value. The program iterates through a series of questions in order to narrow the smoothie choice selection down for the user based on their responses. 

# UX

## Site Owner Goals

The objectives of the site owner are: 
* To create a user friendly, attractive, command line program that is easier to follow.
* To create a program that is useful for target users.
* To create a program to that is of industry standard.

## User Stories

User would like:

* To be able to open up the program and immediately be able to grasp what its purpose is.
* The program is clean and consistent in layout.
* The program is easier to follow through.
* The program asks relevant questions to help narrow down smoothie recipes that I can choose from.

# Features

## Existing Features

* Title 
    * The title is enclosed between two fruit emoji's either side of it. The purpose of this is to add colour and a fun aspect to the command line and make the program appealing. 
    * The emoji external python library has been used here.

* Questions and Inputs
    * The question and input prompts have been styled with colour, consistently throughout the program. This is so that users are clearly able to see where their input is required.
    * Both appear in yellow font.
    * The question print statements are additionally highlighted on a red background, to distinguish it from the input prompt.

# Deployment

This program was deployed to Heroku, following the below steps:

1) Push most up-to-date code to Github

2) Create a list of requirements by typing the following into the terminal:
pip3 freeze > requirements.txt

3) Push the requirements to Github

4) Logon to Heroku

5) Select create new app 

6) Add app name 

7) Add app region

8) Select 'Create app'

9) Open up the Settings tab, on the top ribbon

10) In 'Config Vars' select 'Reveal Config Vars'

11) Add 'PORT' as a key and '8000' as a value

12) In 'Buildpacks' select 'Add buildpack' and choose python. Then, repeat for nodejs (order is important; python first followed by nodejs) 

13) Navigate to 'Deploy' on the top ribbon

14) In 'Deployment method', select 'Github', once clicked it should say 'connected'

15) Enter a repository in Github to connect to and click 'Search'

16) Once repository has been found, click 'Connect' to link new app to Github repository

17) In 'Automatic deploys', select the 'Enable Automatic Deploy' option

18) To view your command line on the Heroku platform, once a new code has been pushed to Github, log on to Heroku

19) Select the required app that appears on your home screen

20) Select 'Open app' on the right hand side of the screen 

21) The app should appear in a new tab on the web browser

22) The link to my Heroku app is:
https://smoothie-selector.herokuapp.com/

23) The Github link for this project is:
https://github.com/JPatel87/smoothie-selector




# Credits 

## Content

* Code institute for providing a python essentials template to work from.
* The following recipe websites which were used to obtain all my recipes; [bbc good food](https://www.bbcgoodfood.com/recipes), [downshifology](https://downshiftology.com/), [jar of lemons](https://www.jaroflemons.com/), [clean eating magazine](https://www.cleaneatingmag.com/) and [vitamix](https://www.vitamix.com/us/en_us/).
* To create a flowchart for my project [diagrams.net](https://app.diagrams.net/) was used. 
* The external python library [termcolor](https://pypi.org/project/termcolor/) was used to import colour to text.
* The emojis used in this program were codes taken from the [Unicode Consortium](http://www.unicode.org/emoji/charts/full-emoji-list.html).
* Instructions on how to install and use the python external library termcolor was taken from the youtube channel [Language Programs](https://www.youtube.com/watch?v=tLYHMKeeFIU).
* Instructions on how to add time delays to code were taken from the website [Real Python](https://realpython.com/python-sleep/).
* For general troubleshooting advice, the following websites were used; [Code Institute](https://codeinstitute.net/5-day-coding-challenge/?utm_term=code%20institute&utm_campaign=a%26c_SEA_UK_BR_Brand_Code_Institute&utm_source=adwords&utm_medium=ppc&hsa_acc=8983321581&hsa_cam=1578649861&hsa_grp=62188641240&hsa_ad=492338271836&hsa_src=g&hsa_tgt=kwd-319867646331&hsa_kw=code%20institute&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gclid=EAIaIQobChMI9OSlzraT8wIVgbTtCh0lSQINEAAYASAAEgJHFvD_BwE) Python Essentials module and love sandwiches walk-through project,  [Stack Overflow](https://stackoverflow.com/) and [W3 Schools](https://www.w3schools.com/).

## Acknowledgements

This project has been an eye-opening experience for me to develop a command line program that looks appealing and is able to manipulate data to deliver results. My thanks goes to Code Institute tutor support who have been fantastic at answering all my queries and my tutor, Seun Owonikoko, for her insight and guidance.
