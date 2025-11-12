from dpeaDPi.DPiComputer import DPiComputer
from dpeaDPi.DPiStepper import DPiStepper

dpiComputer = DPiComputer()
dpiStepper = DPiStepper()
                

input_ports = [dpiComputer.IN_CONNECTOR__IN_0,
                dpiComputer.IN_CONNECTOR__IN_1,
                dpiComputer.IN_CONNECTOR__IN_2,
                dpiComputer.IN_CONNECTOR__IN_3]

output_ports = [dpiComputer.OUT_CONNECTOR__OUT_0,
                dpiComputer.OUT_CONNECTOR__OUT_1,
                dpiComputer.OUT_CONNECTOR__OUT_2,
                dpiComputer.OUT_CONNECTOR__OUT_3]


def initialize():
    assert dpiComputer.initialize(), "DPiComputer failed to initialize."
    assert dpiStepper.initialize(), "DPiStepper failed to initialize."

def read_input(port_number):
    return dpiComputer.readDigitalIn(input_ports[port_number])

def set_output(port_number, state: bool):
    dpiComputer.writeDigitalOut(output_ports[port_number], state)