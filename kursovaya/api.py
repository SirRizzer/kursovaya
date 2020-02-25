import csv
from .models import Statistic


class FileReader:
    """
    Реализация паттерна 'Студент'
    """

    def read_file(self, uploaded_file, extension):
        reader = self._get_reader(extension)
        if reader:
            return reader(uploaded_file)
        else:
            return None

    def _get_reader(self, extension):
        if extension == '.txt':
            return self._read_txt_file
        elif extension == '.csv':
            return self._read_csv_file

    @staticmethod
    def _read_txt_file(uploaded_file):
        contents = []
        with open(uploaded_file, 'r') as file:
            for line in file:
                contents.append(line.rstrip().split())
        return contents

    @staticmethod
    def _read_csv_file(uploaded_file):
        content = []
        with open(uploaded_file) as file:
            reader = csv.reader(file, delimiter=',')
            for line in reader:
                content.append(line)
        return content


class Command:
    """
    Реализация паттерна команда
    """

    def execute(self, content):
        raise NotImplementedError()

    def name(self):
        raise NotImplementedError()


class GetMinimumMark(Command):
    def execute(self, content):
        min_mark = []
        for row in content[1:]:
            min_mark = min(list(map(float, row[1:])))
            min_mark.extend([
                row[0],
                min_mark,
            ])
            values = {
                'type': row[0],
                'min_mark ': min_mark,
            }
            record, created = Statistic.objects.update_or_create(
                type=row[0], defaults=values)
        return ', '.join(list(map(str, min_mark)))

    def name(self):
        return 'min_mark'


class GetMaximumMark(Command):
    def execute(self, content):
        max_mark = []
        for row in content[1:]:
            max_mark = max(list(map(float, row[1:])))
            max_mark.extend([row[0], max_mark, ])
            values = {
                'subject': row[0],
                'max_mark': max_mark,
            }
            record, created = Statistic.objects.update_or_create(
                type=row[0], defaults=values)
        return ', '.join(list(map(str, max_mark)))

    def name(self):
        return 'max_mark'
