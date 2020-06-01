# Project for IS 601 - Summer 2020

Features, issues, etc are listed in [issues](https://github.com/cicorias/njit-is601-project/issues)

# Feature List
- survey type are different apps
- a survey is an instance that permits
  - 1 or more questions
  - a creator
  - submitters
  - tally
- question types are:
  - multiple choice with a single selection
  - multiple choice with more than 1 selection
  - feedback type
- protected by a login provided (Auth0 or similar)
  - roles from provider
  - stretch add social login with permitted
  - allow multiple credentials "per" profile


# Short term actions
- dockerize as needed - web tier, data tier
- add application for 'survey type A' 
- Models and database setup for surveys[template, instance, question types, questions], users
- integrate login with external WebSSO like Auth0 



## Background and Description
Within my engineering organization we constantly do Team surveys requesting feedback on various things such as:
- Project Pulse - these are general questions gauging aggregate team member's morale, confidence, boredom, etc.
- Engineering Practices - our team is rated on following proper engineering practices and this survey done monthly allows Team members to provide their perspective which hopefully coincides with Leadership indicators. Things like CI/CD, Process adherence, testing practices.
- Retrospective Feedback - retrospectives provide for process improvement, often we do a "glad, sad, mad" and capture topics for discussion and process improvement ideas that the Team can drive.

## High Level Approach
Basic Form oriented app providing for
* logon page
* setting up a survey
* getting link for survey (anonymous) potentially with single use OTP or generaged nonce to prevent DoS and sharing
* Admin view
* Authoring view
* Respondent view

# Planned Technical Implementation
* Django project
* Perhaps 3 different applications for the "types" of surveys
* Authentication using "self issues" credentials as part of signup
* Use of OAuth2 for Google, Twitter, Microsoft logon - maybe use `social-auth-app-django` or `django-allauth`
```
social-auth-app-django==3.1.0
social-auth-core[azuread]==3.0.0
```
* n-tier with Web, API tiers, along with DB tier via Django Models
  - web tier React JS, bootstrap styling
  - Single Page App "like" - using API tier for data calls via React JS services
* Persistence using Python ORM / PostGres or Sqlite
* Containerized - docker-compose app, service, and db tier
