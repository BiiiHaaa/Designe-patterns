from abc import ABC, abstractmethod

# State Interface
class TrafficLightState(ABC):
    @abstractmethod
    def change(self, traffic_light):
        pass

    @abstractmethod
    def show_signal(self):
        pass

# Concrete States
class RedLight(TrafficLightState):
    def change(self, traffic_light):
        traffic_light.state = GreenLight()  # Change to Green

    def show_signal(self):
        print("🚦 Red Light - STOP!")

class GreenLight(TrafficLightState):
    def change(self, traffic_light):
        traffic_light.state = YellowLight()  # Change to Yellow

    def show_signal(self):
        print("🚦 Green Light - GO!")

class YellowLight(TrafficLightState):
    def change(self, traffic_light):
        traffic_light.state = RedLight()  # Change to Red

    def show_signal(self):
        print("🚦 Yellow Light - SLOW DOWN!")

# Context (Traffic Light)
class TrafficLight:
    def __init__(self):
        self.state = RedLight()  # Initial State

    def change_state(self):
        self.state.change(self)

    def show_signal(self):
        self.state.show_signal()

# Client Code
traffic_light = TrafficLight()

for _ in range(5):  # Cycle through states
    traffic_light.show_signal()
    traffic_light.change_state()
