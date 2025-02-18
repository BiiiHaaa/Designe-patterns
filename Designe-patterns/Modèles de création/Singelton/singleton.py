class Singleton:
    # Private class variable to hold the single instance
    __instance = None

    @staticmethod
    def get_instance():
        """
        Static method to get the singleton instance.
        If no instance exists, create one.
        """
        if Singleton.__instance is None:
            Singleton.__instance = Singleton()
        return Singleton.__instance

    def __init__(self):
        """
        Private constructor to prevent multiple instances.
        """
        if Singleton.__instance is not None:
            raise Exception("This class is a singleton! Use get_instance() instead.")

# Example usage
singleton1 = Singleton.get_instance()
singleton2 = Singleton.get_instance()

print(singleton1 is singleton2)  # True