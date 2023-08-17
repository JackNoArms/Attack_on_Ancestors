class Time:
    def __init__(self, horas=0):
        self.horas = horas

    def set_day_shift(self):
        if 19 <= self.horas <= 23 or 0 <= self.horas < 5:
            return "Noite"
        elif 5 <= self.horas < 13:
            return "Manha"
        elif 13 <= self.horas < 19:
            return "Tarde"

    def advance_time(self, horas=0):
        self.horas += horas
        self.horas %= 24
    
    def show_time(self):
        return f"{self.horas:02d}:00"
