# from gmail import GMail, Message
#
# from random import choice
#
# content = '''<p></p>
# <p style="text-align: center;">Cộng h&ograve;a x&atilde; hội chủ nghĩa Việt Nam</p>
# <p style="text-align: center;">Độc lập - Tự do - Hạnh ph&uacute;c</p>
# <p style="text-align: center;">&nbsp;</p>
# <p style="text-align: center;">&nbsp;</p>
# <h1 style="text-align: center;">Đơn xin nghỉ học</h1>
# <p>Em t&ecirc;n l&agrave;: Nguyễn Quang Duy</p>
# <p>&nbsp;</p>
# <p>Do h&ocirc;m qua em đi bay về muộn, giữa đường về c&ograve;n bị {{sickness}}. V&igrave; vậy, h&ocirc;m nay em xin ph&eacute;p c&ocirc; một c&aacute;ch nghi&ecirc;m t&uacute;c nhất cho em nghỉ một buổi học.</p>
# <p>Em hứa sẽ ghi ch&eacute;p b&agrave;i đầy đủ!</p>
# <p>&nbsp;</p>
# <p>&nbsp;</p>
# <p>Người l&agrave;m đơn,</p>
# <p>Duy</p>
# <p>&nbsp;</p>
# <p>,</p>'''
#
# sickness = [
# "ốm",
# "tiêu chảy",
# "sida"
# ]
#
# n = choice(sickness)
# gmail = GMail('sinhnhat2509@gmail.com', 'sinhnhat')
# msg = Message('Absent Request', to = 'sinhnhat2509@gmail.com', html = content.replace("{{sickness}}", n))
# gmail.send(msg)
