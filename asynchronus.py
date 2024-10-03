#asynchronus programming

import asyncio

async def task_1():
    print("Task 1 started")
    await asyncio.sleep(5)
    print("Task 1 ended!!!1")

async def task_2():
    print("Task 2 started")
    await asyncio.sleep(2)
    print("Task 2 ended") 


# async def main():
#     task1=asyncio.create_task(task_1())
#     task2=asyncio.create_task(task_2())

async def main():
    # Start both tasks at the same time
    await asyncio.gather(
        task_1(),
        task_2()
    )

   

# asyncio.run(main())

if __name__=="__main__":
    asyncio.run(main())