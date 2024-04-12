from tmp.creds import RESPONSE_QUEUE_URL, REQUEST_QUEUE_URL, AWS_REGION_NAME
import boto3

QUEUE_USED = REQUEST_QUEUE_URL


class QueueUtil:
    def __init__(self, region_name=AWS_REGION_NAME):
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

    def set_queue_in_use(self):
        # Set QUEUE_USED based on user choice of available queues
        print("Listing all available queues with indexes:")
        response = self.sqs_client.list_queues()
        queue_urls = response.get("QueueUrls", [])

        # Display each queue with an index
        for index, url in enumerate(queue_urls):
            print(f"{index}. {url}")

        # Get the user's choice of queue
        choice = input("Enter the index of the queue you want to set as QUEUE_USED: ")

        try:
            choice_index = int(choice)
            if 0 <= choice_index < len(queue_urls):
                global QUEUE_USED
                QUEUE_USED = queue_urls[choice_index]
                print(f"QUEUE_USED has been set to: {QUEUE_USED}")
            else:
                print("Invalid index. Please choose a valid queue index.")
        except ValueError:
            print("Invalid input. Please enter a valid integer index.")


# Example usage
if __name__ == "__main__":
    # Instantiate the QueueUtil class
    queue_manager = QueueUtil(region_name=AWS_REGION_NAME)

    while True:
        # Print menu options
        print("\nChoose an option:")
        print("1. List all queues")
        print("2. Print all messages from the specified queue")
        print("3. Clear the specified queue")
        print("4. Set the queue in use")
        print("5. Exit")

        # Get user choice
        choice = input("Enter your choice (1-5): ")

        try:
            choice = int(choice)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
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
            # Set the queue in use
            queue_manager.set_queue_in_use()
        elif choice == 5:
            # Exit the menu
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
