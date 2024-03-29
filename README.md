# **Tea People**
[View a live version of Tea People here](https://chachatea.herokuapp.com/)
This is the main website for *Tea People*. An eccommerce site selling tea and tea tasting in Cork. Tea People will introduce you to the wonderful world of tea. From green tea to Bubble tea. Tea People hopes to promote the health benefits of tea and to help those who wish to move away from traditional black tea and experiment tea from many different countries. 
![Tea People on mobile, ipad, ipad pro and desk top.](/static/testing/teapeople_multi.png) "Tea People on multiple displays"

## Table of Contents
### [User Experience](#user-experience-(ux))
### [Project Goals](#project-goals)
#### [User Stories](#user-stories)
* [First Time Visitor Goals](#first-time-visitor-goals)
* [Returning Visitor Goals](#returning-visitor-goals)
* [Frequent Visitor Goals](#frequent-visitor-goals)




### [Design](#design)

* [Color Scheme](#color-scheme)
* [Typography](#typography)
* [Imagery](#imagery)
* [Features](#features)
* [Defensive Design](#Defensive_Design)
* [Wireframes](#wireframes)
### [Technologies Used](#technologies-used)
* [Languages Used](#languages-used)
* [Frameworks  Libraries and Programs Used](#frameworks-libraries-and-programs-used)
### [Deployment](#delpoyment)
* [GitHub](#github)
* [Cloning to Local Device](#cloning-of-repository-to-a-local-device)
* [Setting up a google maps javascript API](#Setting-up-a-google-maps-javascript-API)

### [Testing](#testing)
### [User Stories] (#)
[Photo story for first time user](#photo-story-for-first-time-user)
[Bugs](#bugs)
- [Gallery](#gallery)
- [Navbar](#navbar)
- [form](#form)
- [Javascript for Maps](#javascript-for-maps)
- [Javascript for mail](#javascript-for-mail)
### [Acknowledgements](#acknowledgements)
* [Media](#media)
* [Individuals](#individuals)


## User Experience (UX)

### Project Goals 

 * An E-commerce website that allows customers to order tea for delivery online. Customers may also log in to write reviews. A site that is vibrant and attractive. It engages the user. it is is easy to navigate and allows a smooth sales process. 
 
 * Site will use HTML, CSS, jQuery, Python, Stripe and Django.

 * Website will provide Users the chance to login, create and edit website. 

 * A user friendly website.

 

#### First Time Visitor Goals
 
 1. A first time user will be able to visit the site on any device. 
 
 2. They will be able to learn about the different types of tea.

 3. They will be able to easily see the products and click for more information. 

 4. They can also sort through the products for their preferences. 

 5. The main navbar will allow to filter by price, category, tea tasting and blogs.

 6. The user will also be able to add tea to shopping basket and remove. 

 7. They can register an account to save their shopping history and delivery  details. 

 8. They can purchase a product with ease using STRIPE.
 
 

 #### Returning Visitor Goals

 1. The user will be able to check passed orders. 
 2. They will be able to log in and leave a review of their order or product. 
 3. They check for new products. 
 4. They can check for blog updates. 


 #### Frequent Visitor Goals.

 1. Check the blog.

 2. Update passwords to log in if forgotten. 

 3. Change and update address if different.

 4. Comment on orders and makee further orders. 

 #### Admin User Goals

 1. The admin will add, edit and delete products. 
 2. The admin will maintain stripe functionality. 
 3. The admin will be  able to add, edit and delete blog posts. 
 4. The admin will be able to delete and remove any user reviews in comments.
 5. The admin will be able to see and manage current users. 
 6. The admin will be able to see and manage current orders.


# Design 
  ## Color Scheme  
  * Three main colors where chosen. Black backgrouund on landing page and White background inproduct and main blog post. The colors are also black, white and bright pink rgb(241, 132, 227). These colors are attractive and complement the main hero neon sign picture. This is with thee ideea of making tea cool and moving it from your grandmother's teapot to the variety the exists today. 
  
  * buttons are black, white and pink but also follow Stripe and Allauth styling. 
  * icons invert colors when hovered over.

 ## Typography 
    
  * Font used is Permanent Marker and Cursive for logo and Lato for the main body.  Permanent Marker is a nod to. thee Neon sign on the landing page.

 ## Imagery
  * Images used were from Unsplash. 
  
## Features
* Responsive on all devices. Allows users to shop for tea online.  Allowing Icons that link to further social media updates.

## Defensive Design

* The user must log in or register shop and to leave a review of the tea.

* Stripe is used for all payments and log in funtionality. 

* You can only add, edit and delete your own review. 

* The passsword must contain between 5-20 characters. 

* You can only log in with one email address. 

* Image Url must contain http:// or https://.


## Database Schema 

![successful validation confirmation](static/testing/schema.png) "Sample of Schema for database."


## Wireframes

* Wireframe for the whole project. [Wireframes](/static/testing/teapeoeple.pdf)


# Technologies Used 
## Languages Used 
* HTML
* CSS
* Jquery
* Python

## Frameworks Libraries and Programs Used 
1. [Boostrap](https://getbootstrap.com/)
  
    Bootstrap

2. [Heroku](https://dashboard.heroku.com/apps)

    Used to deploy app. 

3. [AWS](https://aws.amazon.com/)

    Amazon Wed Services  

4. [Google Fonts](https://fonts.google.com/specimen/Permanent+Marker)

    Permanent markere font used.

5. [Fontawesome](https://fontawesome.com/)
    Fontawesome was used for to get icons for utensils and aa cocktail on the feast page. 
6. [Gitpod](https://gitpod.io/workspaces/)
    Used gitpod to work on my repositories. 
7. [Github](https://github.com/MichelleCoffey/A_Moveable_Feast_Shanghai/tree/1a91746d21707106faef91c699500aff9414e097)
     GitHub is hosting my repositories. 
8. [JQuery](https://jquery.com/)
    * jQuery

9. [Balsamiq](https://balsamiq.com/)
    * Balsamiq was used to design and organise my WireFrames. 
10. [TinyPNG](https://tinypng.com/)
     * Tinypng for fomatting images, so they loaded faster.
11. [Unsplash](https://unsplash.com/)
    * Upsplash was used to access some stock images to add to the site and in particular the hero image and background image. 
12. [Miniwebtool](https://miniwebtool.com/django-secret-key-generator/)

    * Django key generator. 

13. [Stripe](https://stripe.com/en-gb-us)

    * Stripe for handling purchases.

14. [PostgreSQL](https://www.postgresql.org)

    PostgreSQL for the database.

15. [RandomKeyGen](https://randomkeygen.com/)


## Deployment 
### Github

### Requirements 
  1. Python3 
  2. Github account
  3. Django
  4. Summernote
  5. heroku account



#### The repository is hosted on GitHub but deployed on Heroku
To make a local clone on Github, follow the following steps.

1. Log in to GitHub and go to the repository.
2. Click on the green button with the text “Code”.
3. Click on “Open with GitHub Desktop” and follow the prompts in the GitHub Desktop Application for instructions.     
4. For further options and documentation please click [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop).

   
          
    #### Heroku Deployment


    This project was deployed using Heroku. Heroku is a PAAS (platform as a service) that enables developer to build, run and operate applications entirely in the cloud. Heroku integrates with GitHub to make it easy to deploy code living on GitHub to apps running on Heroku.

    1. In the terminal you must first need to create two files.
     **pip3 freeze -- local > requirements.txt**
      Followed by 
     **echo web: python app.py > Procfile**
      These are needed for Heroku. 
    2. Sign in or create a Heroku account. 
        * Click 'New' on the dashboard and select 'Create new app'.
        * Provide a unique app name including dashes, select your region, and   click  **'Create App'**.

    3. Go to **delpoy** tab on the dashboard.
       * For the **deployment method** click **Github**
       * Provide your repository name and click **Search**, once it finds your repository, click **Connect**.
       * Click on **Settings** and then the **Reveal Config Vars** to provide your **environment variables** from your **env.py** file to **Heroku**:
       
       Heroku Config Vars for the whole project. [Heroku Config Vars](/static/testing/heroku_config.png)
    


    4. Return to your git terminal and Push **requirements.txt** and **Profile**.
        $ git add requirements.txt
        $ git commit -m "Add requirements.txt file."
        $ git add Procfile 
        $ git commit -m "Add procfile."
        $ git push
    5.  Return to **Heroku** and click the **deploy** tab. 
        Then click on **Enable Automatic Deployment** followed by **Deploy Branch (main)**
        This will take less than a minute. Once your receive the success note. Click **view** to see your live site. 
    

                            
## Testing 

### Photo story for first time user

### User Stories Testing 

#### First Time User 


 ![Tea People homepage on mobile, ipad, ipad pro and desk top.](/static/testing/teapeople_multi.png) "Tea People on multiple displays."

 * User arrives at site and is guided to register. They must register name and password. They are prompted to add letter and not leave blank. 

 ![Tea People Sign Up.](/static/testing/tea_sign_up.png) "Tea People register page."

 * After registering  for the first time the user is prompted to confirm their email before they can log in.

  ![Verify log in .](/static/testing/tea_verify.png) "Family Recipes profile page."

  * User must then log in with their confirmed log in and password.

  ![log in.](/static/testing/tea_login.png) "Tea login page."

  * User then logs into their account for the first time.

 ![Products Page.](/static/testing/tea_products.png) "Tea Products page."


 * User will scroll through products until they find what they want.

  ![Product Detail Page.](/static/testing/tea_products.png) "Product detail page."

  The user can then look at a description of the full page and decide if they wish to add it to their cart. 

  ![Add Tea to Cart.](/static/testing/tea_addteatocart.png) "Add Tea to Cart."

  * After the shopper has added to the cart, they can then proceed to the checkout.

  ![Tea Checkout.](/static/testing/tea_subtotal.png) "Tea Checkout"

  * The shopper then checksout using stripe. 

  * In this case we are fake shopping so used the stripe assigned card to verify a sale.

  * 4242 4242 4242 4242 Stripe Testing card.

  ![Tea Blogs.](/static/testing/tea_blogs.png) "Tea Blogs"

  * The user can also look at the Blogs landing page to check out the blogs available on the site. 

  ![Tea Blog Details.](/static/testing/tea_blogdetails.png) "Tea Blog Details"

  * Full blog available to read. 

  ![Tea Product Reviews.](/static/testing/tea_reviewform.png) "Tea Review"

  ![Pink Tea Product Review.](/static/testing/tea_reviewform.png) "Tea Review"
 
 * User is invited to leave a review of the tea if logged in. They can also edit or remove review. Reviews are available on the product page if not signed in. 

 ![Tea People Sign Out](/static/testing/tea_signout_success.png) "Signout"
 ![Tea People Sign Out](/static/testing/tea_signout_success.png) "Signout Success"

 * User can then log out when leaving the site.
 


## Code Testing


W3C CSS Validator Services was used to validate CSS.

![successful validation confirmation](/static/testing/cssval.png) "CSS Validation."
 * This was successful.

 ![successful validation confirmation](/static/testing/pep8.png) "Pep8 Python testing."
 * This was successful but there was white space on blank like that would not change.



![successful validation confirmation](/static/testing/tea_htmlval.png) "Home Page HTML success."


### Bugs
#### Summernote

1. When adding the blog I ran into an issue with the color of the font because summernote overrides the font color and my page was black. I fixed this my changing the font color in admin. Also Igor at Code institute helped with code to override this in the blogs page.

#### Images and form
* After setting up AWS I still issues with some images not loading correctly or too slowly.. 

 #### Models 
 * When I initially set up the blog in models I started having a major issue with all my migrations. Thanks to Igor in Tutor support I was able to remove it all migrations and delete the database and then add it all again.. 



## Acknowledgements and Credits
### Media
* Code Institute Tutorials for providing a jumping off block. 
 * Slack for being a great source of help with either googling or when other students have provided suggestions to help improve your work. 
 * Code Institute Tutorials. 

 ### Individuals, Credits and Code
 * My Mentor, Precious Ijege. 
 * Tutors at Code Institute are great guiding hand.   They do not give you the answer but ask the right questions to lead you down the correct path. It also helps build confidence. 
 * Anne Greaves and Code Institute for a comprehensive guide to writing README.md. The template was taken from the Code Institute Guide to writing README and how to write Markdown.

 * I looked at Perkulater, Fashionista and Rebels Beans, all on peer view in Slack, to help figure out both blogs and Product reviews. 

 * [Codementor](https://www.codementor.io/@jadianes/get-started-with-django-building-recommendation-review-app-du107yb1a)

 * A guide to using reviews in wine products. This heelped to formulate my models for product reviews. 

  [Django Central](https://djangocentral.com/building-a-blog-application-with-django/)

 * A guide to writing a blog and using paginator. 

 * Code Institute video on using Summernote in blogs.

 * Boutique Ado for the stripe functionailty and all other workings in the site.

 * Alex Harvey, a guide to writing a table of contents in gitpod. 



  

 

  

 

 


 





 

 
