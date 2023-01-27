from cores.openai.core import ChatGPT

chatgpt = ChatGPT()
res, usage = chatgpt.chat("你是机器人吗？")
