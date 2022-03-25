## **Overview**
#### [GITHUB PAGES LINK]()
<!-- ![image](image file) -->

## proj description

The Spot

A full stack app that uses React Native and Django as a back end. Users will be able to create an account and upload pictures of their 'spots' (biking, skiing, hiking, camping, etc). When posting Users will be able to Name their Spot, Select State, It will auto fill the date. Post MVP will have interactions between users with comments and messages

## user stories

**Ronald** Ronny lives in florida. He loves the mountains and snow, but  because of his location its not really a reality. He loves Oregon and always wanted to go. Scrolling through the uploaded pictures lets him live out that fantasy


**Tammy** Tammy is from the PNW. Tammy loves to ski in the winter time, and bikes in the summer time. Typically Tammy will hop on the app on her lunch break to see if there are maybe any cool new spots that are posted that she doesnt recognize

## Day	Deliverable	Status
- [] Day 1	Figuring Out what Idea Im sticking with
- [] Day 1.5	Wireframes / Priority Matrix / Timeline
- [] Day 2	Backend
- [] Day 3	Learning React Native/Building out Front End
- [] Day 4	Learning to link front and back end (prolly still learning react native)
- [] Day 5  Actually linking front and back end
- [] Day 6  

# Project Description

Posts 
- SpotName: String
- Date: Date
- Location: String
- Description: String
- Images: Array?
- (V1.5)Likes: Number
- (V2)Comments: SubDoc
- (V2)Tags: Array

User
- AccountName: String
- Password: String




Comments (V2)
- Name: String
- Date: Date.now
- Comment: String
- Up/downvote: Number (probably toggle related to prevent multiple likes from one user)




## Inspiration:
- Insta
- Trailforks



## Wireframes
<!-- Upload images of wireframe to cloudinary and add the link here with a description of the specific wireframe. Do not include the actual image and have it render on the page. -->
- ![image]()
<!--
 -->
# MVP/PostMVP - 5min
## MVP
- Posts and Users
- API storing Images with the info corrosponding to the user that uploaded it
- Interactive client side allowing posts to be generated
- Users can delete only their own posts
- a basic feed displaying posts
- *v1.5* ability to search for posts based on state

## POST MVP
- Interactions with posts to add comments and likes
- Creating Seasons from the Dates generated so that users can sort by season

## REACT ARCHITECTURE
| Component | Description | 
| --------- | :---------: |  
| App       | This will render the react components | 
| Nav       | This will enable users to navigate sections of the site                | 
| create post | This will enable the user to create and store a post for others to see and interact with |
| post page | This will enable the user to interact with a specific post  |
| feed      | This will display the list of posts stored in the api |
| userposts | This will display all posts from the user |
| footer | This will display the trademark and lack of liability, scroll to top |
| header | This will display the logo and nav menu, stickied to top |


| **URL**     | **HTTP Verb** | **Action** | **Description**             |
| ----------- | ------------- | -------------- | ---------------------- |
| /    | GET           |   read         | view feed       |
| /post     | POST     |    create          | create a new post     |
| /comment  | POST          |    create            | create a new comment     |
| /post/:postId | GET           |    read            | view comments     |
| /post/:postId | PATCH           |    update            | update a post detail  |
| /post/:postId/comment/:commentId | PATCH           |    update            | update a comment  |
| /post/:postId/comment/:commentId | DELETE        |    destroy            | destroy a single comment |

| Component   | Priority | Estimated Time |	Actual Time    |
|-------------|----------|----------------|----------------|
|Schemas      |	H        |	1hr           |                |
|backend stucture  |	H        |	4hr           |                |
|backend crud/testing  |	H        |	4hr           |                |
|client crud  |	H        |	8hr           |                |
|client route |	H        |	2hr           |                |
|feed         |	H        |	2hr           |                |
|new post     |	H        |	2hr           |                |
|header/footer|	H        |	2hr           |                |
|style        |	M        |	6hr           |                |
|Total	      | H	     |  20hr	      |                |

## Additional Libraries
Use this section to list all supporting libraries and thier role in the project. -->
- React-Native
- Django
-https://www.youtube.com/watch?v=0-S5a0eXPoc&ab_channel=ProgrammingwithMosh

## Code Snippet
