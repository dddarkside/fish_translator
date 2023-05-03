import coder,decoder
import h2f_gui

# coding: utf8

app = h2f_gui.GUI(decoder.decode, coder.encode)
app.start()
