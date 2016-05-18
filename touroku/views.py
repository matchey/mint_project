from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect

from .forms import TourokuForm
from .models import Kansuu


class TourokuView():
    template_name = 'touroku/tourokuform.html'
    func_name = ""
    program_name = ""
    explanation = ""

    def touroku(request):
        if request.method == "POST":
            f = TourokuForm(request.POST)
            # f = TourokuForm(request.GET)
            # check whether it's valid:
            if f.is_valid():
                # process the data in form.cleaned_data as required
                func_name = f.cleaned_data["func_name"]
                program_name = f.cleaned_data["program_name"]
                explanation = f.cleaned_data["explanation"]
                # redirect to a new URL:
                return HttpResponseRedirect('/func_name/')
        else:
            # f = TourokuForm({"func_name":"add1","program_name":"cal1","explanation":"足し算をする関数1"})
            f = TourokuForm()
        return render(request, "touroku/tourokuform.html", {"form1": f})


class ListView():
    # template_name = 'touroku/tourokuform.html'
    func_name = ""
    program_name = ""
    explanation = ""
    
    def lists(request):
        # f = get_object_or_404(Kansuu, pk=kansuu_id)
        # f = Kansuu(pk=request.POST)
        f = TourokuForm(request.POST)
        fn = f["func_name"].value
        fnc = f["func_name"]
        pn = f["program_name"].value
        disp="is added"

        if f.is_valid():
            # func = Kansuu(f.cleaned_data)
            func = Kansuu()
            func.kansu_name=f.cleaned_data["func_name"]
            func.program_name=f.cleaned_data["program_name"]
            func.setsumei=f.cleaned_data["explanation"]
            func.save()
            if func.program_name in "hoge":
                disp="is found!!!!!!!!!!!!!!!!"
            return render(request, "touroku/lists.html", {"list1": fn,"list2": disp})
        else:
            return render(request, "touroku/tourokuform.html", {"form1": f})
