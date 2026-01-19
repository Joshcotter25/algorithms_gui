class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def notify(self, message: str):
        for obs in self._observers:
            obs.update(message)

class TextBoxObserver:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def update(self, message: str):
        self.text_widget.insert("end", message + "\n")
        self.text_widget.see("end")