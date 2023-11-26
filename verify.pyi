# verify.pyi

from typing import Union, AnyStr

def verify(
    *, data_bytes: bytes, shared_secret: Union[bytes, bytearray], hmac_sha256: AnyStr
) -> bool: ...
