# PythonFlaskWebApplication

Fortinet Challenge: The project is a task to upload a text file through a simple WebApp and fetch the API responses from VirusTotal API. Show the results in one table format on WebApp.

## Installation:

Install python3.10.5 https://www.python.org/downloads/release/python-3105/

Clone the repository using command: git clone https://github.com/Yashvi10/fortinet.git

# Install requests for VirusTotal API: 
  pip3 install requests
  
# Run the project:
  python main.py -d
  
## General Summary of project files or code layout:
   1. main.py is the main file in the project containing functions of logic.
   2. Directory named /templates include index.html and result.html file containing webapp front development logic.
   3. Includes sample_hash_input.txt file under project directory.
   4. A directory named Demo Video includes a small project video presenting how it works and explaining the code logic.
   5. DockerFile contains commands to containerize the project.
   
  ## Tech Stack Used: Python, Flask, Linux OS image, Docker container.
  
  ## Issues encountered:
    1. I was under learning phase of python so faced some difficulties in writing the correct syntax at one time but then a little research work helped me very well. 
    2. Faced some errors while working like NoneType, loop errors, etc but resolved it by understanding working flow of code. Learned and understood Flask to develop webapp. 
    3. Found difficulty in figuring out why API responses are throwing error continuously. But then with proper observation and analysis found that it is error 204 which indicates
       limit exceeded in requesting API responses. So, added validation in the code to make it work that if response is 200 then only go ahead.
       
 ## Note:
    It was a good learning expeience for me and it helped me learn many new things.
