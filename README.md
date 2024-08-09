# async_basics

### Intro.

- run 1_intro/original.py
- run nc 127.0.0.1 5000 in second terminal
- run nc 127.0.0.1 5000 in third terminal
- see: write something in second and third terminals, server responds in second but no response in third terminal

### Event loop.

Program 2_event_loop/event_loop.py uses select() function to monitor list of files (sockets in this case) that are ready to read (but also to write and list of files with errors).

When some is readable select() return list of them. And we can read that sockets.

- run 2_event_loop/event_loop.py
- run nc 127.0.0.1 5000 in as many terminals as You want
- see: write something in any terminal, server responds instantly