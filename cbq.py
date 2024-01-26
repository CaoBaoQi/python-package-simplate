import os
import sys
import subprocess
from rich import print
from rich.table import Table
from rich.console import Console
from rich.prompt import Prompt
from rich.markdown import Markdown


def get_base_path():
    """
    获取程序运行时的基础路径。
    在打包后的环境中使用 sys._MEIPASS，否则使用脚本的目录。
    """
    if getattr(sys, 'frozen', False):
        # 如果程序是被 PyInstaller 打包的
        return os.path.dirname(sys.executable)
    else:
        # 如果程序是在开发环境中运行的
        return os.path.dirname(os.path.abspath(__file__))


def list_commands():
    """
    列出 simplate-rich 文件夹中的所有 Python 脚本作为可用命令。
    """
    commands = {}
    base_path = get_base_path()
    simplate_rich_dir = os.path.join(base_path, 'src', 'simplate-rich')
    for index, file in enumerate(os.listdir(simplate_rich_dir)):
        if file.endswith('.py') and file != '__init__.py':
            command_name = file[:-3]  # 移除.py后缀
            commands[str(index + 1)] = command_name  # 将命令与序号关联
    return commands


def display_commands(commands):
    """
    使用 rich 表格显示命令。
    """
    table = Table(show_header=True, header_style="magenta")
    table.add_column("序号", style="white", width=6, justify="center")
    table.add_column("命令", style="bold", justify="left")

    for num, cmd in commands.items():
        table.add_row(num, cmd)

    console = Console()
    console.print(table)


def main():
    try:
        console = Console()
        markdown_content = "# Welcome-to-Simplate-Rich@CaoBaoQi"
        console.print(Markdown(markdown_content, style="red"))

        commands = list_commands()
        while True:
            print("\n[bold]可用命令：[/bold]")
            display_commands(commands)
            print("[italic]输入 'exit' 退出程序。[/italic] :door:")

            choice = Prompt.ask("\n请输入要执行的命令序号或名称", default="exit").strip()
            if choice.lower() == 'exit':
                print(":wave: 再见!\n")
                break

            command_name = commands.get(choice) or (choice if choice in commands.values() else None)
            if command_name:
                command = f"python -m src.simplate-rich.{command_name}"
                subprocess.run(command, shell=True)
            else:
                print("[bold red]无效的命令。[/bold red] :exclamation:")
        ...
    except KeyboardInterrupt:
        print("\n\n:wave: 检测到 Ctrl + C，程序正在退出...")
        # 可以在这里做一些清理工作，如果需要的话
    except Exception as e:
        print(f"发生异常: {e}")
        # 可以在这里处理其他意外异常


if __name__ == "__main__":
    main()
