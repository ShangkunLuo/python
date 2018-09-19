#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "mengdj@outlook.com"
import unittest

from pcap.proc.pcap import Pcap
from pcap.proc.rtmp import RTMP


def callback_rtmp(ins, msg, fr):
    if msg.__class__.__name__ == "str":
        print(msg)
        if msg == "C1":
            print("time:%d zero:%d" % (ins.c1.time, ins.c1.zero))


class PcapTest(unittest.TestCase):
    """测试"""

    def test_rtmp(self):
        t = 3
        print("tt:%s" % bin(t >> 6))

    def test_load(self):
        _pcap = Pcap()
        _gen = _pcap.parse("data/1.pcap")
        for _packet in _gen:
            _mac = _packet.data
            _net = _mac.data
            _trans = _net.data
            if _trans.__class__.__name__ == "TCP":
                # 打印tcp的选项数据
                # print(_trans.option)

                _app = _trans.data
                if _packet.head.usec == 525657:
                    print([hex(i) for i in _app])

                if _app is not None:
                    if RTMP.find(_trans, callback_rtmp):
                        # 依次打印网络层、传输层头部
                        print(_packet.head)
                        # print(_net)
                        # print(_trans)
                        pass


if __name__ == "__main__":
    unittest.main()
