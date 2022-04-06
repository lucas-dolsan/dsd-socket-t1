from dataclasses import dataclass

@dataclass
class SocketMessageEncoder:
    encoding: str

    def encode(self, data: any) -> bytes:
        return bytes(data, encoding=self.encoding)

    def decode(self, data: bytes) -> str:
        return data.decode(encoding=self.encoding) 
