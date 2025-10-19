This file contains a description of the domain models we will handle in our application.


### Item
Represent a meal, drink or any piece of food that could be available at the restaurant.
Contains:
- a Name (str)
- a Price (int)

### User
Represent a person or entity that could start or participate in an event at this restaurant.

Contains:
- a Name (str) 
- an email address

### Event
Represent an event in wish multiple user will participate, with a list of Items available.

Contains:
- Multiple references to the Items that are available for this specific event
- Multiple references to the Users that can participate to this event
- A reference to the specific user that owns this event