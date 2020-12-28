#不知道为什么vscode不能直接调试conda环境库里的代码，从这里设置入口方便调试
from labelme import __main__
__main__.main()