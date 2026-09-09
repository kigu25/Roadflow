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
| *Anna* | *43, Trafic analyst at the transport authority, familiar with a computer but not advanced.* | *Need reliable traffic congestion data to plan road maintenence correctly & effectively.* | *Will mostly use the time-slider located next to the map in the dashboard, to get a quick overview of how trafic changes over time & see trafic congestion patterns.* |
| *Johan* | *37, Roadplanner at the transport authority. Good computer knowledge, but not a programmer.* | *Needs a reliable heatmap and correct data.* | *Will be using the heatmap and and needs some raw traffic-data.* |
| *Sven* | *39, Road trafic management, an expert in his specific field of work.* | *Needs a reliable and quick updating heatmap, has suggested ability to view cameras one by one.* | *Sven will us the heatmap to see where trafic is congested in realtime and can use that info to re-route trafic. He also requests to see specific cameras latest pictures if possible.* | 


### Software Requirements

**Functional Requirements**
- *Camera acquisition & continious archive.*
- *AI-vehicle detection and counting.*
- *Interactive web map and historical timeline.*


**Non-Functional Requirements**
- *System should tolerate missing images & temporary source unavailability.*
- *The map should remian responsive while browsing prototype dataset.*
- *Should at least be capable to run locally.*

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

## Documenting Your Project

Once Sprint 2 begins, add a **User Manual** section to this README, covering:
- **Installing** — what's needed to set up your project locally (dependencies, environment, etc.)
- **Running** — how to start/execute the application

