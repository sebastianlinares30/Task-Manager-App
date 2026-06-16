# Software Requirements Specification
## For Task Manager application

Version 1.0  
Prepared by Sebastian Linares  
Group: CS 2450 - Group 2   
Date Modified: June 11th, 2026

## Table of Contents
<!-- TOC -->
* [1. Introduction](#1-introduction)
    * [1.1 Document Purpose](#11-document-purpose)
    * [1.2 Product Scope](#12-product-scope)
    * [1.3 Definitions, Acronyms, and Abbreviations](#13-definitions-acronyms-and-abbreviations)
    * [1.4 References](#14-references)
    * [1.5 Document Overview](#15-document-overview)
* [2. Product Overview](#2-product-overview)
    * [2.1 Product Perspective](#21-product-perspective)
    * [2.2 Product Functions](#22-product-functions)
    * [2.3 Product Constraints](#23-product-constraints)
    * [2.4 User Characteristics](#24-user-characteristics)
    * [2.5 Assumptions and Dependencies](#25-assumptions-and-dependencies)
* [3. Requirements](#3-requirements)
    * [3.1 External Interfaces](#31-external-interfaces)
    * [3.2 Functional](#32-functional)
    * [3.3 Quality of Service](#33-quality-of-service)
    * [3.4 Compliance](#34-compliance)
    * [3.5 Design and Implementation](#35-design-and-implementation)
* [4. Verification](#4-verification)
* [5. Appendixes](#5-Appendixes)
<!-- TOC -->

## Revision History

| Name            | Date     | Reason For Changes | Version |
|:---------------:|:--------:|:------------------:|:-------:|
|Sebastian Linares|06/15/2026|SRS Creation        |1.0      |
|                 |          |                    |         |

## 1. Introduction
This document will provide a detailed description of the Task Manager application functionality, features, and overall performance. The Task Manager application is an application that currently allows college students to track tasks. Individuals from Group 2 belonging to the CS 2450 X02 Summer 2026 class at Utah Valley University will also be referencing this document to review, enhance, and reference details pertaining to the creation of the Task Manager application. The table of contents organizes this document and breaks this document into three parts which are the introduction section that has definitions on verbiage used, scope of product, and product overview. The product overview section which documents information strictly to the product and the requirements section which holds information on interfaces and performance. 

### 1.1 Document Purpose
This SRS exists so that Alexander Anderson, Dario Coreas, and Sebastian Linares from Group 2 have a point of reference that defines the Task Manager application. This will assist in development of the product to ensure the application does what it is supposed to do. With college students being the primary target audience, user stories have shaped the features that this application will have. Defining these features and the user experience will help keep Group 2 on track to develop the needed features for this application.

### 1.2 Product Scope
<!-- the product (name/version), its primary purpose, key capabilities, and boundaries. keep brief and focus on the "what" and "why", not the "how" -->
Version 1.0
* This version currently allows a user to enter a task name so the user knows what their tasks is. It also allows a user to set a due date for the tasks so the user is aware of when they need to have the task completed by. These two features are currently able to be fulfilled after a user uses the command-line interface to type in the necessary details. 

### 1.3 Definitions, Acronyms, and Abbreviations
<!-- glossary of domain terms, acronyms, and abbreviations; keep entries alphabetized -->

| Term | Definition |
|------|------------|
| CS   | Computer Science             |
| CLI  | Command-Line Interface       |
| MTBF | Mean Time Between Failures   |
| MTTR | Mean Time to Recovery/Repair |
| PC   | Personal Computer            |

### 1.4 References
<!-- normative and informative external sources; include title, owner, version, date, location/URL, and whether it is normative or informative -->
Informative
* https://kivy.org/doc/stable/

### 1.5 Document Overview
<!-- document structure and conventions -->
Product Overview
* This section will cover details such as origin, constraints, characteristics, and dependencies.

Requirements
* This section holds information on interfaces, quality of service, and performance. 

## 2. Product Overview
<!-- background and context that shape the product's requirements -->
This product was formed by recognizing the complex schedule college students have to abide by. To address this exisiting challenge, the Task Manager application will be developed to help college students organize their day/week/month/year.

### 2.1 Product Perspective
<!-- context of the system: a new product, a replacement, or part of a family; note relationships to other systems -->
Origin
* This is a replacement product that would provide an alternate option for college students to manage their schedules.

Ownership
* Scrum methodology is used with a bi-weekly rotation on roles. Github project board is utilized to keep track of ownership with the scrum master being responsible for ensuring deadlines are met and backlog has ownership. 

### 2.2 Product Functions
<!-- major functional areas or features the product provides in 5–10 concise bullets -->
* Add/edit tasks
* Add/edit due dates
* Group tasks
* Add task descriptions
* Color code tasks based on priority

### 2.3 Product Constraints
<!-- design and implementation constraints that affect the solution -->
* Application is built on Python 3.x. 
* Application accepts user input through the CLI.

### 2.4 User Characteristics
<!-- classes, roles, expertise, access levels, frequency of use, and accessibility or localization needs -->
This application does not have user roles not restricted access based on personas. 

### 2.5 Assumptions and Dependencies
<!-- assumptions about environment, third-party services, usage patterns, and other external factors; note potential impact/risk. -->
Dependencies
* Limited to PCs and laptops.

## 3. Requirements
<!-- identifiable, verifiable, testable requirements; avoid implementation details -->
* Feature 1
    * ID: REQ-FUNC-001
    * Title: Add/Edit Tasks
    * Statement: The system shall allow a user to enter the name and edit the name of a task. 
    * Rationale: With task tracking being the main function of this application, adding and editing tasks is important for the functionality of the application. 
    * Acceptance Criteria: Users can add/edit a task from the home page. 
    * Verification Method: Test

* Feature 2
    * ID: REQ-FUNC-002
    * Title: Add/Edit Due Dates
    * Statement: The system shall allow a user to add and edit due dates. 
    * Rationale: Managing tasks require a deadline. 
    * Acceptance: User can add/edit the due date when making their task from the home page.
    * Verification Method: Test

### 3.1 External Interfaces
<!-- inputs/outputs (formats, protocols, timing, etc); reference interface schemas where available. -->

#### 3.1.1 User Interfaces
<!-- user interactions (UI elements, dialogs, flows); reference design/style guides -->
* Users will have the option to initiate adding a task by clicking a button on the home page. This button will open a following screen that will require user input on the task name and due date. Once the user has typed in the requested details, the user will then have the option of saving the task by clicking on a confirmation button. Users will also have the ability to select an existing task on the home page and delete it by selecting a deletion button that will appear after the task is selected. 

### 3.2 Functions
<!-- externally observable behaviors organized by feature/use case -->
* Users can add tasks that will be visible on the home page. 
* Users will be able to view due dates on the home page. 

### 3.3 Quality of Service
<!-- measurable non-functional attributes section -->

#### 3.3.1 Performance
<!-- time (latency, throughput, etc.) and space (memory, storage, bandwidth, etc.) -->

#### 3.3.2 Reliability
<!-- ability to consistently perform as specified (MTBF, redundancy/failover, caches, etc) -->
MTTR
* In the event of a system crash, the application should recover all entered tasks upon relaunch.

MTBF
* This application should maintain unlimited hours of continous runtime. 

#### 3.3.3 Availability
<!-- readiness to deliver service (target SLAs, maintenance windows, recovery/restore, etc) -->
Target Uptime
* 99.99% annually.

### 3.4 Compliance
<!-- laws, standards, contracts, or policies; cite the authority and verifiable criteria. -->
Not applicable at this time. 

### 3.5 Design and Implementation
<!-- constraints and mandates on design, deployment, and maintenance section -->

#### 3.5.1 Installation
<!-- ensure software runs smoothly in its target environments (supported platforms, prerequisites, configuration, etc) -->
Supported
* Windows

#### 3.5.2 Build and Delivery
<!-- controls for building and delivering (dependency management, automation, integrity/traceability, etc) -->
Build Requirements
* Python 3.x

Delivery Requirements
* Software updates shall only be released after successful manual testing.

#### 3.5.3 Distribution
<!-- distributed deployments, data, and devices (topologies, replication/placement, etc) -->
Single Machine Application
* Application executes on single local client device.

#### 3.5.4 Maintainability
<!-- measurable attributes that make the software easier to modify, fix, and evolve (modularity, standards, documentation, observability, etc) -->
This application will have a modular approach to organize what each block of code will do. 

#### 3.5.5 Reusability
Modular components will be reused where applicable. 

#### 3.5.6 Portability
<!-- ability to run on multiple environments (supported OSs/runtimes, cloud providers, etc) -->
The system currently requires Python 3.x to run at this time. 

#### 3.5.7 Deadline
<!-- milestones, delivery dates, and readiness criteria -->
* Milestone 1
    * 06/01/26

* Milestone 2
    * 06/15/26

* Milestone 3 
    * 07/06/26

* Milestone 4
    * 07/13/26

* Milestone 5
    * 07/20/26

#### 3.5.8 Proof of Concept
<!-- objectives, scope, timebox, and success criteria for any POC -->
Purpose
* Provide a method for college students to maintain tasks. 

Scope
* The Task Manager application will allow college students to manage tasks. 

* The Task Manager application does not guarantee increased productivity.

#### 3.5.9 Change Management
<!-- how changes are introduced and communicated (categories, required artifacts and workflow, etc) -->
* Changes are discussed in bi-weekly meetings with Group 2 in attendance. Scrum methodology is used, allowing for feature implementations to be developed in sprints with Group 2 determining priority on changes. 


## 4. Verification

| Requirement ID | Verification Method | Test/Artifact Link | Status | Evidence |
|----------------|---------------------|--------------------|--------|----------|
|                |                     |                    |        |          |
|                |                     |                    |        |          |

## 5. Appendixes