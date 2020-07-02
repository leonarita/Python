from win10toast import ToastNotifier
import time

toaster = ToastNotifier()

toaster.show_toast("Notificação", "Alert! Yes", threaded=True, icon_path=None, duration=5)

while toaster.notification_active():
    time.sleep(0.1)

