# JANUS variant: build A+F = PORT_MODE A (LOOSE_ONLY) + the per-initiator filter on every ext_xbar master port
# Thin wrapper: loads configs/janus.py (the product configuration) and calls config() with other arguments, so the
# configuration file name selects the build (X_HEEP_CFG=configs/janus_af.py). Spec: janus/eval/docs/af_filter.md.
# Red-team and ablation variants are the same call with other arguments (af_check_mask, af_reset_enable, af_prelock).
import importlib.util
import os


def config():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "janus.py")
    spec = importlib.util.spec_from_file_location("configs._janus_base", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.config(port_mode=0, af=1)
