# JANUS LAB ONLY variant: PORT_MODE B TIGHT_ONLY with the X-HEEP SPI slave ENABLED (has_spi_slave=1).
# The SPI slave is an external OBI master on the debug crossbar port (like the debug SBA); production configs disable it.
# Use only for the SPI/SBA stand-in experiments (external master at boot / after the lock); never for headline numbers.
# Thin wrapper: loads configs/janus.py (the product configuration) and calls config() with other arguments, so the
# configuration file name selects the build (X_HEEP_CFG=configs/janus_lab_b.py).
import importlib.util
import os


def config():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "janus.py")
    spec = importlib.util.spec_from_file_location("configs._janus_base", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.config(port_mode=1, spi_slave=1)
