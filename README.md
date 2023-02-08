# Project 1 Cloud Continuous Delivery of Microservice (Data Engineering Focused)

## Key Objectives of Project
In project 1, the purpose is to build cloud continuous delivery of Microservice in FlaskAPI through Data Engineering. I build a simple Automatic Coin Value Calculator FlaskAPI, this algorithm can be applied in the automatic change registers in supermarkets. It is used to find the coin value for the cashiers when customers using coin to pay for the goods or services. According to the formula of the Coin Values Calculator: Dollar = $1, Quarter = $0.25, Dime = $0.1, Nickel = $0.05, Penny = $0.01, once the user type dollars and cents, the microservice will return their change. For example, if you have $1.34, it will return:"{5: 'Quarters'}, {1: 'Nickels'}, {4: 'Pennies'}". That is, 4 pennies + 1 nickel + 5 quarters = $1.34

## Structure Diagram
<img width="1139" alt="Screen Shot 2023-01-24 at 1 22 52 AM" src="https://user-images.githubusercontent.com/112274822/214225298-7b69851b-aac0-43bc-a330-e9ef07bf5ecb.png">

## Demo Video Link
https://teams.microsoft.com/l/message/19:53b60ceaebe2478e8cc1508cb3b4eb07@thread.tacv2/1675307470656?tenantId=cb72c54e-4a31-4d9e-b14a-1ea36dfac94c&groupId=7757ff33-20f5-434b-8d0b-5fe61b251c34&parentMessageId=1675307470656&teamName=IDS-721-Spring-2023&channelName=Week%203%20Individual%20Project%201&createdTime=1675307470656&allowXTenantAccess=false

## Preparation
### 1. Containerization: Setup virtual environment
A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them. 
* Type: `python3 -m venv env` and `source env/bin/activate`

### 2. Setup continuous integration via a new workflow at Github
A workflow is a configurable automated process that will run one or more jobs. Workflows are defined by a YAML file checked in to your repository and will run when triggered by an event in your repository, or they can be triggered manually, or at a defined schedule.
* Go to the homepage of the repository, cilck the button "Actions", choose "set up a workflow yourself".
* Name it as "test.yml", type the code you need, then click the green button "start commit".
* Once complete these steps, you can check the status of your workflows from "Actions" page, so that make sure your program could pass the tests. Otherwise, you need to fix the code where the bugs/errors arw reported.
* eg. Check out code for issues such as pylint and pytest errors:
<img width="831" alt="Screen Shot 2023-01-23 at 11 27 09 PM" src="https://user-images.githubusercontent.com/112274822/214212463-899e3fe6-b653-46c9-8b9a-ef987dcff984.png">

### 3. Add requirements.txt
Requirement. txt file is a type of file that usually stores information about all the libraries, modules, and packages in itself that are used while developing a particular project. It also stores all files and packages on which that project is dependent or requires to run. Here are the packages I will use for this project:

<img width="185" alt="Screen Shot 2023-01-23 at 11 29 29 PM" src="https://user-images.githubusercontent.com/112274822/214212510-891f470a-d8eb-42ba-ae1d-755904f6baff.png">

### 4. Create a Makefile
A makefile is a special file that lists a set of rules for compiling a project. These rules include targets, which can be an action make needs to take (eg. "clean" or "build") or the files/objects make will need to build, and the commands that need to be run in order to build that target. 
* Type: `touch Makefile` and `make install` after adding requirement.txt
<img width="396" alt="Screen Shot 2023-01-23 at 11 28 58 PM" src="https://user-images.githubusercontent.com/112274822/214212594-a3a66e41-9596-413a-9c68-ec2b798c7600.png">

## Steps of Configure Build Server to Deploy Changes on build (Continuous Delivery)

