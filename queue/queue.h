//
// Created by villar on 5/15/18.
//

#ifndef SIMPLEMQ_QUEUE_H
#define SIMPLEMQ_QUEUE_H

typedef struct queue {
    int position;
} Queue;

/** Define the Queue functions */

int create_queue(const char * name);

#endif //SIMPLEMQ_QUEUE_H
