# PA1414 Software Engineering Project HT26

## Project Description

**Project Name:** *RoadFlow*

**Customer Name:** *Oleksii Novikov*

**Student Full Name:** *Kim Gustafsson*

### Project Aim and Objectives

*The goal with RoadFlow is to successfully deliver a software that identifies vehicles on public-roads using AI for object-identification. With those detections the software will archive the images and related metadata & create statistics. These statistics will be used to visualise congestion on roads over-time in a map/heatmap. RoadFlow is intended to be used as a situational-awarness prototype for authorities or companies.*

### User Personas

| Name | Characteristics | Needs and Expectations | How will they use the system? |
|---|---|---|---|
| *Anna* | *43, Road maintenence planner at the transport authority, not much previous computer excperience.* | *Need reliable & correct traffic congestion data over different time/date periods to plan her work correctly & effectively.* | *Will use the map & timeslider, to get a quick overview of how traffic changes over different days.* |
| *Johan* | *37, Roadplanner (new roads) at the transport authority. Good computer knowledge, but not a programmer.* | *Needs a reliable heatmap and correct trafic data. Wants a feature to see raw data* | *Will be using the map/heatmap & check raw data.* |
| *Sven* | *39, Road trafic manager, has lots of experience with computers.* | *Needs a reliable and quick updating heatmap, has suggested ability to view cameras one by one and their latest picture.* | *Will use the heatmap to see where traffic is congested in real-time, uses that info to re-route trafic. He also checks singular cameras one by one.* | 


### Software Requirements

**Functional Requirements**
- *The system shall collect & store image snapshots at a fixed & documented cadence*
- *The system shall collect & store metadata with every image*
- *The system should have a continuos observation period of one week. E.g Mon-Fri*
- *Detect vehicles using AI*
- *Count number of vehicles the AI detects per image*
- *The AI-model's Detection quality should be evaluated using a manually reviewed subset of images*
- *Webpage to visualise the data*
- *Interactive map displaying the camera locations*
- *trafic-heatmap*
- *Historical timeline connected to the map/heatmap*
- *When clicking on a road segment or camera data should appear for that specific section/camera*
- *The interface must clearly distinguish **missing data** from **low traffic***
- *The web application should support filtering*


**Non-Functional Requirements**
- *System should tolerate missing images & temporary source unavailability*
- *The system must not fabricate or replace missing data*
- *The map should remian responsive while browsing prototype dataset*
- *The system has an archive limit of 10GB*
- *Should at least be capable to run locally*

---

## Your Backlog

Your backlog lives in two places, working together:

### 1. GitHub Issues (the content)

For every user story, feature, and task, create a GitHub Issue with a clear title and description. Use the issue template provided in this repository (see `.github/ISSUE_TEMPLATE/`).

Write them in this order:
1. All **user stories** first (format: *"As [a user], I want [action] so that [goal]"*)
2. Then all **features**
3. Then all **tasks**

### 2. Project Board (the backlog itself)

Add every Issue to a Project board. The board is your backlog, not the issue text.

Your repository does not come with a board already set up — see **[PROJECT_BOARD.md](PROJECT_BOARD.md)** for step-by-step instructions on creating your board and setting up the required fields (Priority, Estimated Effort, Sprint). 

You'll need a working board by the end of Sprint 1, as Status Report 3 requires it.


---

## Development

From Week 38 onward:
- Set up your development environment and start development.
- You're free to organise your code however works best for you — for example, using `src/` and `docs/` folders, or any other structure. There's no required folder layout; 
- At the end of each sprint, your work will be demonstrated to the customer at that sprint's Demo
- Keep this README as the one place that always explains how to install and run your project.


Your repository must remain **Private** for the entire course. This protects your customer's requirements and your own work.

---


# User manual
This software is tested on Python 3.13

Before installation, make sure that the following is installed on your pc.
- Python 3.13 or newer
- MySQL Server
- MySQL Workbench



<br>


# Windows installation:

### 1. Clone the repo
- Use the standard github clone commands to clone the project

### 2. Create a virtual environment (venv)
- `python -m venv .venv`

### 3. Activate the virtual environment (venv)
- Using a powershell terminal, run the command `.venv\Scripts\activate`

### 4. Install all the necessary packages & dependencies
- Using that same terminal, run `pip install -r requirements.txt`

### 5. Create a database with mysql-workbench
- Open MySQL Workbench and create a new connection.
- Double-click the connection to open it.
- Go to `File` -> `Open SQL script...` and select `setup_query.sql`, found in `DB_config` folder.
- Click the lightning bolt (Execute) to run the whole setup sql file. This will create all tables needed.

### 6. Change the .env.dummy
- Inside the project folder you'll find a file called `.env.dummy`. Please change the name of the file to `.env`. 
- Fill in your corresponding credentials for: `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD`, `trafikverket_api_key`. <br> 
- Make sure that `DB_PORT` is numeric and don't change the `DB_NAME`.

    **This step is crucial. Follow it!**

### 7. Done 
- Now the installation part is done, check running section to see how to run the software.
<br><br>

# Run the software:

### First time you start the software
- Run main with this flag `python main.py --setup`, this will create everything needed to run the software later.

### Standard-run process
- run `python main.py`, this will start the applications webpage and set the timer for the image_pipeline
- In the terminal a link to localhost where the webpage will be is output. Open that link.

