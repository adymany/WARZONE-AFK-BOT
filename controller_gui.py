import vgamepad as vg
import random
import time
import math
from datetime import datetime


def create_controller():
    try:
        return vg.VX360Gamepad()
    except Exception as e:
        print(f"Error creating controller: {e}")
        return None
    time.sleep(300)

class HumanlikeMovement:
    def __init__(self):
        self.last_x = 0
        self.last_y = 0
        self.current_direction = 0
        
    def smooth_camera(self, target_x, target_y, steps=10):
        """Generate smooth camera movement values"""
        x_step = (target_x - self.last_x) / steps
        y_step = (target_y - self.last_y) / steps
        
        for i in range(steps):
            current_x = self.last_x + x_step * i
            current_y = self.last_y + y_step * i
            yield (int(current_x), int(current_y))
            
        self.last_x = target_x
        self.last_y = target_y

def human_like_scan(gamepad, movement):
    """Smooth, human-like camera movement"""
    # Generate a natural looking sweep
    target_x = random.randint(-16384, 16384)
    target_y = random.randint(-8192, 8192)  # Less vertical movement
    
    for x, y in movement.smooth_camera(target_x, target_y):
        gamepad.right_joystick(x_value=x, y_value=y)
        gamepad.update()
        time.sleep(0.02)  # Smooth 50Hz updates

def combat_sequence(gamepad, movement):
    """Simulates combat movement with shooting and jumping"""
    # Aim and shoot sequence
    for _ in range(random.randint(1, 3)):
        # Quick aim adjustment
        target_x = random.randint(-8192, 8192)
        target_y = random.randint(-4096, 4096)
        
        for x, y in movement.smooth_camera(target_x, target_y, steps=5):
            gamepad.right_joystick(x_value=x, y_value=y)
            gamepad.update()
            time.sleep(0.02)
        
        # Trigger pull (right trigger for shooting)
        gamepad.right_trigger(value=255)
        gamepad.update()
        time.sleep(random.uniform(0.1, 0.3))
        gamepad.right_trigger(value=0)
        gamepad.update()

def jump_and_move(gamepad):
    """Performs jump with movement"""
    # Press A button (jump)
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.update()
    
    # Add some movement while jumping
    gamepad.left_joystick(
        x_value=random.randint(-32768, 32767),
        y_value=random.randint(-32768, 32767)
    )
    gamepad.update()
    
    
    
    # Release jump button
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.update()

def natural_movement_sequence(gamepad, movement):
    """Combines movement, looking, and combat in a natural way"""
    # Move in a direction
    gamepad.left_joystick(
        x_value=random.randint(-32768, 32767),
        y_value=random.randint(-32768, 32767)
    )
    
    # Look around naturally
    human_like_scan(gamepad, movement)
    
    # Chance to jump
    if random.random() < 0.15:  # 15% chance to jump
        jump_and_move(gamepad)
    
    # Chance to engage in combat
    if random.random() < 0.4:  # 40% chance to shoot
        combat_sequence(gamepad, movement)

def tactical_movement(gamepad, movement):
    """Simulates tactical checking of corners and angles"""
    angles = [
        (16384, 0),    # Right
        (-16384, 0),   # Left
        (8192, -4096), # Up-right
        (-8192, -4096) # Up-left
    ]
    
    for angle_x, angle_y in random.sample(angles, random.randint(2, 3)):
        for x, y in movement.smooth_camera(angle_x, angle_y):
            gamepad.right_joystick(x_value=x, y_value=y)
            gamepad.update()
            time.sleep(0.02)
            
        # Pause briefly at each angle
        time.sleep(random.uniform(0.1, 0.3))
        
        # Chance to shoot while checking angle
        if random.random() < 0.2:  # 20% chance
            gamepad.right_trigger(value=255)
            gamepad.update()
            time.sleep(random.uniform(0.1, 0.2))
            gamepad.right_trigger(value=0)
            gamepad.update()

def main():
    flag=0
    print("Initializing enhanced controller script...")
    gamepad = create_controller()
    movement = HumanlikeMovement()
    
    if not gamepad:
        print("Failed to create controller. Exiting...")
        return
    
    print("Starting enhanced movement script...")
    print("Press Ctrl+C to stop")
    
    actions = [
        (natural_movement_sequence, "Natural movement"),
        (tactical_movement, "Tactical checking"),
        (combat_sequence, "Combat sequence"),
        (human_like_scan, "Looking around")
    ]
    
    try:
        while flag==0:
            flag=bool(input("1 to start"))
        while flag==1:
            # Select and execute a random action
            action, name = random.choice(actions)
            print(f"{datetime.now().strftime('%H:%M:%S')} - {name}")
            
            # Execute the action
            action(gamepad, movement)
            
            # Short, variable delay between actions
            time.sleep(random.uniform(0.2, 0.6))
            
            # Occasionally jump
            if random.random() < 0.1:  # 20% chance
                jump_and_move(gamepad)
            
    except KeyboardInterrupt:
        print("\nScript stopped by user")
    finally:
        if gamepad:
            gamepad.reset()
            print("Controller reset")

if __name__ == "__main__":
    main()