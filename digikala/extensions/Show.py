from django.utils import timezone

class show_now():
    now=timezone.now()
    def show_it(self):
        return self.now()