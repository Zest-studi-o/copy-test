# THE RESTAURANT BOOKING SYSTEM

![The Restaurant Booking system](link)

A web application that enables users to know more about the restaurant, manage bookings and view the menu, as well as a tool for restaurant owners and staff to organise their bookings.

Visit the live site: [My restaurant booking system](https://megarestaurant-20c7141b277b.herokuapp.com/)

# Table of contents

- [User Experience (UX)](#User-Experience-UX)

  - [User Stories](#User-Stories)

- [Design](#Design)

  - [Flowchart](#Flowchart)
  - [Features](#Features)

- [Technologies Used](#Technologies-Used)

  - [Languages Used](#languages-used)
  - [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

- [Deployment & Local Development](#Deployment--Local-Development)

  - [Deployment](#Deployment)
  - [Local Development](#Local-Development)
    - [How to Fork](#How-to-Fork)
    - [How to Clone](#How-to-Clone)

- [Testing](#Testing)

- [Credits](#Credits)
  - [Code Used](#code-used)
  - [Content](#content)
  - [Media](#media)
  - [Acknowledgments](#Acknowledgments)

---

## User Experience (UX)

#### Key information for the site

This section provides insight into the UX process, with a focus on the people who this restaurant booking system has been created for, the main aims of the project and how it can help users to meet their needs.

Project goals:

- To encourage people to know and book in the restaurant.

- To provide an easy and user-friendly web app where users can book and know more.

- To provide a system where restaurant owners and staff can manage bookings and interact with customers.

### User Stories

|   EPIC                                |ID|                                User Story                                                   |
| :-------------------------------------|--|:------------------------------------------------------------------------------------------- |
|**CONTENT AND NAVIGATION**             |  ||
|                                       |1A| As a user, I want to see a menu so I can easily access all the content |             
|                                       |1B| As a user, I want to see relevant information about the restaurant|
|                                       |1C| As a user, I want the website to have a nice and intuitive design that will match the restaurant's theme|
|**USER REGISTRATION/AUTENTHICATION**   |  || 
|                                       |2A| As a user, I want to be able to register on the website|
|                                       |2B| As a user, I want to be able to authenticate using only email and password|
|                                       |2C| As a user, I want to be able to log out at any time|
|**BOOKING**                            |  ||
|                                       |3A| As a logged-in user, I want to be able to find the available tables for a specific date and time|
|                                       |3B| As a logged-in user, I want to be able to select the table that I want to reserve|
|**MENU**                               |  ||
|                                       |4A| As a user, I want to see the restaurant's menu with details about description, category and price, so that I can make an informed decision|                                  
|**USER PROFILE**                       |  ||
|                                       |5A| As a logged-in user, I want to view a list of my upcoming bookings|
|                                       |5B| As a logged-in user, I want to be able to edit my bookings|
|                                       |5C| As a logged-in user, I want to be able to delete my bookings|
|**ADMIN MANAGE BOOKINGS**              |  ||
|                                       |6A| As a logged-in admin member, I want to see the restaurant's upcoming bookings for the current day sorted by time|
|                                       |6B| As a logged-in admin member, I want to be able to filter bookings by date|
|**CONTACT**                            |  ||
|                                       |7A| As a user, I want to see the restaurant's opening and closing hours|
|                                       |7B| As a user, I want to see location information on the website|
|                                       |7C| As a user, I want to see contact information on the website|

---

## Design

### Flowchart

![Flowchart](flowchart.jpeg)

### Features

#### Existing Features

**Logo**

- The website visual identity.

![Logo](image)

**Colour Palette**

Extracted from a picture with healthy restaurant theme, which was picked for the cover image, using the colour picker, after picking the cover image this matching colour palette was selected using [Coolors](https://coolors.co/) and other pictures containing the same colour scheme for a consistent visual design.

![Colour palette](docs/readme/colour-palette.png)
---

### Features Left to Implement

In the future, I would like to:

- Feature not implemented

---

## Technologies Used

### Languages Used

The language used is Python

### Frameworks, Libraries & Programs Used

[Lucid chart](https://www.lucidchart.com/pages/) - Used to create flowcharts.

[Git](https://git-scm.com/) - For version control.

[GitHub](https://github.com/) - To save and store the files for the website.

[Shields](https://shields.io/) - To add badges to the readme file.

[Amiresponsive](https://ui.dev/amiresponsive) - To generate a mockup in different screen sizes.

[Bandicam](https://www.bandicam.com/es/) - To screen record bugs and features.

[Windows photo feature](https://www.microsoft.com/en-us/windows/photo-movie-editor) - To trim screen recording.

[Veed](https://www.veed.io/convert/mp4-to-gif?gad=1&gclid=CjwKCAjwgqejBhBAEiwAuWHioCzHSc5XTTdsnixrxavlvLKEi4i_YeN__Xol0nANQCBhw60caeyF3RoC31wQAvD_BwE) - To convert mp4 to gif

[Heroku](https://id.heroku.com/) - To deploy the App.

[Code Institute template](https://github.com/Code-Institute-Org/p3-template) - To run the game in the terminal using Heroku.

[Django](https://www.djangoproject.com/) - Web Framework.

[Elephantsql](https://www.elephantsql.com/) - PostgreSQL as a Service.

[Cloudinary](https://cloudinary.com/) - For storing static data

## Deployment & Local Development

### Deployment

- This site was deployed by completing the following steps:

####  Django
In order to protect the django app secret key it was set as environment variable and stored in env.py file

####  Heroku
1. Log in to [Heroku](https://id.heroku.com) or create an account
2. Click “New”
3. Click “Create new app”
4. Give your app a name and select the region closest to you. When you’re done, click “Create app” to confirm
5. Open the Settings tab and add the config vars

####  ElephantSQL
1. Log in to [ElephantSQL](https://www.elephantsql.com/) or create an account
2. Click “Create New Instance”
3. Set up your plan
 - Give your plan a Name (this is commonly the name of the project)
 - Select the Tiny Turtle (Free) plan
 - You can leave the Tags field blank
4. Select “Select Region”
5. Select a data center near you
6. Then click “Review”
7. Check your details are correct and then click “Create instance”
8. Return to the ElephantSQL dashboard and click on the database instance name for this project
9. In the URL section, click the copy icon to copy the database URL
10. Paste this URL into env.py file as DATABASE_URL value and save the file.


####  Cloudinary
1. Log in to [Cloudinary](https://cloudinary.com/) or create an account
2. Navigate to dashboard/console https://console.cloudinary.com/console/ and copy API Enviroment variable starting with "cloudinary://".
3. Paste copied url into env.py file as CLOUDINARY_URL value and save the file.


### Local Development

#### How to Fork

To fork the Zest-studi-o/p04-restaurant-bookings repository:

1. Log in (or sign up) to Github.
2. Go to the repository for this project, Zest-studi-o/P03-Hangman.
3. Click the Fork button in the top right corner.

#### How to Clone

To clone the Zest-studi-o/p04-restaurant-bookings repository:

1. Log in (or sign up) to GitHub.
2. Go to the repository for this project, Zest-studi-o/Zest-studi-o/P03-Hangman.
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.

---

## Testing

Please refer to [TESTING.md](TESTING.md) file for all testing carried out.

## Credits

### Code Used

- [Title](link)

### Content

- [Title](link)

### Media

- [Ramen bowl](https://www.pexels.com/photo/a-bowl-of-ramen-17952227/)
- [Women on bench](https://www.pexels.com/photo/two-smiling-women-sitting-on-wooden-bench-1267696/)
- [Avocado & egg toast](https://www.pexels.com/photo/pastry-and-boiled-egg-on-plate-566566/)


### Acknowledgments

- [Derek MCAuley](https://github.com/derekmcauley7), my Code Institute Mentor.
