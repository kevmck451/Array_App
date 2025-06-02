
from gui.window_main import Main_Window
from controller.controller import Controller
from engine.array.AudioStream import Mic_Array
from engine.temp_sensor.client import Sender_Client
from engine.server.server import Server
from gui.array_selector import get_array_selection



if __name__ == "__main__":

    selection, app_device = get_array_selection()

    if selection == 'RECT':
        from engine.array import array_config_RECT as array_config
    else: from engine.array import array_config_LINE as array_config

    if app_device == 'mac':
        from gui import configuration as device_config
    elif app_device == 'pi':
        from gui import configuration_pi as device_config
    else: from gui import configuration_monitor as device_config

    temp_sensor = Sender_Client(name='macbook')
    audio_realtime = Mic_Array(array_config)

    controller = Controller(array_config, device_config)

    gui = Main_Window(controller.handle_event, array_config, device_config)

    server = Server(port=array_config.server_port)
    server.controller = controller
    server.start()

    controller.add_peripherals(temp_sensor, audio_realtime, gui, server)

    gui.mainloop()
