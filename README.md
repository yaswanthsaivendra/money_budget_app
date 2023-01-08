# money_budget_tracking_app

Demo of the application : http://yaswanthsaivendra.me/money_budget_tracking_app/

## How to run the application : 

1. Clone the repo
	git clone https://github.com/yaswanthsaivendra/money_budget_app
2. Firstly start by running the backend : 
   1. Create virtual environment and activate it :
   
		virtualenv env

		source ./env/bin/activate 	(for linux)

		venv/Scripts/activate 		(for windows)

   2. Install requirements : 
   
		pip install -r requirements.txt

   3. Make migrations and runserver : 
   
		python manage.py makemigrations
		python manage.py migrate
		python manage.py runserver

Now our backend is up and running, Time to run the react app : 

1. Change the directory to client : 
   
	cd client/

2. Install the dependencies and run the server : 
   
	npm install
	npm start

## How to use the application : 

1. Start by creating a user, then after reaching the dashboard you can add income and expense along with their categories. 
2. Then go to the friends page and start by adding the friends to make any transactions or splits. 
<br>
Note : Here in our app, we are having 2 main things - splits and transactions.

	Splits - splits are what you called as transactions in our problem statement.
	
	Transactions - these are normal money transfers in which money can be transferred from one person to another person.

3. Once u added some friends, You can start by adding splits, deleting and updating them in the splits page.
4. You can clear the splits (or) pay the transactions from the split single page.
5. You can also make normal transactions from the dashboard.
6. Your incomes, expenses and budget will be kept track of in Dashboard.
7. All our pending debts and credits will be shown in the Pending page.
