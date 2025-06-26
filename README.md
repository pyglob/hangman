# Hangman

      simple Hangman game in python

                  _    _ 
                 | |  | | 
                 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
                 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
                 | |  | | (_| | | | | (_| | | | | | | (_| | | | | 
                 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| 
                                      __/ | 
                                     |___/ 

Hangman is a game which a user needs to guess a whole word

The number of blank spaces representing the word is displayed (dashes)

2. Guesses:
    The word guesser takes turns suggesting letters one at a time. 
The word setter indicates if the guessed letter is in the word and its correct positions. 
If the letter is correct, it is filled in the blank spaces. 
If the letter is incorrect, a part of the hanged man is drawn. 
The word guesser can also guess the whole word at any time. 

3. Winning and Losing:
    The word guesser wins if they correctly guess all the letters before the hanged man is completed.
    The word guesser loses if the hanged man is completed before they guess all the letters.


there are 2 files in this repo
hangman.py for running the game
and a word.txt with the list of words






Hangman game in Python using Jenkins automation

Welcome to the Hangman Automation Demo App—a simple, containerized Python game showcasing CI/CD automation with Jenkins,
Ansible, and Docker.


Overview

This project demonstrates how to automate the deployment and execution of a Python-based Hangman game using a Jenkins pipeline,
Ansible for environment setup, and Docker for containerization. All required files are managed in a GitHub repository and 
automatically delivered to a CentOS 8 system, where the game runs inside an Ubuntu-based Docker container with Python 3.10


Features

    Automated CI/CD: Jenkins pipeline builds the Docker image and deploys the latest version to your host.

    Stateless Execution: No containers are kept running; each game session launches a fresh container.

    Easy Access: Play the game by simply typing hangman in your CentOS shell—no manual Docker commands required.


Prerequisites
    CentOS 8 target system
    Jenkins for CI/CD automation
    Ansible for environment preparation
    Docker (or containerd) installed on the target system


Setup Instructions

1. Clone the repository (if you want to review or customize files):

     git clone https://github.com/yourusername/hangman-automation-demo.git



2. Jenkins Pipeline:

    Jenkins will:

        Build the Docker image from the latest commit.

        Tag the image as anewpipe:latest.

        Copy the hangman script from the repository to /usr/local/bin/hangman on your CentOS system.

        Ensure the script is executable.


3. The /usr/local/bin/hangman Script:
      This script dynamically selects the latest anewpipe:latest image and runs the game in a new container:

         #!/bin/bash
         # Find the most recently built 'anewpipe' image (by tag or latest)
         IMAGE=$(docker images --format '{{.Repository}}:{{.Tag}} {{.CreatedAt}}' | \
              grep '^anewpipe:' | sort -rk2 | head -n1 | awk '{print $1}')
          
          if [ -z "$IMAGE" ]; then
              echo "No anewpipe image found."
              exit 1
          fi
          
          # Run the game in a new, temporary container
          docker run --rm -it "$IMAGE" hangman


1. How to Play

    Type hangman in your CentOS shell:
	
	hangman

2. Game Flow:

    The game uses a words.txt file inside the container.
    Press Enter to use the default words file.
    When prompted for "Enter index:", type any number to select a word from the file.
    The Hangman game starts. Guess letters as prompted.
    After winning or losing, the container exits automatically.
    To play again, simply type hangman once more.



Example Game Session

      Welcome to the game Hangman

                  _    _
                 | |  | |
                 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
                 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
                 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
                 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                      __/ |
                                     |___/

      Enter file path [/app/words.txt]:
      Enter index:
      
      Let's start
      
          x-------x
      _ _ _
      Guess a letter: a
      :(
          x-------x
          |
          |
          |
          |
          |
      
      _ _ _
      Guess a letter:



Maintenance
    Jenkins will always update the anewpipe:latest image after each build, ensuring you play the newest version every time.
    No containers are left running after the game ends
	





