import json
from collections import OrderedDict
from django.http import HttpResponse
from sail.models import Book

# Create your views here.

data = {'id': 1, 'name': 'hoge'}
json_str = json.dump(data, ensure_ascii=False, indent=2)
