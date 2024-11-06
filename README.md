# Banana_Bytes by Jobless_Monkeys
# Roster:
**Top Banana (Fullstack/Project Manager)**: Aidan Wong 

**Code Chimp (Backend/Python):** Abidur Rahman

**Data Ape (Backend/Database):** Brian Liu

**Pixel Primate (Frontend):** Leon Huang

# Project Description:

"Banana_Bytes" is a collaborative storytelling website where registered users can create stories and contribute to existing ones. Users can start a story by providing a title and adding content of any length on a "create" page. When contributing to a story on the "contribute" page, users can only see the most recent update by another user. After submitting their contribution, users are restricted from adding to that story again, but can now read the full story on a "view" page. Each user will have a personalized dashboard where they can view all the stories they have contributed to. In addition, there is a "collection" page where users can see all existing story titles, and filter based on contribution status, modification date, and more.

# Install Guide

**Prerequisites**

Ensure that **Git** and **Python** are installed on your machine. It is recommended that you use a virtual machine when running this project to avoid any possible conflicts. For help, refer to the following documentation:
   1. Installing Git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git 
   2. Installing Python: https://www.python.org/downloads/ 

   3. (Optional) Setting up Git with SSH (Ms. Novillo's APCSA Guide): https://novillo-cs.github.io/apcsa/tools/ 
         

**Cloning the Project**
1. Create Python virtual environment:

```
$ python3 -m PATH/TO/venv_name
```

2. Activate virtual environment 

   - Linux: `$ . PATH/TO/venv_name/bin/activate`
   - Windows: `$ . .\PATH\TO\venv_name\Scripts\activate`
   - macOS: `$ source PATH/TO/venv_name/bin/activate`

   *Notes*

   - If successful, command line will display name of virtual environment: `(venv_name) $ `

   - To close a virtual environment, simply type `$ deactivate` in the terminal


3. In terminal, clone the repository to your local machine: 

HTTPS METHOD (Recommended)

```
$ git clone https://github.com/awong50/Jobless_Monkeys__aidanw26_abidurr6_brianl237_leonh15.git        
```

SSH METHOD (Requires SSH Key to be set up):

```
$ git clone git@github.com:awong50/Jobless_Monkeys__aidanw26_abidurr6_brianl237_leonh15.git
```

4. Navigate to project directory

```
$ cd PATH/TO/Jobless_Monkeys__aidanw26_abidurr6_brianl237_leonh15/
```

5. Install dependencies

```
$ pip install -r requirements.txt
```
        
# Launch Codes

1. Navigate to project directory:

```
$ cd PATH/TO/Jobless_Monkeys__aidanw26_abidurr6_brianl237_leonh15/
```
 
2. Navigate to 'app' directory

```
 $ cd app/
```

3. Run App

```
 $ python3 __init__.py
```
4. Open the link that appears in the terminal to be brought to the website
    - You can visit the link via several methods:
        - Control + Clicking on the link
        - Typing/Pasting http://127.0.0.1:5000 in any browser
    - To close the app, press control + C when in the terminal

```    
* Running on http://127.0.0.1:5000
``` 
