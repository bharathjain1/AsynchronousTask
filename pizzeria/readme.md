About Project : 
    Above project is a basic asynchronous task based project
    Pizzeria store allows user to order pizza and your pizza gets ready 
    by 5 mins, user can track the status of the order

To start the project
1. Install the requirements using requirements.txt file
2. Run docker compose file for different services such as mysql db, redis(message broker)
    $ docker-compose up -d
3. Run development server -- $ python managr.py runserver
4. Start celery worker server -- $ celery -A pizzeria worker -l info -P eventlet

Run the endpoints 
endpoint1(post request) booking an order: http://localhost:8000/orders/placeOrder/ 
                payload : [
                                {
                                    "userid": 18,
                                    "pizza_base": "thin-crust",
                                    "pizza_cheese": "MOZZARELLA",
                                    "pizza_toppings": "{'Roast pumpkin','chorizo pizzas', 'Silverbeet', 'mozzarella', 'broccolini'}"
                                }
                            ]

endpoint2(get request) tracking oder: http://localhost:8000/orders/Orderdetails/?order_id=13
