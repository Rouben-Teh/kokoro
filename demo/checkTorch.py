# import torch
# print(torch.version.cuda)

from kokoro import KPipeline
p = KPipeline(lang_code='j')
print(p.g2p("こんにちは"))