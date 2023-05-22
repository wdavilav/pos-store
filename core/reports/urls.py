from django.urls import path

from core.reports.views.sale_report.views import SaleReportView

urlpatterns = [
    path('sale/', SaleReportView.as_view(), name='sale_report'),
]
