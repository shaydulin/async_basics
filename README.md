### 1. Intro

This program is a simple synchronous web server.

- Run `1_intro/original.py`.
- In multiple terminals, run `nc 127.0.0.1 5000`.
- Observe: Type something in any terminal, and the server only responds in one terminal.

### 2. Event Loop

The program uses the `select()` function to monitor a list of files (sockets, in this case) that are ready for reading, writing, or have errors. When some are ready to be read, `select()` returns a list of them, and we can then read from those sockets.

- Run `2_event_loop/event_loop.py`.
- In multiple terminals, run `nc 127.0.0.1 5000`.
- Observe: Type something in any terminal, and the server responds instantly.

### 3. Async with Callbacks

The program uses the higher-level `selectors` interface to monitor files. A server socket is created and registered. When it is ready for reading, a client socket is created and registered. The `event_loop()` iterates over the files and calls the appropriate functions.

- Run `3_async_with_callbacks/callbacks.py`.
- In multiple terminals, run `nc 127.0.0.1 5000`.
- Observe: Type something in any terminal, and the server responds instantly.

### 4. Async with Generators

Using generators allows the function to yield control back to the event loop. Both `server()` and `client()` are generator functions. The `yield` keyword is used to yield a socket, which will then be added to the appropriate list of sockets (`TO_READ` or `TO_WRITE`). These lists are passed to the `select()` function, which returns sockets that are ready for reading or writing.

- Run `4_generators/generators.py`.
- In multiple terminals, run `nc 127.0.0.1 5000`.
- Observe: Type something in any terminal, and the server responds instantly.
