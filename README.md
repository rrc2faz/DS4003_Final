# DS4003_Final - Rachel Cleal 

### Project Overview
Cinemaniac is a dynamic app designed to enrich your movie experience through the use of interactive graphs that allow you to dive into a film dataset and uncover trends, statistics, and insights into 10 top directors in the film industry. 

### Dashboard Building Process
Planning: I began my dashboard building process by finding a dataset of IMDb films I was interested in exploring on Kaggle. After cleaning the data and performing exploratory analysis, I opted to narrow the scope of my dataset to 10 top-grossing directors. From there, I created user personas to best understand who would be interested in using my app and what graphs would best align with their needs. Using these insights, I created a mock layout using Canva to get an idea of what my finished app would look like. From there, I began coding the dash app in VS Code using the packages listed below. 
	▪ Data: https://www.kaggle.com/datasets/elvinrustam/imdb-movies-dataset/data 
	▪ Packages Used: Dash, Plotly, Matplotlib, Bootstrap, Pandas, Seaborn
App Layout: After specifying a stylesheet and initializing the app, I coded the app layout to include each markdown, input component, and graphical elements. This provides the shell of the app and specifies where each element will be placed. To prevent the app from appearing cluttered, I also added several break lines to the layout to give each element its own space. 
Callbacks: Next, I ensured every function had its own callback operator. There are two callbacks within my app code to coincide with each function that updates the graphs within the app. These callbacks include the input (the slider and dropdown) and the outputs (each graph).  Since the last graph, a bar graph, interacts with a separate dropdown menu it required a separate callback. 
Functions: The functions ensure that each of my graphs update depending on user input into the dropdown and/or slider. Within section resides the code creating each graph. The functions accept the input values from these components, then run through the graphical elements I code to determine how to construct the graphs with the appropriate data. This section is also where a lot of the more intricate design work resides, such as changing the background color of the graphs to match the app theme and hiding the gridlines within the graphs. 
Deployment: The app is deployed using Render, which automatically builds and deploys my code when changes are pushed to the linked Git branch. Render provides the web service with a unique subdomain on onrender.com, which can be found below. 
	▪ Render Link: https://ds4003-final-iz98.onrender.com/

### User Experience (UX) Elements 
	▪ Definition: UX refers to the overall experience someone has when using a product or service and includes all aspects of the interaction, from the initial contact with the product or service to the final use and potential follow-up with the goal of creating a positive and meaningful experience for the user by considering their needs, preferences, and limitations
	▪ Research: Created user personas to best understand the needs and behaviors of potential users. This helped me create graphs that met user's needs and solved their problems.
	▪ Emotional Aspects: Aimed to design an app that evokes positive emotions in users through the use of aesthetics, including presenting a seamless experience with concise communication. 

### User Interface (UI) Elements 
	▪ Definitions: Refers to the visual and interactive aspects of a software application or website that allow users to interact with it and accomplish their goals
	▪ Layout: Arranged visual elements in a consistent layout throughout app
	▪ Typography: Used a consistent font throughout the app that was legible, readable, and appealing when displayed
	▪ Color Schemes: Used the Vapor theme to mimic dark-mode that many users prefer on apps and create an edgy atmosphere for the app
	▪ Navigational Components: Included a way to filter data within graphs through a dropdown for director and slider for release date range. Added a separate dropdown for the bar graph to improve graph readability. These each ensured that it was easy for users to find what they're looking for and move through the app
	▪ Graphical Elements: Included a bubble plot, treemap, heatmap, and bar chart to display multiple variables to provide the most information possible

 ### Principles of Design Elements
	▪ Balance: Evenly distributed graphs throughout app to create a balanced design that invokes a feeling of stability and harmony
	▪ Contrast: Used opposing elements, including a dark background and light text and graphical elements. This contrast creates visual interest in the design and highlights important elements to create focal points in the graphs
	▪ Emphasis: Used the technique of color and size to create focal areas in the app in the form of graphical elements
	▪ Proportion & Rhythm: Structured each graph the same size to provide a consistent flow and harmony within the app and help draw attention to key elements
	▪ Unity: Used a color theme to create the sense that all elements within the app are working together towards a common goal, providing a sense of completeness and harmony

### Conclusion
This project allowed me to utilize the design and technical skills taught throughout the semester into one strong, cohesive app. In this process, I gained great insight into the challenges involved in transforming a project from concept to finished product. My technical skills also improved, and I'm confident that I could repeat the process with another dataset based on potential user needs.
