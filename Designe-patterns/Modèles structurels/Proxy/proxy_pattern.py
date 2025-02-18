from abc import ABC, abstractmethod

# Subject Interface
class Subject(ABC):
    @abstractmethod
    def request(self):
        pass

# Real Subject
class RealSubject(Subject):
    def request(self):
        return "RealSubject: Handling request"

# Proxy Class
class Proxy(Subject):
    def __init__(self, real_subject: RealSubject):
        self._real_subject = real_subject
    
    def request(self):
        if self._check_access():
            result = self._real_subject.request()
            self._log_access()
            return result
        return "Proxy: Access Denied"
    
    def _check_access(self):
        print("Proxy: Checking access before forwarding request...")
        return True  # Simulating an access check
    
    def _log_access(self):
        print("Proxy: Logging request access.")

# Client Code
def client_code(subject: Subject):
    print(subject.request())

# Running the code
print("Client: Executing with a RealSubject:")
real_subject = RealSubject()
client_code(real_subject)

print("\nClient: Executing with a Proxy:")
proxy = Proxy(real_subject)
client_code(proxy)
