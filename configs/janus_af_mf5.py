# JANUS red-team variant MF5: build A+F with an IOPMP-style open reset (unchecked until the ROM enables the filter)
# Thin wrapper: loads configs/janus.py (the product configuration) and calls config() with other arguments, so the
# configuration file name selects the build (X_HEEP_CFG=configs/janus_af_mf5.py). Spec: janus/eval/docs/af_filter.md section 7.5.
import importlib.util
import os


def config():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "janus.py")
    spec = importlib.util.spec_from_file_location("configs._janus_base", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.config(port_mode=0, af=1, af_reset_enable=0)
