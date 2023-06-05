import json
weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
commandlist = ['load', 'add', 'save', 'show', 'exit']
class DailyPlan:
    def __init__(self):
        self.week = self.prepare_week()

    def prepare_week(self):
        week = dict()
        week['monday'] = []
        week['tuesday'] = []
        week['wednesday'] = []
        week['thursday'] = []
        week['friday'] = []
        week['saturday'] = []
        week['sunday'] = []
        return week

    def save(self):
        while 1:
            filename = input('File Name? ')
            if filename.endswith('.json'):
                break
            else:
                print('Only .json files are allowed')

        json_object = json.dumps(self.week)
        with open(filename, "w") as outfile:
            outfile.write(json_object)
        return

    def show(self):
        day=input('Which Day? ')
        day = day.lower()
        print('Your Plan for '+day.title()+' is:')
        for item in self.week.get(day):
            print(item.get('start')+' - '+item.get('end')+' : '+ item.get('comment'))
        return

    def load(self):
        while 1:
            filename = input('File Name? ')
            if filename.endswith('.json'):
                break
            else:
                print('Only .json files are allowed')
        try:
            with open(filename, 'r') as openfile:
                json_object = json.load(openfile)
            self.week = json_object
        except Exception as e:
            print(e)

    def add(self):
        while 1:
            day = input('Which day? ')
            day = day.lower()
            if day not  in weekdays:
                print('Inavlid day')
            else:
                break
        start = input('Start time? ')
        end = input('End time? ')
        comment = input('Plan? ')
        obj = dict()
        obj['start'] = start
        obj['end'] = end
        obj['comment'] =comment
        self.week[day].append(obj)

    def exit(self):
        raise SystemExit


    def execute(self):
        while 1:
            print('Choose '+ ' '.join(commandlist))
            command = input('choose from list ')
            try:
                func = getattr(self, command)
                func()
            except Exception as e:
                print(e)


plan = DailyPlan()
plan.execute()

