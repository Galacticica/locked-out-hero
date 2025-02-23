# Welcome To Lock Out Hero

## What Is Lock Out Hero?
Lock Out Hero is a static website created as part of the CCSC Hackathon.  We created this website as a 
way for students to regain access to buildings on our college campus, without contacting security.  In this repo, you will find instructions on how to use this demo, and will be able to easily follow through the code yourself.  Thank you for checking out Lo

## How To Use Our Demo
In the development stage, our program runs off of a uv environment. 

In the terminal, run the command ```uv run py manage.py runserver```
Then control click the url ```http://127.0.0.1:8000```

    Jimmy John is a male student living in the Ruth dorm. This means that if you log in during the hours of  10 AM - 12 AM Central time he can access all the dorms, but if he logs during the hours between 12 AM - 10 AM  Central time, only Ruth (his home dorm) will be available. 

### Demo Login Info
    Username:jimmy.john  
        This would be the standard username for the school website accounts. For us it's FirstName.LastName

    Password: freakyfastfood  
        This is the same password that is used for all school login accounts by default, or it can be set separately
    


Once logged in, select the building you want to gain access to.  
Once clicking the call for help button, it will show a screen, and at that point the door would unlock.  
It also logs the usage in our database.  
    
