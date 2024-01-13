#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <mqueue.h>

#define UP_QUEUE_NAME "/up_queue"
#define DOWN_QUEUE_NAME "/down_queue"
#define MAX_MESSAGE_SIZE 256

int main() {
    mqd_t up_queue, down_queue;
    struct mq_attr attr;
    char message[MAX_MESSAGE_SIZE];

    // Open UP queue
    up_queue = mq_open(UP_QUEUE_NAME, O_RDONLY);
    if (up_queue == (mqd_t)-1) {
        perror("mq_open");
        exit(EXIT_FAILURE);
    }

    // Open DOWN queue
    down_queue = mq_open(DOWN_QUEUE_NAME, O_WRONLY);
    if (down_queue == (mqd_t)-1) {
        perror("mq_open");
        mq_close(up_queue);
        exit(EXIT_FAILURE);
    }

    while (1) {
        // Receive message from client via UP queue
        mq_receive(up_queue, message, MAX_MESSAGE_SIZE, NULL);
        printf("Received message from client: %s\n", message);

        // Convert message to upper case
        int len = strlen(message);
        for (int i = 0; i < len; ++i) {
            if (islower(message[i])) {
                message[i] = toupper(message[i]);
            } else if (isupper(message[i])) {
                message[i] = tolower(message[i]);
            }
        }

        // Send processed message back to client via DOWN queue
        mq_send(down_queue, message, strlen(message) + 1, 0);

        if (strcmp(message, "exit") == 0) {
            break;
        }
    }

    // Clean up
    mq_close(up_queue);
    mq_close(down_queue);
    mq_unlink(UP_QUEUE_NAME);
    mq_unlink(DOWN_QUEUE_NAME);

    return 0;
}
