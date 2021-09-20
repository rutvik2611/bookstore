# bookstore
-Coding Challenge

I Will be working on Documentation Soon
 




Fictional book store.
Book store API written in Django rest framework

Installation

Clone this repository and cd bookstore
	https://github.com/rutvik2611/bookstore.git

Create venv
py -m venv libraryenv


After activation the env

cd bookstore


Install the dependencies needed to run the app:
    pip install -r requirements.txt

Models: 
1. User 
2. Books 
3. Library 
4. Transaction

Running the migrations (run the commands in order)

python manage.py makemigrations
python manage.py migrate

Start the server
	python manage.py runserver 


You can now access the file api service on your browser by using
1)	List of Users   
 	
	http://localhost:8000/users/


2)	Each User

	
	http://localhost:8000/users/{user_id}

3)	List of Transactions

	
	http://localhost:8000/transactions/

4)	Transactions Details

	
	http://localhost:8000/transactions/{transactions_id}

 
5)	List of books title, author and isbn 

	
	http://localhost:8000/books/


6)	Book details title, author and isbn


	http://localhost:8000/books/{book_id}


7)	Users rented books past and current (order by due date)


	http://localhost:8000/users/{user_id}/books/



8)	List of books in a library and their start (if they are rented or not at the moment)


	http://localhost:8000/library/{library_id}/books/

   admin/
api/ users/
api/ users/<int:pk>/
api/ books/
api/ books/<int:pk>/
api/ transactions/
api/ transactions/<int:pk>/
api/ library/
api/ library/<int:pk>/
api/ library/<int:library_id>/books/
api/ users/<int:user_id>/books/






