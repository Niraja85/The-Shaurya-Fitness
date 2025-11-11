# The-Shaurya-Fitness
Project-portfolio-5

[Live Site](https://the-shaurya-fitness-509fd3f24de8.herokuapp.com/)

![Mockup_Image]()

## Table of Contents
- [The Shaurya Fitness](#the-shaurya-fitness)
  - [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [UX](#ux)
  - [Strategy](#strategy)
  - [Marketing Strategy](#marketing-strategy)
  - [Scope](#scope)
  - [Structure](#structure)
  - [Skeleton](#skeleton)
  - [Surface](#surface)
- [Agile](#agile)
  - [Epics](#epics)
  - [Sprints](#sprints)
- [Features](#features)
  - [Header](#header)
  - [Footer](#footer)
  - [Homepage](#homepage)
  - [Producers](#producers)
  - [Products / Store](#products--store)
  - [Product Details](#product-details)
  - [Bag / Cart](#bag--cart)
  - [Checkout](#checkout)
  - [Order Confirmation / history](#order-confirmation--history)
  - [User Profiles](#user-profiles)
  - [Product Management](#product-management)
  - [Error Pages](#error-pages)
- [Marketing Strategy Implementation](#marketing-strategy-implementation)
  - [Branding](#branding)
  - [SEO](#seo)
  - [Keywords](#keywords)
  - [Newsletter](#newsletter)
  - [Social media](#social-media)
- [Testing](#testing)
- [Technologies used](#technologies-used)
  - [Languages](#languages)
  - [Libraries / Frameworks](#libraries--frameworks)
- [Running Locally](#running-locally)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Deployment](#deployment)
  - [Prerequisites](#prerequisites-1)
  - [Deployment to Heroku](#deployment-to-heroku)
- [Future Development](#future-development)
- [Credits](#credits)
  - [Media](#media)
  - [Code](#code)
- [Acknowledgements](#acknowledgements)

# Introduction

Welcome to my ecommerce website "The Shaurya Fitnness' - an online store for Workout clothing and accessories exclusively for women!! It is a B2C e-commerce website for the final project of the Code Institute diploma in Software Development.

The site provides role based permissions for users to interact with a central dataset. It includes user authentication, email validation and full CRUD functionality for approved users for Products.

The payment system uses Stripe. Please note that this website is for educational purposes only and the payment gateway is not set up to accept real payments. Do not enter any personal credit/debit card details when using the site.

When testing the site, please use the following from Stripe's testing documentation:

- a Stripe test card number, such as 4242 4242 4242 4242.
- a future expiry date, such as 04/26.
- any three-digit CVC.

# UX

## Strategy

### The Problem
While researching for activewear market, I found out the increased demand of athleisure brands among women who want to look stylish and feel comfortable at the same time. At the same time fast fashion is a real problem in today's world, due to social media influencer trends, remote working and relaxed dress codes, increased awareness of wellness and fitness culture has heightened the demand.

### The Solution
Lets put the focus on designing an ecommerce website for activewear exclusively for women, which encompasses the use of recycled materials, hence reducing the carbon footprint and encouraging slow fashion with stylish workout wear that does not compromise on the performance, but adds on to the increasing deamnds of athleisure clothing.

### Target audience
Women who are passionate about their physical fitness and love to add style too in their workout wear wardrobe.

*Go back to the [top](#table-of-contents)*

---

## Marketing Strategy
The main goal of the company is to increase sales to add on to the increasing demands of fitness among women and encourage slow fashion at the same time. To increase sales, we need to raise awareness of the brand and allow the products to be available to a much larger number of people. This is where the website comes in.

Having a strong brand and a solid, trustworthy and easy to use website creates a good foundation for the company to build its online presence, massively increasing its reach in comparison to a handful of shop fronts across the country.

With the website as an asset and a newsletter email list as a starting point, we can then share the brand on social media or online advertising, continue to evolve the SEO, and build out additional features (such as a blog, educational resources and charity campaigns) to help increase traffic to the site. We could run social media competitions and email campaigns.

*Go back to the [top](#table-of-contents)*

----

## Scope

### User Expectations
1. As a user I expect the app to be responsive.
2. As a user I expect the app to be accessible.
3. As a user I expect my data to be secure.

### User Stories
4. As a user, I want to see an interesting homepage, So that I can learn about the store and the type of products it sells.
5. As a user, I want to subscribe to a newsletter, So that I can receive updates about the store.
6. As a user, I want to register my profile, So that I can save my personal information for future shopping.
7. As a user, I want to view the list of products available, So that I can see what the store has to offer.
8. As a user, I want to filter the products, So that I can narrow down my search.
9. As a user, I want to search for specific products, So that I can avoid clicking through pages.
10. As a user, I want to add products to my bag, So that I can save what I might purchase later.
11. As a user, I want to remove products from my bag, So that I can edit the order before checking out.
12. As a user, I want to edit the quantities of items in my bag, So that I can edit the order before checking out.
13. As a user, I want to go through a checkout process, So that I can review my bag and add my details to complete my purchase.
14. As a user, I want to provide card details, So that I can pay for the products in my cart.
15. As a user, I want to have my payment processed, So that I can complete my order.
16. As a user that's logged in, I want my details to be autofilled at checkout, So that I can make purchase quicker and easier.
17. As a user, I want to see feedback on my actions, So that I can get confirmation of the actions I've taken.

### User (Owner) Stories
18. As a superuser, I want to add products to the store, So that I can offer products to seel and add new products in the future.
19. As a superuser, I want to update products, So that I can keep them up to date.
20. As a superuser, I want to delete products, So that users won't buy unavailable products.

All the user stories were further divided into milestones divided across § 3 sprints based on priority with must-haves, should-haves and could haves that are seen on GitHub Issues section.

#### SPRINT 1
---

1. BASE SETUP (Milestone 1)
- Initial Setup
- Create Base.html
- Create Nav-bar
- Create Footer

2. AUTHENTICATION (Milestone 2)
- AllAuth Authentication
- Style AllAuth pages.

3. ABOUT Ss(Milestone 3)
-S Create Homepage.

#### SPRINT 2
---

4. NEWSLETTER (Milestone 4)
- Create a newsletter model adde to the footer.

5. CONTACT FORM (Milestone 5)
- Create a contact form

6. FAQ (Milestone 6)
- Create a FAQ page.

7. CLOTHING (Milestone 7)
- Create a clothing link for all fitness wear collection.
-  Add items to my bag
- Edit quantity of items in my bag.

8. ACCESSORIES (Milestone 8):
- Create a accessories link for all the accessories collection.
- Add items to my bag
- Edit quantity of items in my bag.

9. SORTING AND SEARCHING (Milestone 9)
- Sorting and searching the products.
- Filtering the products according to price and category.

10. SHOPPING BAG (milestone 10)
- Add sizes to clothing and accessories products.
- Remove and update products from the bag.

11. REGISTRATION AND USER ACCOUNT (Milestone 11)
-  Every user has a personalised profile to view orders and order history.

12. ADMIN AND STORE MANAGEMENT (Milestone 12)
- As a store owner, able to add, update and delete products from the store.

13. PURCHASING AND CHECKOUT (Milestone 13)
- As a user be able to add, remove, update, products in bag, go through a checkout, enter card details to make a payment, and complete my order after successful order placement.

14. DEPLOYMENT (Milestone 14)
- Setup White noise for static files.
- Deploy to Heroku.

#### SPRINT 3
---
15. STAND ALONE PAGES (Milestone 15)

- Create 400, 403, 404 and 500 error pages.

16. DOCUMENTATION (Milestone 16)
- Create FB page for the website
- SEO Implementation
- Write Readme and Testing.md


**DATABASE MODELS**

Thanks to DBeaver that helped me create the diagram of models.

![Database_Models]()

*Go back to the [top](#table-of-contents)*



















