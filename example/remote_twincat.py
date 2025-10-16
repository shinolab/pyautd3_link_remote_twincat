import numpy as np
from pyautd3 import AUTD3, Controller, Focus, FocusOption, Hz, Sine, SineOption

from pyautd3_link_remote_twincat import RemoteTwinCAT, RemoteTwinCATOption

if __name__ == "__main__":
    with Controller.open(
        [AUTD3(pos=[0.0, 0.0, 0.0], rot=[1.0, 0.0, 0.0, 0.0])],
        RemoteTwinCAT(
            "0.0.0.0",  # noqa: S104
            "1.1.1.1.1.1",
            RemoteTwinCATOption(),
        ),
    ) as autd:
        autd.send(
            (
                Sine(freq=150.0 * Hz, option=SineOption()),
                Focus(pos=autd.center + np.array([0.0, 0.0, 150.0]), option=FocusOption()),
            ),
        )

        _ = input("Press Enter to exit")

        autd.close()
