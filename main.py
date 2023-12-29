# This is a sample Python script.
from youtube_processor import YouTubeProcessor
from gui_components import AppGUI


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    processor = YouTubeProcessor()
    app = AppGUI(processor=processor)
    app.run()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
