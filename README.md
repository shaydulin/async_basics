Source - [Асинхронность в Python](https://www.youtube.com/playlist?list=PLlWXhlUMyooawilqK4lPXRvxtbYiw34S8)

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

### 5. Coroutines

#### `5_coroutines/coroutines.py`

Using `yield` allows not only yielding values from the generator but also sending values to the generator. A generator that utilizes this capability is called a `coroutine`.

- Run `5_coroutines/coroutines.py` in interactive mode.
- Use `getgeneratorstate` to inspect `gen_`. Initially, its state is `GEN_CREATED`. To initialize it, use `gen_.send(None)` or `next(gen_)`. The coroutine's state will now be `GEN_SUSPENDED`.
- Type, for example, `gen_.send("example")`. You will see `Gen received: example`, indicating that the coroutine has received the value `"example"`.
- The coroutine's state is now `GEN_CLOSED` as there is nothing left to yield.
- You can also throw exceptions in a coroutine using the `throw` method.

- The `coroutine` decorator is used to avoid extra work and initialize the coroutine.
- `avg` is a more complex coroutine that calculates the average value of the received integer numbers online. Send numbers one by one and get the average value in response.

#### `5_coroutines/delegation.py`

It is possible to place a coroutine inside another coroutine. `yield from` is used to yield values from the inner coroutine (or from any iterable).

- Run `5_coroutines/delegation.py` in interactive mode.
- Send messages to `g`, which will forward them to `sg`.
- `yield from` also propagates exceptions to the inner coroutine if an exception is thrown to the outer one.
- Generators can not only yield values but also return values. `yield from` returns this value as well.

### 6. asyncio, async/await

#### `6_asyncio_async_await/asyncio_async_await.py`

This basic program demonstrates asynchronous printing using the `async/await` syntax with two coroutines.

- Run `6_asyncio_async_await/asyncio_async_await.py`.
- Two functions run asynchronously: one prints numbers and the other prints elapsed time.

#### `6_asyncio_async_await/async_image_downloader.py`

This program compares the speed of synchronous and asynchronous image downloading from the Internet. Since the request-response phase is I/O-bound, the difference in performance is significant.

- You need the `aiohttp` and `requests` libraries. Install them using `pip install aiohttp==3.10.5 requests==2.32.3`.
- Run `6_asyncio_async_await/async_image_downloader.py`.
- Observe the difference in speed between the synchronous and asynchronous approaches.