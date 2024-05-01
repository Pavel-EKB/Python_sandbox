from multiprocessing import Process
def func():
    print("Hello from child Process")
if __name__ == "__main__":
    print("Hello from main Process")
    proc = Process(target=func)
    proc.start()
    print(f"Proc is_alive status: {proc.is_alive()}")
    proc.join() #выполнение программы будет остановлено до тех пор пока процесс не завершит работу
    print("Goodbye")
    print(f"Proc is_alive status: {proc.is_alive()}")