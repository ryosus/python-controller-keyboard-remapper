from inputs import get_gamepad
import vgamepad as vg
import math
import threading

class XboxController(object):
    MAX_TRIG_VAL = math.pow(2, 8)
    MAX_JOY_VAL = math.pow(2, 15)

    
    def __init__(self):

        self.LeftJoystickY = 0
        self.LeftJoystickX = 0
        self.RightJoystickY = 0
        self.RightJoystickX = 0
        self.LeftTrigger = 0
        self.RightTrigger = 0
        self.LeftBumper = 0
        self.RightBumper = 0
        self.A = 0
        self.X = 0
        self.Y = 0
        self.B = 0
        self.LeftThumb = 0
        self.RightThumb = 0
        self.Back = 0
        self.Start = 0
        self.LeftDPad = 0
        self.RightDPad = 0
        self.UpDPad = 0
        self.DownDPad = 0

        self._monitor_thread = threading.Thread(target=self._monitor_controller, args=())
        self._monitor_thread.daemon = True
        self._monitor_thread.start()


    def read(self): # return the buttons/triggers that you care about in this methode
        ljY = self.LeftJoystickY
        ljX = self.LeftJoystickX
        rjY = self.RightJoystickY
        rjX = self.RightJoystickX
        lt = self.LeftTrigger
        rt = self.RightTrigger
        lb = self.LeftBumper
        rb = self.RightBumper
        a = self.A
        x = self.X
        y = self.Y
        b = self.B
        lTh = self.LeftThumb
        rTh = self.RightThumb
        back = self.Back
        start = self.Start
        dpL = self.LeftDPad
        dpR = self.RightDPad
        dpU = self.UpDPad
        dpD = self.DownDPad

        return [ljY, ljX, rjY, rjX, lt, rt, lb, rb, a, x, y, b, lTh, rTh, back, start, dpL, dpR, dpU, dpD]


    def _monitor_controller(self):
        while True:
            
            while True:
                try:
                    events = get_gamepad()
                except:
                    continue
                else:
                    break
            
                
            
            for event in events:
                if event.code == 'ABS_Y':
                    self.LeftJoystickY = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_X':
                    self.LeftJoystickX = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_RY':
                    self.RightJoystickY = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_RX':
                    self.RightJoystickX = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_Z':
                    self.LeftTrigger = event.state / XboxController.MAX_TRIG_VAL # normalize between 0 and 1
                elif event.code == 'ABS_RZ':
                    self.RightTrigger = event.state / XboxController.MAX_TRIG_VAL # normalize between 0 and 1
                elif event.code == 'BTN_TL':
                    self.LeftBumper = event.state
                elif event.code == 'BTN_TR':
                    self.RightBumper = event.state
                elif event.code == 'BTN_SOUTH':
                    self.A = event.state
                elif event.code == 'BTN_NORTH':
                    self.X = event.state
                elif event.code == 'BTN_WEST':
                    self.Y = event.state
                elif event.code == 'BTN_EAST':
                    self.B = event.state
                elif event.code == 'BTN_THUMBL':
                    self.LeftThumb = event.state
                elif event.code == 'BTN_THUMBR':
                    self.RightThumb = event.state
                elif event.code == 'BTN_SELECT':
                    self.Back = event.state
                elif event.code == 'BTN_START':
                    self.Start = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY1':
                    self.LeftDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY2':
                    self.RightDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY3':
                    self.UpDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY4':
                    self.DownDPad = event.state




if __name__ == '__main__':
    gamepad = vg.VX360Gamepad()
    
    joy = XboxController()
    while True:
        #ljY, ljX, rjY, rjX, lt, rt, lb, rb, a, x, y, b, lTh, rTh, back, start, dpL, dpR, dpU, dpD
        # 0    1    2    3    4   5   6   7  8  9  10 11 12   13   14    15     16   17   18   19
        originalInputs = joy.read()
        
        ljY = originalInputs[0]
        ljX = originalInputs[1]
        rjY = originalInputs[2]
        rjX = originalInputs[3]
        lt = originalInputs[4]
        rt = originalInputs[5]
        lb = originalInputs[6]
        rb = originalInputs[7]
        a = originalInputs[8]
        x = originalInputs[9]
        y = originalInputs[10]
        b = originalInputs[11]
        lTh = originalInputs[12]
        rTh = originalInputs[13]
        back = originalInputs[14]
        start = originalInputs[15]
        dpL = originalInputs[16]
        dpR = originalInputs[17]
        dpU = originalInputs[18]
        dpD = originalInputs[19]
        
        gamepad.left_joystick_float(x_value_float=ljX, y_value_float=ljY)
        gamepad.right_joystick_float(x_value_float=rjX, y_value_float=rjY)
        gamepad.left_trigger_float(value_float=lt)
        gamepad.right_trigger_float(value_float=rt)
        if lb == 1:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
        else:
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
        
        if rb == 1:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
        else:
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
        
        if a == 1:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        else:
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        
        if x == 1:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
        else:
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
            
        if y == 1:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
        else:
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)

        if b == 1:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
        else:
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            
        if lTh == 1:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
        else:
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB)
            
        if rTh == 1:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
        else:
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB)
        
        if back == 1:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
        else:
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
        
        if start == 1:
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
        else:
            gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
            
        
        gamepad.update()
        