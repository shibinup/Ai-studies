import time
start_time = time.perf_counter()
users=["shibin","isha","shahan","muneer"]
def helloying(users):
    for i in users:
        print("helllo",i)
        time.sleep(1)
def hying(users):
      for i in users:
        print("hyyy",i)
        time.sleep(1)
helloying(users)
hying(users)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Total execution time: {elapsed_time:.4f} seconds")