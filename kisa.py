# -*- coding: utf-8 -*-
"""
kise -- Keyboard Interrupt + System Exit

see https://github.com/PavelMSTU/kisa/blob/master/README.md

see __test() for example

Created by pavel on 07.03.17 22:22
"""
import signal
import sys

__author__ = 'pavelmstu'
__mail__ = 'pavelmstu@stego.su'

# #####################################
# ### You can change default params!

# types of signals, which kisa is supported by default
DEFAULT_SIGNALS_LIST = [
    signal.SIGINT,
    # signal.SIGKILL, It is impossible! See http://stackoverflow.com/questions/3908694/sigkill-signal-handler
    signal.SIGQUIT,
    # if you are add signal, please change default_do_signal function
]

DEFAULT_SIGNAL_MESSAGE = \
    "***Signal for quit script is get! Please wait while critical code will be done***"

DEFAULT_END_WORK_MESSAGE = \
    "***End critical code. Exit from with Kisa statement***"


def default_do_signal(signal_no):
    """
    Do signal work after with statement in Kisa
    :param signal_no: number of signal
    :return:
    """
    if signal_no == signal.SIGINT:
        raise KeyboardInterrupt("KeyboardInterrupt in Kisa")

    print("{0} in Kisa. exit".format(signal.SIGKILL))
    sys.exit()


# #####################################
# ### Don't change this params!

SIGNAL_INFO = [None]
MESSAGE = [None]


def default_handle_func(signum, frame):
    global SIGNAL_INFO
    global MESSAGE
    print(MESSAGE[0])
    SIGNAL_INFO[0] = signum


# TODO ВОЗМОЖНО не работает в многопоточном режиме!
class Kisa():
    """
    Класс для реализации критически важного кода
        код будет выполнен в Kisa даже при нажатии Ctrl+C и kill9

    ВАЖНО: Kisa не перехватывает ВСЕ исключения.
    Только те, что отвечают за останов программы

    Список исключений можно изменить в DEFAULT_SIGNALS_LIST
    либо явно, задав в конструкторе

    Использование:

    >>  with Kisa():
    >>      ...
    >>      ...

    Можно задать два сообщения.
    первое -- при сигнале, второе после вызова __exit__

    >>  with Kisa("Ааа... Вы хотите завершить меня! Сейчас...", "Все, теперь можно завершать") as kise:
    >>      ...
    >>      ...

    """

    def __init__(
            self,
            signal_message=DEFAULT_SIGNAL_MESSAGE,
            end_work_message=DEFAULT_END_WORK_MESSAGE,
            signals_list=DEFAULT_SIGNALS_LIST,
            do_signal=default_do_signal,
    ):
        """
        Init Kise

        use init in with statment:

        >>  with Kise(...) as kise:
        >>      ...
        >>      ...

        :param signal_message: сообщение при получении сигнала
        :param end_work_message: сообщение после выполнении работы,
        в случае получения сигнала
        :param signals_list: список отлавливаемых сигналов
        """
        self.signals_list = signals_list
        self.signal_message = signal_message
        self.end_work_message = end_work_message
        self.do_signal = do_signal

    def __enter__(self):
        # signal.signal(signal.SIGINT, signal.SIG_IGN)
        global MESSAGE

        for sig in self.signals_list:
            signal.signal(sig, default_handle_func)
        MESSAGE[0] = self.signal_message
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 'Returning control to default signal handler'
        global SIGNAL_INFO
        for sig in self.signals_list:
            signal.signal(sig, signal.SIG_DFL)
        if SIGNAL_INFO[0]:
            print(self.end_work_message)
            self.do_signal(signal_no=SIGNAL_INFO[0])


def __test():
    from time import sleep
    print('Test Kisa! ')

    with Kisa():
        for i in range(10):
            print('{0}\tPlease press Ctrl+v!'.format(i))
            sleep(1)
        print('This is critical code!')

    print("This is not critical code. If you see it, you didn't pass CTRL+V!")

if __name__ == "__main__":
    __test()

