# qaiotdb-challenge2022


## Welcome to the IoTBig Data QA Challenge

Follow the steps to fulfill the challenge:

### Clone this repo:
  
    git@github.com:XavierVal/qaiotdb-challenge2022.git


### Read carefully this file to understand the purpose correctly
    
All task resolutions must be uploaded to a Git repository (Github, Gitlab, Bitbucket, etc.). Public or private. 
Add a readme file describing the configuration environment and the basics of the test.
This tasks should take less than three hours of work, you can take as much time as you need.
Intelligent prioritisation is another goal for these tasks.


### Our System under Test (SuT)
We are going to use an open REST/API based on the famous TV show Rick & Morty: https://rickandmortyapi.com/ 
  
        https://rickandmortyapi.com/api

With three main resources 
    
    {"characters":"https://rickandmortyapi.com/api/character",
    "locations":"https://rickandmortyapi.com/api/location",
    "episodes":"https://rickandmortyapi.com/api/episode"}

### Task 0, Implement an API consumer function, *Character info extractor*
    
  Implement a piece of code that allows users to interact with the API in a simple way.
  The functionality requested is given a "Character Name" it returns info about the character, location and the "episode/s" where is present   

Example: 

    >>> Function input: 
      Character: "Pickle Rick"

    <<< Response should contain the following info return:
      - Character info  ->  "species": "unknown", "type": "Pickle"
      - Location/s info ->  "name": "Earth (Replacement Dimension)", "type": "Planet", "dimension": "Replacement Dimension","population" 230
      - Episode/s info  ->  "episode_name": "Pickle Rick", "episode_id": "S03E03", "characters_count": 15

Feel free to select the output format that fits better the outputs under your understanding.

###  Task 1, Designing a test plan

  Write a test plan for the API Rest data. Test cases must be self-descriptive.
  If necessary, note down any descriptions or clarifications.
  The organisation and format of the test plan are at your discretion. Be careful not to overemphasise the importance of prioritising tests!
  The prioritisation of tests is important. 

###  Task 2, Integration testing (you own code)

  Develop simple test cases using any tool/framework of your choice. 
  The objective is to test simple function and its integration with the endpoints, i.e. ensure the basic correctness of the REST API.

###  Task 3, end-to-end testing

  Design and develop some end-to-end tests for the REST API of the API; you can use any automation framework to do this.
  Any automation framework can be used for this task.

Remember. It is not necessary to test everything, there are always new tests to design and develop.
There are always new tests to design and develop, so we recommend that you work on the design of the initial test plan during the development of Tasks 2 and 3.
Task 2 and Task 3. Once completed, you can expand them as you see fit: new data, new tests, new
new data, new tests, non-functional specifications, security, CICD, framework improvements, etc.
framework improvements, etc. ...... There is a lot to do.
I hope the code is clear and straightforward! Good luck.

