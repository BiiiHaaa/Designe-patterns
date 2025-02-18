from singleton import Singleton

def main():
    instance1 = Singleton.get_instance()
    instance2 = Singleton.get_instance()
    
    print("Instance 1 ID:", id(instance1))
    print("Instance 2 ID:", id(instance2))
    
    if instance1 is instance2:
        print("Both instances are the same.")
    else:
        print("Instances are different, which should not happen in a singleton.")

if __name__ == "__main__":
    main()