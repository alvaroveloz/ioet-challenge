# ioet-challenge

## Analysis of solution
As can be seen below in the image, a line of input data, we can determine 3 classes initially, such as: User, Programming, Registration. Afterward, I declare the data input through the DataSource abstraction which is extended by FileSource. Finally to show the results Output class was created.
![Architecture](./src//images//model.png)

######  Directory Structure 

```
ioet-challenge
│   README.md
│   main.py    
│
└───classes
│   __init.py__
│   DataReader.py
│   Output.py
│   Register.py
│   Schedule.py
│   User.py
│
└───data
│   └───input
│   │   inputFile.txt
│   │
│   └───output
│       YYYYMMDD_HHMMSS.txt
│
└───src
│   └───images
│
└───tests
│   __init.py__
│   └───classes
│       __init.py__
│       test_schedule.py
│       test_user.py
│
└───utils
    __init.py__
    helpers.py
```

            

### Code execution


###### Before of all, clone the repository
> git clone git@github.com:alvaroveloz/ioet-challenge.git
###### Then go to directory ioet-challenge
> cd ioet-challenge

###### Then save the input file data inside of the directory 
> /ioet-challenge/data/input

###### You can run the code typing in your console 
> python3 main.py

You are going to receive this message in console
```
Enter the name of the file to export content: 
```
Type the name of the input file, then you can show the results of the table in console


###### Test User Class
> pytest tests/classes/test_user.py -v
###### Test Schedule Class
> pytest tests/classes/test_schedule.py -v

