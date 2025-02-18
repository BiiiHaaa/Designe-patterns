# Command Interface
class Command:
    def execute(self):
        pass

# Concrete Commands
class TurnOnLightCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        return self.light.turn_on()

class TurnOffLightCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        return self.light.turn_off()

# Receiver (The actual implementation)
class Light:
    def turn_on(self):
        return "Light is ON"

    def turn_off(self):
        return "Light is OFF"

# Invoker (Takes the command and executes it)
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        if self.command:
            return self.command.execute()
        return "No command set"

# Client Code
light = Light()
remote = RemoteControl()

# Turning the light ON
turn_on_command = TurnOnLightCommand(light)
remote.set_command(turn_on_command)
print(remote.press_button())  # Output: Light is ON

# Turning the light OFF
turn_off_command = TurnOffLightCommand(light)
remote.set_command(turn_off_command)
print(remote.press_button())  # Output: Light is OFF