### 1. Create a Microservice
* Run APP after creating app.py: `python app.py` (Press CTRL+C to quit)
<img width="857" alt="Screen Shot 2023-01-23 at 11 28 23 PM" src="https://user-images.githubusercontent.com/112274822/214214608-00675d98-0708-456e-b483-eeb46a2ac43c.png">
<img width="1158" alt="Screen Shot 2023-01-23 at 11 53 01 PM" src="https://user-images.githubusercontent.com/112274822/214214837-2040d1f2-b7e2-45d9-b9db-c3e43f46bb8c.png">

* Usage of examples (Test the URL): https://helenyjx-miniature-space-capybara-p46qgq5qg79crp5w-8080.preview.app.github.dev/change/2/17
<img width="815" alt="Screen Shot 2023-01-23 at 11 18 28 PM" src="https://user-images.githubusercontent.com/112274822/214215017-e41c480c-222c-4195-9974-5b8a080db58a.png">
<img width="807" alt="Screen Shot 2023-01-23 at 11 18 01 PM" src="https://user-images.githubusercontent.com/112274822/214215056-122e698e-e670-48be-a590-b44b74d19f7a.png">

### 2. Configure Build System to Deploy changes
#### 1). Use AWS App Runner to deploy code
* AWS App Runner is a fully managed container application service that lets you build, deploy, and run containerized web applications and API services. Below are the steps when we use github repository at AWS App Runner: 
<img width="880" alt="Screen Shot 2023-01-23 at 8 45 12 PM" src="https://user-images.githubusercontent.com/112274822/214215786-c11c273c-3854-4d08-a4b3-ff067275f900.png">
<img width="874" alt="Screen Shot 2023-01-23 at 8 47 04 PM" src="https://user-images.githubusercontent.com/112274822/214215787-28283b0f-dad8-48a5-9901-29cd9c127eef.png">
<img width="915" alt="Screen Shot 2023-01-23 at 8 49 00 PM" src="https://user-images.githubusercontent.com/112274822/214215789-b17168fa-6803-45ae-a41a-677d5b717a61.png">

* Once we click "review and create", it will turn to this page, and we only need to wait for running deployment.
<img width="1406" alt="Screen Shot 2023-01-23 at 10 12 55 PM" src="https://user-images.githubusercontent.com/112274822/214216616-a4f487cd-073c-4425-867c-a9b1335f2757.png">

* Finally, check the "Event status" under deployment logs, so that make sure you pass all tests successfully. Otherwise, please find the errors from "Event log" to debug.
* We use the link above (https://anca32dvu7.us-east-2.awsapprunner.com) to check app.py again
<img width="415" alt="Screen Shot 2023-01-24 at 12 20 46 AM" src="https://user-images.githubusercontent.com/112274822/214217706-9a18f15d-8a57-461f-827e-6592d355f518.png">
<img width="976" alt="Screen Shot 2023-01-23 at 10 11 16 PM" src="https://user-images.githubusercontent.com/112274822/214217100-72fa038d-f278-42ce-af68-9a7f1ed03e70.png">

* Usage of examples (Test the URL):anca32dvu7.us-east-2.awsapprunner.com/change/1/38
<img width="692" alt="Screen Shot 2023-01-23 at 10 12 34 PM" src="https://user-images.githubusercontent.com/112274822/214217102-8a58ad86-46cb-49da-b6c1-1b9c6b6ddeb8.png">

#### 2). After using IaC (Infrastructure as Code) via AWS APP Runner, check it in CloudFormation
* CloudFormation uses YAML or JSON, it is a popular cloud infrastructure automation tool coming from the IaaS giant AWS. It enables organizations to easily create, deploy and manage the AWS resource stack using a template or a text file that acts as a single source of truth.
* Login to AWS, go to CloudFormation and then click "Stack", we can check our code status based on the project that we just deploy at the AWS APP Runner, and then choose below "Events".
<img width="1286" alt="Screen Shot 2023-01-23 at 10 35 54 PM" src="https://user-images.githubusercontent.com/112274822/214215670-05586370-c2f3-459f-bd3d-dd3e79e6da29.png">
