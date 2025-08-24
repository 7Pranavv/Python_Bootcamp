def very_slow_func():
    print("Oyee.........")
    print("Oyee.........")
    print("Oyee.........")
    print("Oyee.........")
    print("Oyee.........")
    print("Oyee.........")
    return 70
#a=very_slow_func()
if((a:=very_slow_func())>10):
    print(a)

else:
    print("its not greater than 10")