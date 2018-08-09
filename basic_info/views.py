from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
import twstock, datetime


# Create your views here.
class IndexView(View):

    def get(self, request, *args, **kwargs):
        try:
            return render(request, "basic_info/index.html", locals())
        except Exception as e:
            raise

    def post(self, request, *args, **kwargs):
        try:

            stock_id = request.POST.get('stock_id', '')
            date = request.POST.get('date', '')
            date = datetime.datetime.strptime(date, '%Y/%m/%d')

            stock_info = twstock.codes[stock_id]
            stock = twstock.Stock(stock_id)
            data = stock.fetch_from(date.year, date.month)
            name = stock_info[1] + stock_info[2]

            price = stock.price

            date = []

            for item in stock.date:
                item = datetime.datetime.strftime(item, "%Y-%m-%d")
                date.append(item)

            return JsonResponse({'result': True, 'date': date, 'name': name, 'price': price})

        except Exception as e:
            return JsonResponse({'result': False})
            # raise
