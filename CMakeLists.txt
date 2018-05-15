cmake_minimum_required(VERSION 3.10)
project(SimpleMQ C)

set(CMAKE_C_STANDARD 11)

add_executable(SimpleMQ main.c queue/queue.c server/server.c server/server.h message/message.c message/message.h)