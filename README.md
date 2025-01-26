# Speech to company event recommendation solution

## Description
The objective of this project is to provide an interface outputting a set of relevant venue/activity results when typing a description of the desired service.

## Table of Contents
- [Philosophy](#Philosophy)
- [Data Processing](#Dataprocessing)
- [Brief to text](#brieftotext)
- [Recommendation](#recommendation)
- [Respository](#Respository)

## Philosophy
The main phylosphy of the project is to try and approach the problem with a very standardized way. In the end the clients input is considered to be a set of requirements. This is ment to fasten any itterations on the service and also it prevents the code's complexity to increase with those itteration. For instance looking at a "number of participant" is no different than having a "budget", those are both numerical criterion.
For time constraint reasons, the project is not dealing with more complexe cases but the reasoning could be the same even for more textual criterion where the only difference would be that they would require a bit more data preparation to extract details from an activity description.

## Data Processing
The data procesing is quite limited for now. The only criterion considered are related to the desired city and to the number of participant. There were no null values regarding the capacity of venues. For consistency the cities were put to lower string. Some cities were not mentionned for some venues but dealing with those cases would have required some extra data preparation that was not affordable when working on the project and would have potentially been useless as those venues might not even be relevant in the first place.

Functions:

load_data

clean_data

## Brief to text
I did not benefit from a paid subscription to any LLM API so my first criterion was to find a free solution. I tried out the free version of the Hugging face API which was overwelmed with request most of the time which was not convenient when working with a time constraint. I ended up using a local solution with the transformers library which worked just fine for this exercice.

Functions:

## Recommendation
This project would be a very first mvp of the recommendation system. The idea is to approach the recommendation as a business rule system. You have requirements that are not negociatable and some that are but can be used as a way to order your recommendations by order of relevancy. In the end the clients input can be deaggregated in to a set of requirements. Then its just a matter of having this kind of requirement implemented. Its the objective of the requirements.csv file. You can specify which requirement value you want to extract from the speech of the user, which dimension it represents in your data base, how to compare the two and what level of importance this requirement should have for the recommendation system. 
This first iteration is more of an architectural approach and is not yet dealing with a huge amount of requirements. I avoided starting off with complexe alrogirthms right away as I don't have enough business context to know if those algorithm are relevants to begin with. Also starting with a standardized approach will ease the implementation of potential algorithm as they might as well just be treated as a "requirement" and be part of the already existing recommendation system. Currently the repo doesn't provid a monitoring system for the performance of a given requirement rule. This should be the most important next step as having a good way of monitoring the performance would allow to prioritise the most important requirements to implement as well as fixing the current ones. 

To monitor the system we could think of several KPI:
- proportion of clients request receiving an answer
- by labelling the results (either manually or by asking the client) we could keep track of the system's precision

As we devided the system into a set of criterion we might also follow each of them individually to spot potential weaknesses. In addition we could have some criterion working in a dry run state and utilising those performance dashboards to asses there relevancy before putting them in production.
- proportion of clients request triggering the criterion
- proportion of laballed results aligned with the criterion's label
- redundancy of the criterion compared to the overall system (mostly usefull for the dry run state)

Functions:

## Testing the code
To run the code you can start the streamlit app and type queries within the prompt.


