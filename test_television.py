import unittest

from television import*


class MyTestCase(unittest.TestCase):
    # set up and tear down
    def setUp(self):
        self.tv = Television()
        self.tv2 = Television()

    def tearDown(self):
        del self.tv
        del self.tv2

    # test init
    def test_init(self):
        print(self.tv)

    # test status
    def test_power(self):
        self.tv.power()
        self.assertEqual(self.tv._status, True)
        self.tv.power()
        self.assertEqual(self.tv._status, False)

    # test mute
    def test_mute(self):
        self.tv.power()
        self.tv.volume_up()
        self.tv.mute()
        self.assertEqual(self.tv._muted, True)
        self.assertEqual(self.tv._volume, 0)

        self.tv.mute()
        self.assertEqual(self.tv._muted, False)



    # test channel_up
    def test_channel_up(self):
        self.assertEqual(self.tv2._status, False)
        self.tv2.channel_up()
        self.assertEqual(self.tv2._channel, 0)

        self.tv2.power()
        self.assertEqual(self.tv2._status, True)
        self.tv2.channel_up()
        self.assertEqual(self.tv2._channel, 1)

        self.tv2.channel_up()
        self.tv2.channel_up()
        self.tv2.channel_up()
        self.assertEqual(self.tv2._channel, 0)


    # test channel_down
    def test_channel_down(self):
        self.tv2.channel_down()
        self.assertEqual(self.tv2._channel, 0)

        self.tv2.power()
        self.assertEqual(self.tv2._status, True)
        self.tv2.channel_down()
        self.assertEqual(self.tv2._channel, 3)


    # # test volume_up
    def test_volume_up(self):
        self.tv2.volume_up()
        self.assertEqual(self.tv2._volume, 0)

        self.tv2.power()
        self.tv2.volume_up()
        self.assertEqual(self.tv2._volume, 1)

        self.tv2.mute()
        self.tv2.volume_up()
        self.assertEqual(self.tv2._volume, 2)

        self.tv2.volume_up()
        self.tv2.volume_up()
        self.assertEqual(self.tv2._volume, 2)



    # test volume_down
    def test_volume_down(self):
        self.tv2.volume_down()
        self.assertEqual(self.tv2._volume, 0)

        self.tv2.power()
        self.tv2._volume = Television.MAX_VOLUME
        self.tv2.volume_down()
        self.assertEqual(self.tv2._volume, 1)

        self.tv2._volume = Television.MAX_VOLUME
        self.tv2.mute()
        self.tv2.volume_down()
        self.assertEqual(self.tv2._volume, 0)

        self.tv2._volume = Television.MAX_VOLUME
        self.tv2.volume_down()
        self.tv2.volume_down()
        self.tv2.volume_down()
        self.assertEqual(self.tv2._volume, 0)





if __name__ == '__main__':
    unittest.main()
