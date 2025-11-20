class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self._status = False
        self._muted = False
        self._volume = Television.MIN_VOLUME
        self._channel = Television.MIN_CHANNEL


    def power(self):
        if self._status:
            self._status = False
        else:
            self._status = True


    def mute(self):
        if self._status:
            if self._muted:
                self._muted = False
            else:
                self._muted = True


    def channel_up(self):
        if self._status:
            if self._channel + 1 <= Television.MAX_CHANNEL:
                self._channel += 1
            else:
                self._channel = Television.MIN_CHANNEL


    def channel_down(self):
        if self._status:
            if self._channel - 1 >= Television.MIN_CHANNEL:
                self._channel -= 1
            else:
                self._channel = Television.MAX_CHANNEL


    def volume_up(self):
        if self._status:
            if self._muted:
                self.mute()

            if self._volume != Television.MAX_VOLUME:
                self._volume += 1


    def volume_down(self):
        if self._status:
            if self._muted:
                self.mute()

            if self._volume != Television.MIN_VOLUME:
                self._volume -= 1



    def __str__(self):
        if self._muted:
            return f"Power = {self._status}, Channel = {self._channel}, Volume = {Television.MIN_VOLUME}"
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}"