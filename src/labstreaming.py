import pylsl

class Streamer():
    def __init__(self, s_name, s_type):
        self.info = pylsl.StreamInfo(s_name, s_type, 1, pylsl.IRREGULAR_RATE, 'float32', str(s_type) + '_' + str(s_name))
        self.outlet = pylsl.StreamOutlet(self.info)

    def push(self, x):
        self.outlet.push_sample(x)

class Receiver():
    def __init__(self, s_name, s_type, timeout = 0.2):
        streams = pylsl.resolve_stream('source_id', str(s_type) + '_' + str(s_name))

        self.inlet = pylsl.StreamInlet(streams[0])
        self.info = self.inlet.info()
        self.n_channels = self.info.channel_count()
        self.timeout = timeout
    
    def get(self):
        x = self.inlet.pull_sample(self.timeout)
        return x