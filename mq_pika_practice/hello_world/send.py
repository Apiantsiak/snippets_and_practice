import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
message = 'Hello World!'
channel.basic_publish(exchange='', routing_key='hello', body=f'{message}')

print(f" [x] Sent '{message}")

connection.close()
