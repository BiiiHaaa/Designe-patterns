# Observer Interface
class Observer:
    def update(self, message):
        pass

# Concrete Observers (Subscribers)
class Subscriber(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received news update: {message}")

# Subject (News Agency)
class NewsAgency:
    def __init__(self):
        self.subscribers = []
        self.latest_news = None

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def remove_subscriber(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify_subscribers(self):
        for subscriber in self.subscribers:
            subscriber.update(self.latest_news)

    def publish_news(self, news):
        self.latest_news = news
        print("\nNews Published:", news)
        self.notify_subscribers()

# Client Code
news_agency = NewsAgency()

alice = Subscriber("Alice")
bob = Subscriber("Bob")

news_agency.add_subscriber(alice)
news_agency.add_subscriber(bob)

news_agency.publish_news("Python 3.12 Released!")  # Both Alice and Bob receive updates

news_agency.remove_subscriber(alice)

news_agency.publish_news("New AI Breakthrough!")  # Only Bob receives the update
