from pyautd3_link_remote_twincat import RemoteTwinCAT, RemoteTwinCATOption


def test_remote_twincat():
    _ = RemoteTwinCAT(
        "0.0.0.0",  # noqa: S104
        "1.1.1.1.1.1",
        RemoteTwinCATOption(),
    )
