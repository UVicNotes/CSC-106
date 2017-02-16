## Lecture 12 - February 1st, 2017

**Guest lecture 2**

#### SendWithUs

* Automated E-mail
* Realtime API 
* Send Transactional Emails
* Started in 2013, Matt and Brad
* YCombinator Startup Accelerator
* $2.5M -> US Investors
* Team of 17 People
    * Sales and Marketing in San Fran, California
    * Engineering and Product Development in Victoria, BC

**API Example:**

```bash
curl -X POST -u key_123 https://api.sendwithus.com/api/v1/send
    -d '{
    "email_id": "tem_12345",
    }'
```

**Template:**

```html
<td>
    Welcome to Awesome Co, {{first_name}}!
</td>
```

**Rendered Template:**

![Rendered Email](..References/email_Rendered.png)

#### Techincal Overview:

* Over 10M emails per day 
* <= 600 instances (on Heroku)
* Python, Coffeescript, Golang, CSS, HTML
* PostgreSQL, MongoDB, Redis


#### Backstory

* Brandon: VIU (Remax, Startup -> websites/products -> SendWithUs)
* John: UVIC (5Years -> Math (Failed) -> C's get degrees -> Co-Ops -> Startups vs Big Company -> Real Job -> Interview -> SendWithUs (Backend Dev))

#### What Makes Programming Awesome?

* Foundational Learning
    * University Co-Op
    * Computer Science 
        * Self-taught
        * Uvic
        * Bootcamps 
* Side Projects
    * Github
    * Simple - Complex
    * Are the new Resume 
* Open Source
    * Open your code to the world
    * Collaborate 
* Community Involvement
    * Victoria Tech Sector is Exploding
    * StartUpSlam and Battlesnake
    * Victoria Start Up Job Board
    * Ladies Learning Code
