class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Initializes staus, muted, volume, and channel variables
        """
        self._status = False
        self._muted = False
        self._volume = Television.MIN_VOLUME
        self._channel = Television.MIN_CHANNEL



    def power(self) -> None:
        """
        Turns TV on and off
        """
        if self._status:
            self._status = False
        else:
            self._status = True



    def mute(self) -> None:
        """
        Mutes and unmutes TV when the TV is on and sets volume to minimum volume
        """
        if self._status:
            if self._muted:
                self._muted = False
            else:
                self._muted = True



    def channel_up(self) -> None:
        """
        When TV is on, increase channel by one.
        If channel is at max, cycle back to the minimum channel number
        """
        if self._status:
            if self._channel + 1 <= Television.MAX_CHANNEL:
                self._channel += 1
            else:
                self._channel = Television.MIN_CHANNEL



    def channel_down(self)-> None:
        """
        When TV is on, decrease channel by one.
        If channel is at mininum, cycle back to the maximum channel number
        """
        if self._status:
            if self._channel - 1 >= Television.MIN_CHANNEL:
                self._channel -= 1
            else:
                self._channel = Television.MAX_CHANNEL



    def volume_up(self) -> None:
        """
      When TV is on, increase volume by one.
      If TV is already at max volume, volume stays at max
      """
        if self._status:
            if self._muted:
                self._muted = False
            if self._volume != Television.MAX_VOLUME:
                self._volume += 1




    def volume_down(self) -> None:
        """
      When TV is on, decrease volume by one.
      If TV is already at min volume, volume stays at min
      """
        if self._status:
            if self._muted:
                self._muted = False
            if self._volume != Television.MIN_VOLUME:
                self._volume -= 1


    def __str__(self) -> str:
        """
        Return status, channel, and volume values
        """

        if self._muted:
            return f"Power = {self._status}, Channel = {self._channel}, Volume = {Television.MIN_VOLUME}"
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}"