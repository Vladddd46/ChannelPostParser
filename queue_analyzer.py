from tmp.creds import RESPONSE_QUEUE_URL, REQUEST_QUEUE_URL
import boto3

QUEUE_USED = RESPONSE_QUEUE_URL


class QueueUtil:
    def __init__(self, region_name="us-east-1"):
        # Initialize the SQS client with the desired region
        self.sqs_client = boto3.client("sqs", region_name=region_name)

    def print_all_queues(self):
        # List all queues and print their URLs
        print("Listing all queues:")
        response = self.sqs_client.list_queues()
        queue_urls = response.get("QueueUrls", [])
        for url in queue_urls:
            print(url)

    def print_all_messages_from_queue(self, queue_url):
        # Print all messages from a specific queue
        print(f"Printing all messages from queue: {queue_url}")

        # Define parameters for receiving messages
        receive_params = {
            "QueueUrl": queue_url,
            "MaxNumberOfMessages": 10,  # Maximum number of messages to receive per request
            "WaitTimeSeconds": 5,  # Wait time in seconds for long polling
        }

        while True:
            # Receive messages from the queue
            response = self.sqs_client.receive_message(**receive_params)

            # Get the list of messages from the response
            messages = response.get("Messages", [])

            # If there are no messages, break out of the loop
            if not messages:
                break

            # Process each message
            for message in messages:
                # Print the message body
                print(f"Message Body: {message['Body']}")

                # After processing the message, delete it from the queue
                receipt_handle = message["ReceiptHandle"]
                self.sqs_client.delete_message(
                    QueueUrl=queue_url, ReceiptHandle=receipt_handle
                )

        print("Finished printing all messages from the queue.")

    def clear_queue(self, queue_url):
        # Clear a specific queue by continuously receiving and deleting messages
        print(f"Clearing queue: {queue_url}")

        # Define parameters for receiving messages
        receive_params = {
            "QueueUrl": queue_url,
            "MaxNumberOfMessages": 10,  # Maximum number of messages to receive per request
            "WaitTimeSeconds": 5,  # Wait time in seconds for long polling
        }

        while True:
            # Receive messages from the queue
            response = self.sqs_client.receive_message(**receive_params)

            # Get the list of messages from the response
            messages = response.get("Messages", [])

            # If there are no messages, break out of the loop
            if not messages:
                break

            # Process each message
            for message in messages:
                # Delete the message from the queue
                receipt_handle = message["ReceiptHandle"]
                self.sqs_client.delete_message(
                    QueueUrl=queue_url, ReceiptHandle=receipt_handle
                )

        print("Finished clearing the queue.")


# Example usage
if __name__ == "__main__":
    # Instantiate the Queue class
    queue_manager = QueueUtil(region_name="us-east-1")

    # Define the queue URL
    queue_url = "https://sqs.us-east-1.amazonaws.com/531190140983/main_test"

    while True:
        # Print menu options
        print("\nChoose an option:")
        print("1. List all queues")
        print("2. Print all messages from the specified queue")
        print("3. Clear the specified queue")
        print("4. Exit")

        # Get user choice
        choice = input("Enter your choice (1-4): ")

        try:
            choice = int(choice)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            # List all queues
            queue_manager.print_all_queues()
        elif choice == 2:
            # Print all messages from the specified queue
            queue_manager.print_all_messages_from_queue(QUEUE_USED)
        elif choice == 3:
            # Clear the specified queue
            queue_manager.clear_queue(QUEUE_USED)
        elif choice == 4:
            # Exit the menu
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
