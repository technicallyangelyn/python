from television import*


tv = Television()
tv2 = Television()

# test init
def test_init():
    assert tv.__str__() == f"Power = {tv._status}, Channel = {tv._channel}, Volume = {tv._volume}"

# test status
def test_power():
    tv.power()
    assert tv._status == True
    tv.power()
    assert tv._status == False

# test mute
def test_mute():
    tv.power()
    tv.volume_up()
    tv.mute()
    assert tv._muted == True

    assert tv._status == True
    tv.mute()
    assert tv._muted == False

    tv.power()
    assert tv._muted == False

    tv.mute()
    assert tv._muted == False





# test channel_up
def test_channel_up():
    assert tv2._status == False
    tv2.channel_up()
    assert tv2._channel == 0

    tv2.power()
    assert tv2._status == True
    tv2.channel_up()
    assert tv2._channel == 1

    tv2.channel_up()
    tv2.channel_up()
    tv2.channel_up()
    assert tv2._channel == 0


# test channel_down
def test_channel_down():
    assert tv2._status == True
    assert tv2._channel == 0
    tv2.channel_down()
    assert tv2._channel == 3

    tv2.power()
    assert tv2._status == False
    tv2.channel_down()
    assert tv2._channel == 3


# # test volume_up
def test_volume_up():
    tv2.volume_up()
    assert tv2._volume == 0

    tv2.power()
    tv2.volume_up()
    assert tv2._volume == 1

    tv2.mute()
    tv2.volume_up()
    assert tv2._volume == 2

    tv2.volume_up()
    tv2.volume_up()
    assert tv2._volume == 2



# test volume_down
def test_volume_down():
    tv2.power()
    assert tv2._status == False
    tv2._volume = Television.MIN_VOLUME
    tv2.volume_down()
    assert tv2._volume == 0

    tv2.power()
    tv2._volume = Television.MAX_VOLUME
    tv2.volume_down()
    assert tv2._volume == 1

    tv2._volume = Television.MAX_VOLUME
    tv2.mute()
    tv2.volume_down()
    assert tv2._volume == 1

    tv2._volume = Television.MAX_VOLUME
    tv2.volume_down()
    tv2.volume_down()
    tv2.volume_down()
    assert tv2._volume == 0




