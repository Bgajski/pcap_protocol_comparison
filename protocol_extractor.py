# Network protocol extraction handler

class ProtocolExtractor:
    def __init__(self, packet):
        self.packet = packet

    def extract(self):
        raise NotImplementedError("Extraction method is not implemented")


class TCP(ProtocolExtractor):
    def extract(self):
        try:
            return hasattr(self.packet, 'tcp')
        except Exception as e:
            print(f"Error extracting TCP data: {e}")
            return False


class UDP(ProtocolExtractor):
    def extract(self):
        try:
            return hasattr(self.packet, 'udp')
        except Exception as e:
            print(f"Error extracting UDP data: {e}")
            return False


class SSL(ProtocolExtractor):
    def extract(self):
        try:
            return hasattr(self.packet, 'ssl')
        except Exception as e:
            print(f"Error extracting SSL data: {e}")
            return False

