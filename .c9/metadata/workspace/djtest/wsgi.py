{"filter":false,"title":"wsgi.py","tooltip":"/djtest/wsgi.py","undoManager":{"mark":11,"position":11,"stack":[[{"group":"doc","deltas":[{"start":{"row":14,"column":0},"end":{"row":15,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":15,"column":0},"end":{"row":18,"column":43},"action":"insert","lines":["from django.core.wsgi import get_wsgi_application","from dj_static import Cling","","application = Cling(get_wsgi_application())"]}]}],[{"group":"doc","deltas":[{"start":{"row":12,"column":0},"end":{"row":13,"column":36},"action":"remove","lines":["from django.core.wsgi import get_wsgi_application","application = get_wsgi_application()"]}]}],[{"group":"doc","deltas":[{"start":{"row":11,"column":0},"end":{"row":12,"column":0},"action":"remove","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":10,"column":66},"end":{"row":11,"column":0},"action":"remove","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":15,"column":43},"end":{"row":16,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":16,"column":0},"end":{"row":17,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":17,"column":0},"end":{"row":22,"column":0},"action":"insert","lines":["import os","os.environ.setdefault(\"DJANGO_SETTINGS_MODULE\", \"djtest.settings\")","","from django.core.wsgi import get_wsgi_application","application = get_wsgi_application()",""]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":0},"end":{"row":15,"column":43},"action":"remove","lines":["","import os","os.environ.setdefault(\"DJANGO_SETTINGS_MODULE\", \"djtest.settings\")","","from django.core.wsgi import get_wsgi_application","from dj_static import Cling","","application = Cling(get_wsgi_application())"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":3},"end":{"row":8,"column":0},"action":"remove","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":14,"column":0},"end":{"row":15,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":15,"column":0},"end":{"row":19,"column":43},"action":"insert","lines":["from django.core.wsgi import get_wsgi_application","from whitenoise.django import DjangoWhiteNoise","","application = get_wsgi_application()","application = DjangoWhiteNoise(application)"]}]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":19,"column":43},"end":{"row":19,"column":43},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1425308933142,"hash":"4134f134e761699db35e80053f232dfc14515881"}